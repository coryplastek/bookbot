from stats import get_num_words, get_character_stats

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text('books/frankenstein.txt')
    num = get_num_words(text)
    message = f"{num} words found in the document"
    print(message)

    stats = get_character_stats(text)
    print(stats)

main()
