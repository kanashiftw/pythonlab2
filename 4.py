import re
#Вариант 9
def find_post(file):
    text = [string.strip() for string in open(file, 'r', encoding='utf-8').readlines()]
    pattern = re.compile('83\d{3}, \w{3,}')
    dates = {}
    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка " + str(index + 1) + ", позиция " + str(match.start())] = " : найдено '" + match.group() + "'"
    for key in dates.keys():
        print(key + dates[key])
