def drawing(n_error):
    if n_error == 1:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")

    elif n_error == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif n_error == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif n_error == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif n_error == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif n_error == 6:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    elif n_error:  # you lost graphic
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("YOU LOST!")
    else:
        print("       0      ")
        print("     ~~|~~    ")
        print("      / \     ")
        print("YOU WON!")


def guessed_letters(letter, word, blanks):
    for i in range(len(word)):
        if word[i]==letter:
            blanks = blanks[:i] + word[i] + blanks[i + 1:]
    return blanks


def hangman():
    word=str(input("Your word: "))
    errors=0
    guessed=0
    blanks = '_' * len(word)
    while errors!=7:
        if guessed==len(word):
            drawing(0)
            break
        letter=input("Give me a letter: ")
        if letter in word:
            print("Good guess!")
            guessed += 1
            blanks = guessed_letters(letter, word, blanks)
            print(blanks)
        else:
            errors+=1
            print("Wrong!")
            drawing(errors)


if __name__ == "__main__":
    hangman()
    print("END!")