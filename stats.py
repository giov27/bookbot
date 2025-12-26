def count_words(text):
    return len(text.split())   

def sort_on(items):
    return items["num"]

def count_characters(text):

    count_char = {}
    lower_text = text.lower()
    for i in lower_text:
        if i in count_char:
            count_char[i] += 1
        else:
            count_char[i] = 1

    return count_char

def formatted_count_character(count_char):
    arr_char = []
    for i in count_char:
        arr_char.append({"char": i, "num": count_char[i]})
    arr_char.sort(reverse=True, key=sort_on)
    return arr_char