from stats import word_count, letter_count
import sys

def sort_on(items):
    return items[1]

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    count = word_count(path)
    letter_count_dir = letter_count(path)
    letter_count_dir.pop(' ')
    letter_count_ls = list(letter_count_dir.items())
    letter_count_ls.sort(reverse=True,key=sort_on)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for word,counts in letter_count_ls:
        print(f"{word}: {counts}")
    print("============= END ===============")

main()
