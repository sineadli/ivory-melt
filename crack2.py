f = open("dictionary.txt", "r")
words = f.readlines()

password = input()

def decrypt(password, word):
    if password + "\n" == word:
        return 1
    else:
        return 0

for word in words:
    if decrypt(password, word) == 1:
        print(password)
        break
