import glob
import os

from printcomic.collator import ORDER_FACTORY, STYLE_TYPE, CollatedOrder
from printcomic.image_writer import PRINT_ORDER, concat_couples


def create_printable_pages(
    style: str,
    path: str,
    extension: str,
    default_image: str,
    back_order: str,
    wet_run: bool,
):
    validate_params(path, default_image)
    order_pages = get_order_pages(
        style=get_collator_style(style),
        total=count_files(path, extension),
    )
    concat_couples(
        order_pages,
        path=path,
        extension=extension,
        default_image=default_image,
        back_order=get_print_order(back_order),
        wet_run=bool(wet_run),
    )


def get_order_pages(style: STYLE_TYPE, total: int) -> CollatedOrder:
    if total > 99:
        # TODO: support without limit
        raise ValueError("Only supported until 99 images for now")
    return ORDER_FACTORY[style](total)


def count_files(path: str, extension: str) -> int:
    if not path:
        return 0
    else:
        return len(glob.glob1(path, "*.{}".format(extension)))


def get_print_order(order: str):
    if order == "DESC":
        return PRINT_ORDER.DESC
    elif order == "ASC":
        return PRINT_ORDER.ASC
    else:
        return PRINT_ORDER.ASC


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
