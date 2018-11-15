import random
import string

words = ["sweltering", "detailed", "literate", "toothpaste", "giraffe", "electric", "fanatic", "scattered", "disastrous", "abashed", "thirsty", "dashing", "simplistic", "trousers", "alluring", "abnormal", "agreement", "agenda", "obsolete", "wrathful", "omniscient", "acoustic"] 
word = list(words[random.randrange(0, len(words), 1)])

letters = list(string.ascii_letters)

word = list("nevertheless")

blank_word = []
health = 6

for i in range(len(word)):
    blank_word.append("_ ")

print("\nHealth: " + str(health) + "\n") 
print("".join(blank_word))

while True:
    # flags for iteration
    health_flag = False
    valid_flag = False
    win_flag = True
    # did you win?
    for item in blank_word:
        if item == "_ ":
            win_flag = False
    if win_flag == True:
        print("\nYou won!")
        break
    # is the input valid (i.e. a letter?)
    while valid_flag == False:
        letter_chosen = input("\nLetter: ")
        for letter in letters:
            if letter_chosen == letter:
                valid_flag = True    
    for i in range(len(word)):
        # change blank_word
        if letter_chosen == word[i]:
            blank_word[i] = word[i] + " "
            # you didn't lose health
            health_flag = True
    # change health
    if health_flag == False:
        health = health - 1
    print("\nHealth: " + str(health) + "\n")
    # did you lose?
    if health == 0:
        print("You lose!")
        break
    # show blank_word
    print("".join(blank_word))
