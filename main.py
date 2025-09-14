from stats import get_word_count, get_char_count, get_report
import sys

def get_books_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    contents = get_books_text(file_path)
    num_words = get_word_count(contents)
    num_char = get_char_count(contents)
    report = get_report(num_char)

    print("============ BOOKBOT ============")
    print(F"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for d in report:
        print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")

main()

