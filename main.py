import argparse
import printcomic


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

    printcomic.create_printable_pages(
        args.style, args.path, args.extension, args.default_image, args.wet_run
    )


if __name__ == "__main__":
    main()
