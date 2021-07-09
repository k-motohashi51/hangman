import readchar as rc

class controllerClass:

    def __init__(self, wc, icwc):
        self.__inputChar = None     # 入力文字
        self.__usedChar = []        # 既入力文字リスト
        self.__remain = 6           # 残り入力可能回数
        self.__inputCount = 0       # 入力した回数
        self.__isGameClear = False  # ゲームクリアしたかどうか
        self.__wc = wc              # wordクラス
        self.__icwc = icwc       # incorrectWordsクラス
    
    # ゲーム中の表示 
    def disp(self):
        # 合っている文字のみを表示
        print("\n単語：", end = "")
        for i in range(self.__wc.length()):
            if (self.__wc.passed())[i] == True:
                print((self.__wc.word())[i], end = "")
            else:
                print("-", end = "")
        
        # 前回までに使用した文字を表示
        print("\n使用済み文字：", end = "")
        for i in self.__usedChar:
            if i != None:
                print(i, end = " ")
        
        # 残り入力可能回数を表示
        print("\n残り回数:" + str(self.__remain))

    # 推測文字を入力する
    def input(self):
        print("文字を入力してください")
        self.__inputChar = str(rc.readkey())

        if self.__judgeInput() == False:
            self.input()
    
    # 入力文字が条件を満たしているか判定する
    def __judgeInput(self):
        if len(self.__inputChar) > 1:
            print("文字数超過")
            return False
        
        if self.__inputChar < 'a' or 'z' < self.__inputChar:
            print("予期されていない文字")
            return False

        for i in self.__usedChar:
            if i == self.__inputChar:
                print("既に入力されている")
                return False

        return True
    
    # 入力文字が正解単語中の文字と一致しているか判定する
    def judgeInputChar(self):
        return self.__wc.judge(self.__inputChar)
    
    # 各種変数更新をする
    def updateVariables(self, isRight):
        if isRight == False:
            self.__remain -= 1
        
        self.__inputCount += 1
        self.__usedChar.append(self.__inputChar)
 
    # ゲーム終了条件を満たしているか判定する
    def isEnd(self):
        if self.__remain == 0:
            self.__addIncorrectWord(self.__wc.word())
            return True
            
        if all(self.__wc.passed()) == True:
            self.__isGameClear = True
            return True

        return False
    
    # 結果を表示する
    def dispResult(self):
        if self.__isGameClear == True:
            print("正解です\n")
            return
        
        print("残念　正解は" + str(self.__wc.word()))
    
    # ゲーム続行するか入力させて判定する
    def isContinue(self):
        print("ゲームを続けますか(y/n):", end = "")
        if input() == 'y':
            return True
        
        self.__icwc.saveWords()
        return False

    # 間違えた単語を保存する
    def __addIncorrectWord(self, word):
        self.__icwc.addWord(word)
