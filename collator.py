import math
from typing import List

def order_in_western_style(total: int) -> List[int]:
    list_of_pages = []
    total_pages = math.ceil(total/4)

    for i in range(1, total_pages+1):
        reverse_index = (total_pages * 2) - i + 1
        list_of_pages.append(reverse_index * 2)
        list_of_pages.append(2 * i - 1)
        list_of_pages.append(2 * i)
        list_of_pages.append(reverse_index * 2 - 1)

    return list_of_pages

def order_in_japan_style(total: int) -> List[int]:
    list_of_pages = []
    total_pages = math.ceil(total/4)

    for i in range(1, total_pages+1):
        pass

    return list_of_pages
