import glob
import os

from printcomic.collator import ORDER_FACTORY, STYLE_TYPE
from printcomic.image_writer import concat_couples


def create_printable_pages(
    style: str, path: str, extension: str, default_image: str, wet_run: bool
):
    validate_params(path, default_image)
    collator_style = get_collator_style(style)
    files_count = count_files(path, extension)
    if files_count > 99:
        raise ValueError(
            "Only supported until 99 images for now"
        )  # TODO: support without limit
    order_pages = get_order_pages(style=collator_style, total=files_count)
    print(order_pages)
    concat_couples(
        order_pages,
        path=path,
        extension=extension,
        default_image=default_image,
        wet_run=bool(wet_run),
    )


def get_order_pages(style: STYLE_TYPE, total: int) -> list:
    return ORDER_FACTORY[style](total)


def count_files(path: str, extension: str) -> int:
    if not path:
        return 0
    else:
        return len(glob.glob1(path, "*.{}".format(extension)))


def get_collator_style(style: str) -> STYLE_TYPE:
    valid_styles = ["western", "japan"]
    if style in valid_styles:
        return STYLE_TYPE(style)
    else:
        return STYLE_TYPE("western")


def validate_params(path: str, default_image: str):
    """
    :raise ValueError
    :raise LookupError
    """
    if not path.endswith("/"):
        raise ValueError('Path must to end with "/"')

    if not default_image.startswith("/"):
        raise ValueError("Default image must to be an absolute filename")

    if not os.path.exists("{}".format(default_image)):
        raise LookupError("Not found the default image")
