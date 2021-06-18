import itertools as itls
import random as rand

class Word:
    def __init__(self, word):
        self.__word = word
        self.__length = len(self.__word)
        self.__passed = [0] * self.__length
    
    def word(self):
        return self.__word
    
    # 単語の任意の要素を返す
    def index(self, index):
        return self.__word[index]
    
    # 単語の長さを返す
    def length(self):
        return self.__length
    
    # 入力文字が単語に含まれているか判定する
    def judge(self, ch):
        is_passed = 0

        for i in self.__word:
            if ch == i:
                self.__passed[i] = true
                is_passed = true
               
        if is_passed == true:
            return true
        
        return false
    
    # 正解している文字のリストを返す
    def passed(self, index):
        return list(itls.compress(self.__word, self.__passed))
#----------------------------------------------------------------

class Controller:
    def __init__(self):
        self.remain = 6
        self.inputCount = 0
        self.isGameClear = false
        self.isContinue = false
        self.usedChar[]

    #def disp()


while True:
    # 出題単語の取得
    with open('words', 'r') as f:
        lines = f.readlines()
        data = rand.choice(lines)
    
    word = Word(data)

    while(#残り回数が0でない&&ゲームクリアしてない
            ):
        #disp





















