def count(content):
    words = content.split()
    letter_count = {}
    for letter in content:
        # for l in list(letter.lower()):
        l = letter.lower()
        if not l.isalpha():
            continue
        try:
            letter_count[l] += 1
        except:
            letter_count[l] = 1
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document \n")

    for key in dict(sorted(letter_count.items())):
        print(f"The {key} character was found {letter_count[key]} times")
    
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count(file_contents)

main()
