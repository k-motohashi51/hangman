from pkg import wordClass
from pkg import controllerClass

import random as rand

def main():

    # ゲーム自体の繰り返し
    while 1:

        data = getWord()

        print(data) # 完成版は消す

        word = wordClass.wordClass(data)
        controller = controllerClass.controllerClass(word)

        # ゲーム中の繰り返し
        while 1:
            print("正解", end = '')     # 完成版は消す
            print(data)                 # 完成版は消す
            
            # 表示
            controller.disp()
            
            # 文字の入力
            controller.input()

            # 文字の判定
            a = controller.judgeInputChar()

            # 設定の更新
            controller.updateVariables(a);
            
            # 終了判定
            if controller.isEnd() == True:
                controller.dispResult()
                break
        
        if controller.isContinue() == False:
            del word
            del controller
            break


# 出題単語の取得
def getWord():

    while(1):
        print("~~~モード選択~~~")
        print("通常の出題\t(1)")
        print("弱点克服モード(2)\n>")

        playMode = input()

        if int(playMode) == 1:
            print("単語帳ファイル名>", end = "")
            file = input()
            break
        
        elif playMode == 2:
            print("弱点克服モードです")
            file = 'weak.txt'
            break

        else:
            print("予期しない入力")
        
    with open(file, 'r') as f:
        lines = f.readlines()
        data = rand.choice(lines)

    return data


if __name__ == "__main__":
    main()
