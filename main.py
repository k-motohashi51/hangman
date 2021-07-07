from pkg import wordClass
from pkg import controllerClass

import random as rand

def main():

    # ゲーム自体の繰り返し
    while 1:

        # 出題単語の取得
        with open('words', 'r') as f:
            lines = f.readlines()
            data = rand.choice(lines)

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


if __name__ == "__main__":
    main()
