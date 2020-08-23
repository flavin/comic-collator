import os
import argparse
import math
import subprocess
import typing


def process(total: int) -> list:
    list_of_pages = []
    total_pages = math.ceil(total/4)
    index_for_pages = 0

    for i in range(1, total_pages+1):
        reverse_index = (total_pages * 2) - i + 1
        list_of_pages.append(reverse_index * 2)
        list_of_pages.append(2 * i - 1)
        list_of_pages.append(2 * i)
        list_of_pages.append(reverse_index * 2 - 1)

    return list_of_pages

def write_couples(list_of_pages: list, path: str, extension: str, default_image: typing.Optional[str]=None, wet_run: bool=False):
    print('first round')
    index = 0
    for i in range(0, len(list_of_pages), 4):
        index += 1
        args = prepare_command_arg(index, list_of_pages[i], list_of_pages[i+1], path, 'front', extension, default_image)
        if wet_run:
            subprocess.run(*args)
        else:
            print(' '.join(args))
    print('second round')
    for i in range(2, len(list_of_pages), 4):
        index += 1
        args = prepare_command_arg(index, list_of_pages[i], list_of_pages[i+1], path, 'back', extension, default_image)
        if wet_run:
            subprocess.run(*args)
        else:
            print(' '.join(args))

def prepare_command_arg(index: int, index_a: int, index_b: int, path: str, prefix: str, extension: str, default_image: typing.Optional[str] = None) -> list:
    image_a = '{}.{}'.format(str(index_a).zfill(2), extension)
    image_a = _get_image_or_default(path, image_a, default_image)
    image_b = '{}.{}'.format(str(index_b).zfill(2), extension)
    image_b = _get_image_or_default(path, image_b, default_image)
    output = '{}-{}.{}'.format(prefix, str(index).zfill(2), extension)

    args = ['convert', image_a, image_b, '+append', output]
    return args

def _get_image_or_default(path: str, image: str, default_image: typing.Optional[str]=None) -> str:
    """
    :raise FileNotFoundError
    """
    if not os.path.exists('{}{}'.format(path, image)):
        if default_image:
            image = default_image
        else:
            raise FileNotFoundError('{} not found'.format(image))
    return image

def count_files(path: str) -> int:
    if not path:
        return 0
    else:
        return len(os.listdir(path))

def main():
    parser = argparse.ArgumentParser('Script to generate page to print comics')
    parser.add_argument('-t', '--total', type=int, dest='total', help='Number of images')
    parser.add_argument('-p', '--path', type=str, dest='path', help='Image path')
    parser.add_argument('-e', '--extension', type=str, required=True, dest='extension', help='Extension')
    parser.add_argument('-w', '--wet_run', type=int, dest='wet_run', help='wet run')
    parser.add_argument('-di', '--default_image', type=str, dest='default_image', help='default image if current doesn\'t exists')
    args = parser.parse_args()
    total = count_files(path=args.path)
    list_of_pages = process(total=total or args.total)
    print(list_of_pages)
    write_couples(
        list_of_pages,
        path=args.path,
        extension=args.extension,
        default_image=args.default_image,
        wet_run=bool(args.wet_run)
    )

if __name__ == '__main__':
    main()
