class wordClass:

    def __init__(self, data):
        self.__word = data
        self.__length = len(self.__word) - 1
        self.__passed = [False] * self.__length
    
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
        
        # 複数正解も含む
        for i in range(self.__length):
            if ch == i:
                self.__passed[i] = True
                is_passed = True
               
        if is_passed == True:
            return True
        
        return False
    
    # 正解している文字のリストを返す
    def passed(self):
        return list(itls.compress(self.__word, self.__passed))
