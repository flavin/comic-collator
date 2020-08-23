import os
import subprocess
from typing import Optional


def write_couples(
    list_of_pages: list,
    path: str,
    extension: str,
    default_image: Optional[str] = None,
    wet_run: bool = False,
):
    print("first round")
    index = 0
    for i in range(0, len(list_of_pages), 4):
        index += 1
        args = prepare_command_arg(
            index,
            list_of_pages[i],
            list_of_pages[i + 1],
            path,
            "front",
            extension,
            default_image,
        )
        if wet_run:
            subprocess.run(*args)
        else:
            print(" ".join(args))
    print("second round")
    for i in range(2, len(list_of_pages), 4):
        index += 1
        args = prepare_command_arg(
            index,
            list_of_pages[i],
            list_of_pages[i + 1],
            path,
            "back",
            extension,
            default_image,
        )
        if wet_run:
            subprocess.run(*args)
        else:
            print(" ".join(args))


def prepare_command_arg(
    index: int,
    index_a: int,
    index_b: int,
    path: str,
    prefix: str,
    extension: str,
    default_image: Optional[str] = None,
) -> list:
    image_a = "{}.{}".format(str(index_a).zfill(2), extension)
    image_a = _get_image_or_default(path, image_a, default_image)
    image_b = "{}.{}".format(str(index_b).zfill(2), extension)
    image_b = _get_image_or_default(path, image_b, default_image)
    output = "{}-{}.{}".format(prefix, str(index).zfill(2), extension)

    args = ["convert", image_a, image_b, "+append", output]
    return args


def _get_image_or_default(
    path: str, image: str, default_image: Optional[str] = None
) -> str:
    """
    :raise FileNotFoundError
    """
    if not os.path.exists("{}{}".format(path, image)):
        if default_image:
            image = default_image
        else:
            raise FileNotFoundError("{} not found".format(image))
    return image
