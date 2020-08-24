import os
from typing import List, Optional

from PIL import Image


def concat_couples(
    list_of_pages: List[int],
    path: str,
    extension: str,
    default_image: Optional[str] = None,
    wet_run: bool = False,
):
    print("first round")
    index = 0
    for i in range(0, len(list_of_pages), 4):
        index += 1
        concat_couple(
            path,
            list_of_pages[i],
            list_of_pages[i + 1],
            index,
            "front",
            extension,
            default_image,
            wet_run,
        )

    print("second round")
    for i in range(2, len(list_of_pages), 4):
        index += 1
        concat_couple(
            path,
            list_of_pages[i],
            list_of_pages[i + 1],
            index,
            "back",
            extension,
            default_image,
            wet_run,
        )


def concat_couple(
    path: str,
    index_a: int,
    index_b: int,
    index_out: int,
    prefix,
    extension: str,
    default_image: Optional[str] = None,
    wet_run: bool = False,
):
    image_a = _get_image(path, index_a, extension, default_image)
    image_b = _get_image(path, index_b, extension, default_image)
    output = "{}{}-{}.{}".format(path, prefix, str(index_out).zfill(2), extension)
    if wet_run:
        new_image = concat(image_a, image_b)
        new_image.save(output)
    else:
        print(" ".join([image_a, image_b, output]))


def _get_image(
    path: str, index: int, extension: str, default_image: Optional[str] = None
) -> str:
    image_name = "{}{}.{}".format(path, str(index).zfill(2), extension)
    image_name = _get_image_or_default(image_name, default_image)
    return image_name


def _get_image_or_default(
    image_absolute: str, default_image: Optional[str] = None
) -> str:
    """
    :raise FileNotFoundError
    """
    if not os.path.exists("{}".format(image_absolute)):
        if default_image:
            image_absolute = default_image
        else:
            raise FileNotFoundError("{} not found".format(image_absolute))
    return image_absolute


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
