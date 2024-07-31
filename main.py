from curses.ascii import isalpha
from traceback import format_exception_only


def main():
    filename = 'books/frankenstein.txt'
    book_content = get_book_content(filename)
    # print("Word count:", count_words(book_content))
    # print("Unique caracters:", count_words(book_content))
    print("\n".join(make_report(filename, count_words(book_content), count_unique_characters(book_content))))

def get_book_content(filename: str) -> str:
    with open(filename, 'r') as f:
        contents = f.read()
        return contents

def count_words(s: str) -> int:
    return len(s.split())

def count_unique_characters(s: str) -> dict[str, int]:
    clean_str = s.lower()
    count = {}

    for char in clean_str:
        count[char] = count.get(char, 0) + 1
    return count

def make_report(filename:str, word_count: int, char_count: dict[str, int]) -> list:
    report = []
    header = "--- Begin report of {filename} ---"
    footer = "--- End report ---"

    report.append(header)
    for k, v in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
        if k.isalpha():
            line = f"The '{k}' character was found {v} times"
            report.append(line)
    report.append(footer)

    return report


main()
