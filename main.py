def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(words):
    split_words = words.split()
    return len(split_words)

main()