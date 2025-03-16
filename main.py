import sys

from stats import count_words

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    reference = generate_report_reference(char_count)
    print_report(reference, word_count, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    lowered = text.lower()
    chars = {}
    for c in lowered:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def generate_report_reference(char_dict):
    char_ref = []
    for d in char_dict:
        if d.isalpha():
            char_ref.append({"char": d, "num": char_dict[d]})
    char_ref.sort(reverse=True, key=sort_on)
    return char_ref


def sort_on(dict):
    return dict["num"]


def print_report(chars, count, path):
    name = path[6:-4].title()
    print(f"--- Begin report of {name} ---")
    print(f"{count} words found in the document")
    print("")
    for c in chars:
        print(f"{c["char"]}: {c["num"]}")
    print("--- End report ---")

if __name__ == "__main__":
    main()
