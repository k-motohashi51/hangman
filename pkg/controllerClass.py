class controllerClass:

    def __init__(self, wc):
        self.__remain = 6             # 残り入力可能回数
        self.__inputCount = 0         # 入力した回数
        self.__isGameClear = False    # ゲームクリアしたかどうか
        self.__usedChar = []          # 既入力文字リスト
        self.__wc = wc                 # wordクラス
    
    # ゲーム中の表示 
    def disp(self):
        print("単語：" + str(word.passed()))
        
        print("使用済み文字：", end = "")
        for i in self.__usedChar:
            if i != None:
                print(i)
        print("\n")

        print("残り回数:", end = "")
        print(self.__remain)

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
        if self.__wc.judge(self.__inputChar) == False:
            self.__remain -= 1
        
        self.__inputCount += 1
        self.__usedChar.append(self.__inputChar)
 
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
