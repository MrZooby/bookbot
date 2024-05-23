def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    letter_count = count_letters(text)
    print(letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(words):
    split_words = words.split()
    return len(split_words)

def count_letters(text):
    totals = {}
    lowered_text = text.lower()
    letters = lowered_text.replace(' ','')
 #   letters = sorted(letters)
    for letter in letters:
        number = letters.count(letter)
        totals.update({letter:number})
    return totals

main()