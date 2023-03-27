import os

def print_frequencies(filename):
    alphabet = {}
    file = open(filename)
    text = ''.join([line.lower() for line in file.readlines()])
    cum = 0
    for symbol in text:
        if symbol in alphabet:
            alphabet[symbol] +=1
            cum += 1
        else:
            if symbol.isalpha():
                alphabet[symbol] = 1
                cum += 1
    print(alphabet)
    freq = list(alphabet.values())
    freq.sort(reverse=True)
    alphabet = dict(sorted(alphabet.items(), key = lambda item: item[1], reverse=True))
    for (key, value) in alphabet.items():
        print("%s:%s" % (key, value/cum))
    file.close()

os.chdir('1 задание')
print_frequencies('file.txt')
