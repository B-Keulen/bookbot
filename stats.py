def get_word_count(file_contents):
       word_count = len(file_contents.split())
       return word_count

def get_char_count(file_contents):
    char_count = {}

    contents = file_contents.lower()
    for char in contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def get_report(chars):
    report = []

    for char, count in chars.items():
        if char.isalpha():
            report.append({"char": char, "num": count})
    report.sort(reverse=True, key=sort_on)
    return report


