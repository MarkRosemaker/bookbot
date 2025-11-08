from collections import Counter


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> Counter[str]:
    return Counter(c for c in text.lower() if c.isalpha())


def sort_characters(chars: Counter[str]) -> list[dict[str, str | int]]:
    res: list[dict[str, str | int]] = []
    for char, num in chars.items():
        res.append({"char": char, "num": num})

    res.sort(reverse=True, key=lambda item: item["num"])
    return res
