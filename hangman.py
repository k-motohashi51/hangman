import wordClass
import controllerClass

import itertools as itls
import random as rand
import pandas as pd

def main():

    # ゲーム自体の繰り返し
    while 1:

        # ゲーム中の繰り返し
        while 1:

            # 出題単語の取得
            with open('words', 'r') as f:
                lines = f.readlines()
                data = rand.choice(lines)

            word = wordClass(data)
            controller = controllerClass(word)
            
            # 文字の入力
            controller.inputChar()
            
            # 設定の更新
            controller.updateVariables();
            
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
