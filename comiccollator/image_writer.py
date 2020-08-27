import os
from enum import Enum
from typing import Optional

from PIL import Image

from comiccollator.collator import CollatedOrder
from comiccollator.utils import progress


class PRINT_ORDER(Enum):
    ASC = 0
    DESC = 1

def concat_couples(
    list_of_pages: CollatedOrder,
    path: str,
    extension: str,
    default_image: Optional[str] = None,
    back_order: PRINT_ORDER = PRINT_ORDER.ASC,
    wet_run: bool = False,
):
    assert len(list_of_pages.front) == len(list_of_pages.back)
    steps = 2
    print("Front pages")
    total = len(list_of_pages.front)
    for index, i in enumerate(range(0, total, steps), 1):
        if wet_run:
            progress(index/(total/steps))
        output_name = "{}front-{}.{}".format(path, str(index).zfill(3), extension)
        concat_couple(
            path,
            list_of_pages.front[i],
            list_of_pages.front[i + 1],
            output_name,
            extension,
            default_image,
            wet_run,
        )

    print("\nBack page")
    for index, i in enumerate(range(0, total, steps), 1):
        if wet_run:
            progress(index/(total/steps))
        back_order_index = int((total/steps)) - index + 1
        back_order_sufix = '{}-for_front_'.format(str(back_order_index).zfill(3)) if back_order == PRINT_ORDER.DESC else ''
        output_name = "{}back-{}{}.{}".format(path, back_order_sufix, str(index).zfill(3), extension)
        concat_couple(
            path,
            list_of_pages.back[i],
            list_of_pages.back[i + 1],
            output_name,
            extension,
            default_image,
            wet_run,
        )
    print("\ndone")


def concat_couple(
    path: str,
    index_a: int,
    index_b: int,
    output_name: str,
    extension: str,
    default_image: Optional[str] = None,
    wet_run: bool = False,
):
    image_a = get_image_name(path, index_a, extension, default_image)
    image_b = get_image_name(path, index_b, extension, default_image)
    if wet_run:
        new_image = concat(image_a, image_b)
        new_image.save(output_name)
    else:
        print(" ".join([image_a, image_b, output_name]))


def get_image_name(
    path: str, index: int, extension: str, default_image: Optional[str] = None
) -> str:
    """
    attempt to find filename like 1.{extension} or 01.{extension} or 001.{extension}
    """
    for i in range(1, 4):
        image_name = "{}{}.{}".format(path, str(index).zfill(i), extension)
        image_name = _get_image_or_default(image_name)
        if image_name:
            return image_name
    else:
        if default_image:
            return default_image
        else:
            images_searched = ['{}.{}'.format(index, extension)]
            if index < 100:
                images_searched.append('0{}.{}'.format(index, extension))
            if index < 10:
                images_searched.append('00{}.{}'.format(index, extension))
            raise FileNotFoundError("File not found({})".format(' or '.join(images_searched)))



def _get_image_or_default(image_absolute: str) -> Optional[str]:
    """
    :raise FileNotFoundError
    """
    if os.path.exists("{}".format(image_absolute)):
        return image_absolute
    else:
        return None


def concat(
    image_a: str,
    image_b: str,
    mode: str = "RGB",
    resample: int = Image.BICUBIC,
    resize_big_image: bool = True,
):
    im1 = Image.open(image_a)
    im2 = Image.open(image_b)

    if im1.height == im2.height:
        _im1 = im1
        _im2 = im2
    elif ((im1.height > im2.height) and resize_big_image) or (
        (im1.height < im2.height) and not resize_big_image
    ):
        _im1 = im1.resize(
            (int(im1.width * im2.height / im1.height), im2.height), resample=resample
        )
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize(
            (int(im2.width * im1.height / im2.height), im1.height), resample=resample
        )

    dst = Image.new(mode, (_im1.width + _im2.width, _im1.height))
    dst.paste(_im1, (0, 0))
    dst.paste(_im2, (_im1.width, 0))
    return dst
