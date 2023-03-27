import re

def find_nicks(text):
    pattern = re.compile(r"[A-Z][A-Za-z]*(\d{2}|\d{4})\b")
    for found in pattern.finditer(text):
        match = found.group()
        if (str.isdigit(match[-1])):
            print(match)
        else:
            print(match[:-1])


find_nicks(input("Введите текст: ")
