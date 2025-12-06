def get_book_content(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(path):

    content = get_book_content(path)
    contentList = content.split()
    return len(contentList)

def letter_count(path):
    content = get_book_content(path)
    content = content.lower()
    letters = {}
    for word in content:
        letters[word] = letters.get(word,0) +1
    return letters