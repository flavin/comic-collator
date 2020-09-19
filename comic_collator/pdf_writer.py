from typing import List

from PIL import Image


def images_files_to_pdf(files: List[str], output_name: str):
    image_list = list(map(get_rgb_image, files))
    images_to_pdf(image_list, output_name)


def images_to_pdf(image_list: List, output_name: str):
    first_image = image_list[0]
    if not first_image:
        return
    rest_of_images = image_list[1:] or []
    first_image.save(output_name, save_all=True, append_images=rest_of_images)


def get_rgb_image(image_file_name: str) -> Image:
    img = Image.open(image_file_name)
    img.convert("RGB")
    return img
