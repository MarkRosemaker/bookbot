import sys

from stats import count_characters, count_words, sort_characters


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def write_report(path: str):
    txt = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = count_words(txt)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = sort_characters(count_characters(txt))
    for cc in char_count:
        print(f"{cc['char']}: {cc['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    write_report(path)


main()
