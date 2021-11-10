import itertools
from typing import Any, Callable, List


def inflate(method: Callable, args: List[List[Any]]):
    data = list(itertools.chain(*args))
    res = method(data)
    if res is None:
        return
    else:
        res = list(res)
    result, index = [], 0
    for datapoint in args:
        result.append(res[index : index + len(datapoint)])
        index += len(datapoint)
    return result
