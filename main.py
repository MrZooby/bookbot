def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    letter_count = count_letters(text)
    list_dict = list(letter_count.items())
    list_dict.sort(reverse=True, key=sort_dict)

    print(f"{word_count} words found in the document")
    print()

    for key in list_dict:
        if key[0].isalpha() == True:
            print(f"The '{key[0]}' character was found {key[1]} times")

    print('--- End report ---')

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
    for letter in letters:
        number = letters.count(letter)
        totals.update({letter:number})
    return totals

def sort_dict(dict):
    return dict[1]

main()