import sys
sys.path.append("../pkg")

import wordClass as wc
import controllerClass as cc
import incorrectWordsClass as icwc

import random as rand

def main():

    icWords = icwc.incorrectWordsClass()

    # ゲーム自体の繰り返し
    while 1:
        fileName = selectMode()

        # 出題単語の取得
        data = getWord(fileName)

        word = wc.wordClass(data)
        controller = cc.controllerClass(word, icWords)

        # ゲーム中の繰り返し
        while 1:
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


# モード選択する
def selectMode():

    while 1:
        print("~~~モード選択~~~")
        print("通常の出題\t(1)")
        print("弱点克服モード(2)\n>", end = "")
    
        playMode = int(input())
    
        if playMode == 1:
            print("単語帳ファイル名>", end = "")
            fileName = input()
            break
        
        elif playMode == 2:
            print("弱点補強モード")
            fileName = 'weak.txt'
            break
        
        else:
            print("予期しない入力")
    
    return fileName


# 出題単語の取得
def getWord(file):
    
    with open(file, 'r') as f:
        lines = f.readlines()
        data = rand.choice(lines)

    return data


if __name__ == "__main__":
    main()
