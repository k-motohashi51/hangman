class controllerClass:

    def __init__(self, word):
        self.remain = 6             # 残り入力可能回数
        self.inputCount = 0         # 入力した回数
        self.isGameClear = False    # ゲームクリアしたかどうか
        self.usedChar = []          # 既入力文字リスト
        word = word                 # wordクラス
    
    # ゲーム中の表示 
    def disp(self):
        print("単語：" + str(word.passed()))
        
        print("使用済み文字：", end = "")
        for i in self.usedChar:
            if i != None:
                print(i)
        print("\n")

        print("残り回数:", end = "")
        print(self.remain)

    # 推測文字を入力する
    def inputChar(self):
        print("文字を入力してください:", end = "")
        self.__inputChar = input()

        print(self.__inputChar)
        #judgeInput()
    
    # 入力文字が条件を満たしているか判定する
    #def judgeInput():
    
    # 入力文字が正解/不正解のときの各種変数更新する
    def updateVariables(self):
        if word.judge(self.__inputWord) == False:
            remain -= 1
        
        inputCount += 1
        self.usedChar.append(self.__inputWord)
 
    def isEnd(self):
        #TODO 終了判定

        return True

    def dispResult(self):
        #TODO 結果表示

        print("正解です")

    def isContinue(self):
        print("ゲームを続けますか(y/n):", end = "")
        if input() == 'y':
            return True

        return False
