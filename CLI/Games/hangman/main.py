import os
import sys
from random import choice


class Hangman:

    miss = 0
    win = False
    wordlist = []
    wordspace = []
    checkwordspace = []

    """SHOWS THE CURRENT STAGE OF THE GAME"""
    def generateStates(self):
        if self.miss == 0:
            print("")
            print("")
            print("")
            print("")
        if self.miss == 1:
            print("0")
            print("")
            print("")
            print("")
        if self.miss == 2:
            print("0")
            print("-")
            print("")
            print("")
        if self.miss == 3:
            print(" 0")
            print("/-")
            print("")
            print("")
        if self.miss == 4:
            print(" 0")
            print("/-\\")
            print("")
            print("")
        if self.miss == 5:
            print(" 0")
            print("/-\\")
            print(" |")
            print("")
        if self.miss == 6:
            print(" 0")
            print("/-\\")
            print(" |")
            print("/")
        if self.miss == 7:
            print(" 0")
            print("/-\\")
            print(" |")
            print("/ \\")

    def selectPseudoRandomWord(self):
        wordslistList = []
        wordslistPath = os.path.abspath('corncob_lowercase.txt')
        with open(wordslistPath, 'r') as wordslist:
            for i in wordslist:
                wordslistList.append(i.replace('\n', ""))
        selectedWord = choice(wordslistList)
        wordslist.close()
        return selectedWord

    """GAME LOOP"""
    def loop(self):
        while True:
            for i in self.wordspace:
                if self.wordspace == self.wordlist:
                    print("YOU WIN")
                    sys.exit()
            self.generateStates()
            prompt = str(input("Guess a letter in the word.")).lower()
            indexes = []
            if len(prompt) > 1:
                print("You have entered more than one letter.")
                return self.loop()
            else:
                """GUESSING CORRECTLY"""
                if prompt in self.wordlist:
                    for i in range(len(self.wordlist)):
                        if prompt == self.wordlist[i]:
                            indexes.append(i)
                        for i in indexes:
                            self.wordspace[i] = prompt
                else:
                    self.miss += 1
                    """LOSS CONDITION"""
                    if self.miss == 7:
                        break
            self.generateStates()
            # FOR DEBUG
            print(hangman.wordspace)
            print(hangman.wordlist)

    def play(self):
        selectedWord = self.selectPseudoRandomWord()
        print(selectedWord)
        for i in selectedWord:
            self.wordlist.append(i)
        for i in range(len(self.wordlist)):
            self.wordspace.append(i)
        self.loop()


# CREATE INSTANCE OF HANGMAN
hangman = Hangman()
hangman.play()