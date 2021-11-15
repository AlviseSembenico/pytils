from copy import deepcopy
from typing import Any, Dict


def merge_dicts(a: Dict, b: Dict):
    """Merge two dictionaries in a recursive way.
    It means that if there is a key match, the keys is merged as well.
    Only dict and list keys merging is supported
    Args:
        a (Dict):
        b (Dict)
    Raises:
        ValueError: if a key is present in both the dictionaries and does not falls
        in one of these classes: Dict, List
    """
    res = deepcopy(a)
    for k, v in b.items():
        if k not in res:
            res[k] = v
        else:
            if isinstance(v, dict):
                res[k] = merge_dicts(res[k], v)
            elif isinstance(v, list):
                res[k] += v
            else:
                raise ValueError(
                    f"""Impossible to merge {res[k].__class__} and {v.__class__}.
                    Data structure combinations not supported. Only merge between list and dict possible"""
                )
    return res


def get_key(obj: Any, key: str):
    try:
        return obj.get(key)
    except:
        return getattr(obj, key)


def set_key(obj: Any, key: str, value: Any):
    try:
        obj[key] = value
    except:
        setattr(obj, key, value)


def get_nested_value(obj: Any, path: str) -> Any:
    if "[]" in path:
        raise Exception(
            "This function works only for non array objects. Use get_nested_values instead"
        )
    keys = path.split(".")
    current_key = keys[0]
    if len(keys) == 1:
        return get_key(obj, path)
    return get_nested_value(get_key(obj, current_key), ".".join(keys[1:]))


def set_nested_value(obj: Any, path: str, value: Any) -> Any:
    def aux(obj: Any, path: str, value: Any):
        keys = path.split(".")
        current_key = keys[0]
        if len(keys) == 1:
            set_key(obj, path, value)
            return

        aux(get_key(obj, current_key), ".".join(keys[1:]), value)

    instance = deepcopy(obj)
    aux(instance, path, value)
    return instance


def get_nested_values(obj: Any, path: str) -> Any:
    keys = path.split(".")
    current_key = keys[0]
    if len(keys) == 1:
        return get_key(obj, path)

    if current_key.endswith("[]"):
        current_key = current_key[:-2]
        return [
            get_nested_values(element, ".".join(keys[1:]))
            for element in get_key(obj, current_key)
        ]
    return get_nested_values(get_key(obj, current_key), ".".join(keys[1:]))
