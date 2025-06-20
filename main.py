from stats import get_num_words, get_character_stats, sort_character_stats
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    
    print("---------- Word Count -----------")
    num = get_num_words(text)
    print(f"Found {num} total words")

    print("--------- Character Count -------")
    stats = sort_character_stats(get_character_stats(text))
    for d in stats:
        if(d["char"].isalpha()):
            print(f"{d['char']}: {d['num']}")

main()
