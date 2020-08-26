import math
from dataclasses import dataclass
from enum import Enum
from typing import List


class STYLE_TYPE(Enum):
    WESTERN = "western"
    JAPAN = "japan"


@dataclass
class CollatedOrder:
    front: List[int]
    back: List[int]


def order_in_western_style(total: int) -> CollatedOrder:
    front_collated = []
    back_collated = []
    total_pages = math.ceil(total / 4)

    for i in range(1, total_pages + 1):
        reverse_index = (total_pages * 2) - i + 1
        front_collated.append(reverse_index * 2)
        front_collated.append(2 * i - 1)
        back_collated.append(2 * i)
        back_collated.append(reverse_index * 2 - 1)

    return CollatedOrder(front=front_collated, back=back_collated)


def order_in_japan_style(total: int) -> CollatedOrder:
    western_order = order_in_western_style(total)
    front_collated = western_order.front or []
    back_collated = western_order.back or []
    front_collated.reverse()
    back_collated.reverse()
    return CollatedOrder(front=front_collated, back=back_collated)


ORDER_FACTORY = {
    STYLE_TYPE.WESTERN: order_in_western_style,
    STYLE_TYPE.JAPAN: order_in_japan_style,
}
