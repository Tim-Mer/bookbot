from stats import *
import os
import sys


def get_book_text(fpath):
    with open(fpath, 'r') as f:
        return f.read()
    
def main(books_path):
    print("============ BOOKBOT ============")
    book_list = []
    if os.path.isfile(books_path):
        book_list.append(books_path)
    else:
        for book in os.listdir(books_path):
            book_list.append(os.path.join(books_path, book))
            
    for cur_book in book_list:
        print(f"Analysing book found at {cur_book}")
        
        contents = get_book_text(cur_book)
        num_words = get_num_words(contents)    
        chars_num = get_num_chars(contents)
        sorted_list = sort_chars(chars_num)
        
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["count"]}")
        
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)    
main(sys.argv[1])