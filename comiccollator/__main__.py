import argparse

import comiccollator


def main():
    parser = argparse.ArgumentParser("Script to generate page to print comics")
    parser.add_argument("-t", "--total", type=int, help="number of images")
    parser.add_argument("-p", "--path", type=str, help="image path")
    parser.add_argument("-e", "--extension", type=str, required=True, help="extension")
    parser.add_argument("-w", "--wet_run", type=int, help="wet run")
    parser.add_argument(
        "-bo", "--back_order", type=str, help="back images order", default="ASC"
    )
    parser.add_argument("-s", "--style", type=str, help="type 'western' or 'japan'", default="western")
    parser.add_argument(
        "-di",
        "--default_image",
        type=str,
        help="default image, to fill empty pages",
    )
    args = parser.parse_args()

    comiccollator.create_printable_pages(
        args.style,
        args.path,
        args.extension,
        args.default_image,
        args.back_order,
        args.wet_run,
    )


if __name__ == "__main__":
    main()
