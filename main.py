def main():
    book_path = "./books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    print(count_words(file_contents))


def count_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
