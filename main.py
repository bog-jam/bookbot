def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters = character_count(text)
    sorted_report = sort_report(num_letters)
    print(f"Begin report of {book_path}")
    print(f"{num_words} words found in document")
    for char, count in sorted_report:
        print(f"The '{char}' character was found '{count}' times")
    print("---End report---")


def count_words(text):
    wordsplit = text.split()
    wordcount = len(wordsplit)

    return wordcount

def character_count(text):
    letter_count = {}
    lower_case_text = text.lower()
  
    for i in lower_case_text:
        if i.isalpha() == False:
            pass        
        elif i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1

    return letter_count

def sort_on(num_letters):
    return num_letters[1]

def sort_report(num_letters):
    sorted_dict = sorted(num_letters.items(), key=sort_on, reverse=True)
      
    return sorted_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()