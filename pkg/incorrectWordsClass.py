import os

class incorrectWordsClass:

    def __init__(self):
        self.__incorrectWord = []  # 間違えた単語リスト
        self.__path = '../src/weak.txt'

    def addWord(self, word):
        self.__incorrectWord.append(word)

    def saveWords(self):
        with open(self.__path, 'a') as f:
            f.writelines(self.__incorrectWord)
