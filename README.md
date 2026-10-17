# simple-base62

Encode non-negative integers as Base62 strings for short, URL-safe identifiers.

```python
from simple_base62 import encode, decode, CHARSET

encode(0)      # "0"
encode(61)      # "z"
encode(62)      # "10"
encode(3844)   # "100"
encode(2**128)  # "7n42Dk6eSEcXVi1A6egW1k"

decode("7n42Dk6eSEcXVi1A6egW1k") == 2**128  # True
```

## Why

URL path segments that double as identifiers want to be short, alphanumeric, and
free of punctuation that breaks routing or needs escaping. Base62 with the
alphabet `0-9A-Za-z` gives 62 symbols, all of which are URL-safe without
percent-encoding, and fits more bits per character than Base36. The trade-off
is that it only represents non-negative integers; if your IDs are signed or
already UUID-sized bytes, use something else.

## Edge cases

- `encode(0)` returns `"0"`, not `""`, so `decode(encode(0))` round-trips. An
  empty string is treated as invalid input to `decode` and raises `ValueError`.
- `encode(-1)` raises `ValueError`; there is no sign representation.
- Any character outside `CHARSET` passed to `decode` raises `ValueError`.
