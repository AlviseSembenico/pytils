from typing import Any, Iterator

from pytils.dictionary import get_nested_value, set_nested_value


class IterMapper:
    items: Iterator
    path: str
    batch_size: int

    def __init__(self, items: Iterator, path: str, batch_size=-1) -> None:
        self.items = items
        self.path = path
        self.batch_size = batch_size
        if "[]" in path:
            raise Exception("Array indexing for IterMapper not supported yet")

    def __getitem__(self, index: int):
        res = get_nested_value(self.items[index], self.path)
        return res

    def __setitem__(self, index: int, value: Any):
        self.items[index] = set_nested_value(self.items[index], self.path, value)
