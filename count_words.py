import collections


def count_words(*, sentence: str, n: int) -> list[tuple[str, int]] | list[None]:
    result: list[tuple[str, int]] | list[None] = []
    if len(sentence):
        common_words: list[tuple[str, int]] = collections.Counter(sentence.split(' ')).most_common()
        result = sorted(common_words, key=lambda x: (-x[1], x[0]))[:n]
    return result


if __name__ == "__main__":
    result: list[tuple[str, int]] = count_words(sentence="baz bar foo foo zblah zblah zblah baz toto bar", n=3)
    print(result)
