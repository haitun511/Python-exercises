from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return [elements[0] for i in range(len(elements))] == elements