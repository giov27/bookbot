
import sys
from stats import count_words, count_characters, formatted_count_character

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read() 
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
    count = count_words(get_book_text(sys.argv[1]))
    print(f"----------- Word Count ----------\nFound {count} total words")

    count_char = count_characters(get_book_text(sys.argv[1]))
    formatted_count_char = formatted_count_character(count_char)
    print(f"--------- Character Count -------")
    for i in formatted_count_char:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    print(f"============= END ===============")




main()