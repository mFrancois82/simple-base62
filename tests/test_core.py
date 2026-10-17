import unittest

from simple_base62 import CHARSET, encode, decode


class TestEncode(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(encode(0), "0")

    def test_single_digit_values(self):
        for i in range(62):
            self.assertEqual(encode(i), CHARSET[i])

    def test_first_two_digit(self):
        self.assertEqual(encode(62), CHARSET[1] + CHARSET[0])

    def test_negative_rejected(self):
        with self.assertRaises(ValueError):
            encode(-1)


class TestDecode(unittest.TestCase):
    def test_zero_string(self):
        self.assertEqual(decode("0"), 0)

    def test_each_single_char(self):
        for i, c in enumerate(CHARSET):
            self.assertEqual(decode(c), i)

    def test_first_two_digit(self):
        self.assertEqual(decode(CHARSET[1] + CHARSET[0]), 62)

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            decode("")

    def test_invalid_char_rejected(self):
        with self.assertRaises(ValueError):
            decode("abc!")

    def test_type_check(self):
        with self.assertRaises(TypeError):
            decode(b"abc")


class TestRoundTrip(unittest.TestCase):
    def _check(self, n):
        self.assertEqual(decode(encode(n)), n)

    def test_boundary_values(self):
        for n in [0, 1, 61, 62, 63, 3843, 3844]:
            self._check(n)

    def test_powers_of_62(self):
        for k in range(8):
            self._check(62 ** k)

    def test_large(self):
        self._check(2 ** 128)


if __name__ == "__main__":
    unittest.main()
