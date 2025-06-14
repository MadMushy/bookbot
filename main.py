

# file_path = "/home/david/bootdev_projects/bookbot/books/frankenstein.txt"


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():

    file_path = "/home/david/bootdev_projects/bookbot/books/frankenstein.txt"

    book_content = get_book_text(file_path)
    print(book_content)

main()

