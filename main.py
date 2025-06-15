from stats import count_words, char_counts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents 

def main():

    file_path = "/home/david/bootdev_projects/bookbot/books/frankenstein.txt"

    book_content = get_book_text(file_path)

    book_word_count = count_words(book_content)

    book_char_count = char_counts(book_content) #try putting in here instead

    print(f"{book_word_count} words found in the document")

    print(f"{book_char_count}")


main()

