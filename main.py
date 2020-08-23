import os
import argparse

from collator import order_in_western_style
from image_writer import write_couples


def process(total: int) -> list:
    return order_in_western_style(total)


def count_files(path: str) -> int:
    if not path:
        return 0
    else:
        return len(os.listdir(path))

def main():
    parser = argparse.ArgumentParser("Script to generate page to print comics")
    parser.add_argument("-t", "--total", type=int, help="Number of images")
    parser.add_argument("-p", "--path", type=str, help="Image path")
    parser.add_argument("-e", "--extension", type=str, required=True, help="Extension")
    parser.add_argument("-w", "--wet_run", type=int, help="wet run")
    parser.add_argument(
        "-di",
        "--default_image",
        type=str,
        help="default image if current doesn't exists",
    )
    args = parser.parse_args()

    total = count_files(path=args.path)
    list_of_pages = process(total=total or args.total)
    write_couples(
        list_of_pages,
        path=args.path,
        extension=args.extension,
        default_image=args.default_image,
        wet_run=bool(args.wet_run),
    )


if __name__ == "__main__":
    main()
