"""simple-base62: Base62 encoding for non-negative integers.

Exports:
    encode  -- int -> Base62 str
    decode  -- Base62 str -> int
    CHARSET -- the 62-symbol alphabet, in canonical order
"""

from .core import CHARSET, decode, encode

__all__ = ["CHARSET", "encode", "decode"]
