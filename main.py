def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    return len(text.split())

def main():
    num = get_num_words(get_book_text('books/frankenstein.txt'))
    message = f"{num} words found in the document"
    print(message)

main()
