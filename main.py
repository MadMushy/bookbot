from stats import count_words, char_counts, sort_on
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():

    file_path = sys.argv[1]

    book_content = get_book_text(file_path)

    book_word_count = count_words(book_content)

    book_char_count = char_counts(book_content)

    char_list_dict = []
    for char, num in book_char_count.items():
        char_small_dict = {"char": char, "num": num}
        char_list_dict.append(char_small_dict)

    char_list_dict.sort(reverse=True, key=sort_on)
    
    filtered = []
    for char in char_list_dict:
        if char['char'].isalpha() and char['char'].isascii():
            filtered.append(char)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for item in filtered:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

