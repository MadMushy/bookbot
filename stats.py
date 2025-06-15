def count_words(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count


def char_counts(file_contents):
    char_count = {}
    char_lower = file_contents.lower()
    for char in char_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(char_list_dict):
    return char_list_dict["num"]
