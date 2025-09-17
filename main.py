import sys
from stats import count_words
from stats import count_char
from stats import sort_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = f"{sys.argv[1]}"
    text = get_book_text(book)
    word_count = count_words(text)
    char_count = count_char(text)
    sorted_chars = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
            continue
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


main()