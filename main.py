import os
import argparse

from collator import ORDER_FACTORY, STYLE_TYPE
from image_writer import write_couples


def get_order_pages(style: STYLE_TYPE, total: int) -> list:
    return ORDER_FACTORY[style](total)


def count_files(path: str) -> int:
    if not path:
        return 0
    else:
        return len(os.listdir(path))


def get_collator_style(style: str) -> STYLE_TYPE:
    valid_styles = ["western", "japan"]
    if style in valid_styles:
        return STYLE_TYPE(style)
    else:
        return STYLE_TYPE("western")


def main():
    parser = argparse.ArgumentParser("Script to generate page to print comics")
    parser.add_argument("-t", "--total", type=int, help="Number of images")
    parser.add_argument("-p", "--path", type=str, help="Image path")
    parser.add_argument("-e", "--extension", type=str, required=True, help="Extension")
    parser.add_argument("-w", "--wet_run", type=int, help="wet run")
    parser.add_argument(
        "-s", "--style", type=str, help="type 'western' or 'japan'", default="western"
    )
    parser.add_argument(
        "-di",
        "--default_image",
        type=str,
        help="default image if current doesn't exists",
    )
    args = parser.parse_args()

    collator_style = get_collator_style(args.style)
    files_count = count_files(path=args.path)
    order_pages = get_order_pages(style=collator_style, total=files_count or args.total)
    print(order_pages)
    write_couples(
        order_pages,
        path=args.path,
        extension=args.extension,
        default_image=args.default_image,
        wet_run=bool(args.wet_run),
    )


if __name__ == "__main__":
    main()
