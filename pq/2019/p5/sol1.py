def print_word(file):
    file = open(file, "r")
    for line in file:
        for word in line.split():
            print(word)
    file.close()


print_word("myTxt.txt")
