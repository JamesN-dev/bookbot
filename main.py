from stats import get_count_dict, count_words, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]


def get_book_text(path: str):
    with open(path) as file:
        return file.read()


def main() -> None:
    book_text = get_book_text(path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    count_dict = get_count_dict(book_text)
    sorted_char_list = sort_dict(count_dict)
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()
