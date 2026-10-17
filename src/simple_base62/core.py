"""Core encode/decode logic.

CHARSET ordering is 0-9, then A-Z, then a-z. This is the most common
convention and keeps digits lexicographically before letters, which tends
to make human-eyeballed IDs sort sensibly when the lengths are equal.
"""

CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# length == 62, indices == code points' positions in CHARSET
assert len(CHARSET) == 62
assert len(set(CHARSET)) == 62

_CHAR_TO_VALUE = {c: i for i, c in enumerate(CHARSET)}


def encode(n: int) -> str:
    """Encode a non-negative int into Base62.

    Returns "0" for n == 0 so round-tripping with decode works: decode("")
    is a ValueError, and returning "" from encode(0) would break that contract.
    Negative inputs raise ValueError because Base62 has no sign bit here.
    """
    if n < 0:
        raise ValueError("base62 cannot encode negative integers")
    if n == 0:
        return "0"
    chars: list[str] = []
    while n > 0:
        n, r = divmod(n, 62)
        chars.append(CHARSET[r])
    return "".join(reversed(chars))


def decode(s: str) -> int:
    """Decode a Base62 string into its int.

    Empty input and any character outside CHARSET are ValueErrors; the caller
    passed us garbage and should not get a silently-wrong answer back.
    """
    if not isinstance(s, str):
        raise TypeError("decode expects str, got " + type(s).__name__)
    if s == "":
        raise ValueError("cannot decode empty string")
    result = 0
    for c in s:
        v = _CHAR_TO_VALUE.get(c)
        if v is None:
            raise ValueError("invalid base62 character: " + repr(c))
        result = result * 62 + v
    return result
