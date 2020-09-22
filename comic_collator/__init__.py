import glob
import os
import time

from comic_collator.collator import ORDER_FACTORY, STYLE_TYPE, CollatedOrder
from comic_collator.image_writer import PRINT_ORDER, concat_couples
from comic_collator.pdf_writer import images_to_pdf


def create_printable_pages(
    style: str,
    path: str,
    extension: str,
    default_image: str,
    back_order: str,
    wet_run: bool,
):
    validate_params(style, path, default_image, back_order)
    total_of_files = count_files(path, extension)
    if total_of_files < 2:
        print('Not enought images(need 2 or more)')
        return
    order_pages = get_order_pages(
        style=get_collator_style(style), total=total_of_files,
    )
    front_images, back_images = concat_couples(
        order_pages,
        path=path,
        extension=extension,
        default_image=default_image,
        back_order=get_print_order(back_order),
        wet_run=bool(wet_run),
    )
    millis = int(round(time.time() * 1000))
    images_to_pdf(front_images, f"{path}/front-{millis}.pdf")
    images_to_pdf(back_images, f"{path}/back-{millis}.pdf")


def get_order_pages(style: STYLE_TYPE, total: int) -> CollatedOrder:
    if total > 999:
        raise ValueError("Only supported until 999 images for now")
    return ORDER_FACTORY[style](total)


def count_files(path: str, extension: str) -> int:
    if not path:
        return 0
    else:
        return len(glob.glob1(path, f"*.{extension}"))


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


def validate_params(style: str, path: str, default_image: str, back_order: str):
    """
    :raise ValueError
    :raise LookupError
    """
    if not path.endswith("/"):
        raise ValueError('Path must to end with "/"')

    if style not in ["japan", "western"]:
        raise ValueError(f"Style {style} not supported")

    if back_order not in ["DESC", "ASC"]:
        raise ValueError(f"Back order not supported {back_order} not supported")

    if not default_image.startswith("/"):
        raise ValueError("Default image must to be an absolute filename")

    if not os.path.exists(f"{default_image}"):
        raise LookupError("Not found the default image")
