from stats import get_num_words, get_character_stats, sort_character_stats

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")

    book_path = 'books/frankenstein.txt'
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
