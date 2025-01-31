def main():
    book_path = "./books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    print(char_count)


def count_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    lowered = text.lower()
    counter = {}
    for c in lowered:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter


main()
