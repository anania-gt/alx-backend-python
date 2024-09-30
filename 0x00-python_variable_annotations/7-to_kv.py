from typing import tuple, union


def to_kv(k: str, v: union[int, float])-> tuple[str, float]:

    return (k, float(v**2))
