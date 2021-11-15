from typing import Any, Iterator, List

from pytils.dictionary import get_nested_values, set_nested_value


class IterMapper:
    items: List
    path: str
    batch_size: int

    def __init__(self, items: List, path: str, batch_size=-1) -> None:
        self.items = items
        self.path = path
        self.batch_size = batch_size
        self.index = 0

    def __getitem__(self, index: int):
        current_index = 0
        for item in self.items:
            values = get_nested_values(item, self.path)
            if not isinstance(values, list):
                values = [values]
            if index - len(values) < current_index < index + len(values):
                return values[index - current_index]
            current_index += len(values)

    def __setitem__(self, index: int, value: Any):
        self.items[index] = set_nested_value(self.items[index], self.path, value)

    def __iter__(self):
        for item in self.items:
            values = get_nested_values(item, self.path)
            if not isinstance(values, list):
                values = [values]
            for value in values:
                yield value

    def __next__(self):
        res = self.__getitem__(self.index)
        self.index += 1
        return res
