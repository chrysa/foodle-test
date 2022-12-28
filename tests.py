import unittest

from parameterized import parameterized

from count_words import count_words


class CountWordTestCase(unittest.TestCase):
    @parameterized.expand([
        [
            "baz bar foo foo zblah zblah zblah baz toto bar", 1, [("zblah", 3), ]
        ],
        [
            "baz bar foo foo zblah zblah zblah baz toto bar", 2, [("zblah", 3), ("bar", 2), ]
        ],
        [
            "baz bar foo foo zblah zblah zblah baz toto bar", 3, [("zblah", 3), ("bar", 2), ("baz", 2), ]
        ],
        [
            "baz bar foo foo zblah zblah zblah baz toto bar", 4,
            [("zblah", 3), ("bar", 2), ("baz", 2), ('foo', 2), ]
        ],
        [
            "baz bar foo foo zblah zblah zblah baz toto bar", 5,
            [("zblah", 3), ("bar", 2), ("baz", 2), ('foo', 2), ('toto', 1), ]
        ]
    ])
    def test_count_words(self, input_string: str, size: int, result: list[tuple[str, int]]) -> None:
        self.assertEqual(count_words(sentence=input_string, n=size), result)

    def test_count_over(self) -> None:
        self.assertEqual(count_words(sentence="baz bar foo foo zblah zblah zblah baz toto bar", n=6),[("zblah", 3), ("bar", 2), ("baz", 2), ('foo', 2), ('toto', 1), ])

    @parameterized.expand([(0,), (1,)])
    def test_empty(self, size: int) -> None:
        self.assertEqual(count_words(sentence='', n=size), [])


if __name__ == '__main__':
    unittest.main()
