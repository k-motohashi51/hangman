#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define LIMIT 6
#define BUF 100
  
typedef struct wrongList_t {
  char    *wrongWord;         // 不正解単語
  int     wrongWordSize;      // 不正解単語の文字数
  struct  wrongList_t *next;  // 次の不正解単語が属する構造体へのポインタ
} wrongList_t;

int   wordCount(char *);
void  wordDeterm(char *, int, char *);
int   wordSizeCalc(char *);
int   *initialize(char *, int, int *, int *, int *, int *, wrongList_t *, int *);
void  disp(char *, int, int *, char *, int, int);
void  input(char *, int *);
int   judge(char, char *, int, int *);
int   result(int *, int);
int   resultDisp(int, int, char *, wrongList_t *, int, int);
void  wrongListDisp(wrongList_t *);
void  makeWeak(wrongList_t *);
wrongList_t *wrongListAdd(wrongList_t *, char *, int);

int main(int argc, char *argv[]) {
  int   wordsNum;           // 単語帳の単語数
  char  rightWord[BUF];     // 正解単語
  int   rightWordSize;      // 正解単語の文字数
  char  usedChar[BUF];      // 使用した文字を順に格納
  int   *isRight;           // 単語内で正解した文字の位置を1にする
  int   isGameClear;        // ゲームクリアしたかどうか
  int   isContinue;         // ゲームコンティニューするかどうか
  int   remain;             // 残りの文字を打てる回数
  int   inputCount;         // 入力した回数(重複除く)
  int   isCorrectAns;       // 入力文字が正解単語に含まれているか
  int   rightNum = 0;       // 正解の回数
  int   wrongNum = 0;       // 不正解の回数
  wrongList_t *head = NULL; // 不正解単語のリスト
  
  if(strcmp(argv[1], "weak.txt") == 0) {
    printf("苦手克服モードです\n");
  }

  /* 単語帳の単語数の取得 */
  wordsNum = wordCount(argv[1]);
  
  do {
    /* 正解単語の決定 */
    wordDeterm(argv[1], wordsNum, rightWord);

    /* 正解単語の文字数を取得 */
    rightWordSize = wordSizeCalc(rightWord);

    /* 初期化 */
    isRight = initialize(usedChar, rightWordSize, &isGameClear, &isContinue, &remain, &isCorrectAns, head, &inputCount);
    
    while(remain != 0 && isGameClear == 0) {
      /* 表示 */
      disp(rightWord, rightWordSize, isRight, usedChar, remain, inputCount);
  
      /* 文字入力 */
      input(usedChar, &inputCount);

      /* 入力文字の判定 */
      isCorrectAns = judge(usedChar[inputCount - 1], rightWord, rightWordSize, isRight);

      /* 入力文字が正解でない場合 */
      if(isCorrectAns == 0) {
        remain -= 1;
      }
      
      /* ゲームクリアしたか判定 */
      isGameClear = result(isRight, rightWordSize); 

      /* ゲームクリア時の表示 */
      if(isGameClear == 1 || remain == 0) {
        if(remain == 0) {
          head = wrongListAdd(head, rightWord, rightWordSize);
          wrongNum++;
        } else {
          rightNum++;
        }
        isContinue = resultDisp(isGameClear, remain, rightWord, head, rightNum, wrongNum);
      }
    }

    /* メモリ解放 */
    free(isRight);
  } while(isContinue == 1);
    
  return 0;
}

/* 単語帳から単語数を求めて、戻り値として返す */
int wordCount(char fileName[]) {
  FILE  *fp;          // 単語帳のファイルポインタ
  int   wordsNum = 0; // 単語数
  char  buf[BUF];      // 長い単語対策

  fp = fopen(fileName, "r");
  if(fp == NULL) {
    printf("ファイル読込失敗\n");
    exit(1);
  }
  
  /* 行数から単語の数を取得 */
  while(fscanf(fp, "%s", buf) != EOF) {
    wordsNum++;
  }
  
  fclose(fp);

  return wordsNum;
}

/* 単語帳の中から出題する単語を決定する */
void wordDeterm(char fileName[], int wordsNum, char rightWord[]) {
  FILE  *fp;        // 単語帳のファイルポインタ
  int   wordLocate; // 単語帳内の正解単語の要素数
  
  /* 出題する単語の要素数決定 */
  srand((unsigned)time(NULL));
  wordLocate = rand() % wordsNum + 1;

  fp = fopen(fileName, "r");
  if(fp == NULL) {
    printf("ファイルを読み込めませんでした\n");
    exit(1);
  }
  
  /* 目的の単語の要素数分単語を取得する*/
  for(int i = 1; i <= wordLocate; i++) {
    fscanf(fp, "%s", rightWord);
  }
  
  fclose(fp);
}

/* 出題単語の文字数を求めて、戻り値として返す */
int wordSizeCalc(char rightWord[]) {
  int wordSize = 0; // 単語帳の単語数
  
  /* 単語を一文字ずつ調べる */
  while(rightWord[wordSize] != '\0') {
    wordSize++;
  }

  return wordSize;
}

/* 変数の初期化 */
int *initialize(char usedChar[], int rightWordSize, int *isGameClear, int *isContinue, int *remain, int *isCorrectAns, wrongList_t *head, int *inputCount) {
  int *isRight;
  
  /* 出題単語の文字数分メモリを確保 */
  isRight = (int *)malloc(sizeof(int) * rightWordSize);

  for(int i = 0; i < BUF; i++) {
    usedChar[i] = 0;
  }
  for(int i = 0; i < rightWordSize; i++) {
    isRight[i] = 0;
  }
  *isGameClear = 0;
  *isContinue = 0;
  *remain = LIMIT;
  *isCorrectAns = 0;
  *inputCount = 0;
  head = NULL;

  return isRight;
}

/* ゲーム中の表示 */
void disp(char rightWord[], int rightWordSize, int isRight[], char usedChar[], int remain, int inputCount) {
  /* 正解している文字だけ表示(例：ma-hema-i-s) */
  printf("\n単語：");
  for(int i = 0; i < rightWordSize; i++) {
    if(isRight[i] == 1) {
      printf("%c", rightWord[i]);
    } else {
      printf("-");
    }
  }
  
  /* 既に使われた文字を列挙 */
  printf("使われた文字：");
  for(int i = 0; i <= inputCount; i++) {
    if(usedChar[i] != '0')
    printf("%c", usedChar[i]);
  }
  printf("\n");

  /* 残り入力可能回数を表示 */
  printf("残り回数：%d\n", remain);
}

/* プレイヤーからの入力 */
void input(char usedChar[], int *inputCount) {
  char s[3] = {0};  // 入力文字列
  char code;        // 入力が成功：0、失敗：1~3

  printf("文字を入力してください\t：");
  
  /* 入力成功するまで入力させる */
  do {
    code = 0;
    scanf("%2s%*[^\n]", s);
    getchar();
    if(s[1] != 0) {
      code = 1;
    } else {
      if(('a' <= s[0] && s[0] <= 'z') || ('A' <= s[0] && s[0] <= 'Z')) {
        for(int i = 0; i < *inputCount; i++) {
          if(s[0] == usedChar[i]) {
            code = 2;
          }
        }
      } else {
        code = 3;
      }
    }
    switch(code) {
      case 1:   printf("入力文字が多すぎます\t：");   break;
      case 2:   printf("既に使われています\t：");     break;
      case 3:   printf("予期されていない文字です："); break;
      default:  break;
    }
  } while(code != 0);
  
  /* 余分にとった入力文字列の一文字目を適用 */
  usedChar[*inputCount] = s[0];

  *inputCount += 1;
}

/* 入力文字が出題単語に含まれているか調査する */
int judge(char inputChar, char rightWord[], int rightWordSize, int isRight[]) {
  int   flag = 0;
  char  inputTrim;
  char  rightTrim;
  
  /* 入力文字が正解に含まれているか */
  for(int i = 0; i < rightWordSize; i++) {
    /* 大文字を小文字として比較 */
    if('A' <= rightWord[i] || rightWord[i] <= 'Z') {
      rightTrim = rightWord[i] + 32;
    } else {
      rightTrim = rightWord[i];
    } 
    if('A' <= inputChar || inputChar <= 'Z'){
      inputTrim = inputChar + 32;
    } else {
      inputTrim = inputChar;
    }

    /* 正解に含まれている場合 */
    if(inputTrim == rightTrim) {
      isRight[i] = 1;
      flag = 1;
    }
  }
  
  return flag;
}

/* ゲーム終了条件を満たしているか調べる */
int result(int isRight[], int rightWordSize) {
  int flag = 1;
  
  /* 一つでも文字が違っていればflag=0 */
  for(int i = 0; i < rightWordSize; i++) {
    if(isRight[i] != 1) {
      flag = 0;
      break;
    }
  }
  
  /* すべて正解の単語と一致しているならば1が返る */
  return flag;
}

/* 結果表示 */
int resultDisp(int isGameClear, int remain, char rightWord[], wrongList_t *head, int rightNum, int wrongNum) {
  char  str[3] = {0}; // 入力
  int   isContinue;   // ゲームを続けるかどうか
  float rightRate;    // 正解率

  if(isGameClear == 1) {
    printf("\n\n正解です %s\n", rightWord);
  }
  if(remain == 0) {
    printf("\n\n残念　正解は%sでした\n", rightWord);
  }
  
  /* ゲームを終わるかどうか */
  printf("続けますか(y/n)?");
  scanf("%2s%*[^\n]", str);
  getchar();
  if(str[1] == 0 && str[0] == 'y') {
    isContinue = 1;
  } else {
    wrongListDisp(head);
    isContinue = 0;
  }
  
  /* ゲームを終わる場合 */
  if(isContinue == 0) {
    rightRate = (float)rightNum / (float)(rightNum + wrongNum);
    printf("正解数\t：%d\n", rightNum);
    printf("不正解数：%d\n", wrongNum);
    printf("正解率\t：%f\n", rightRate);
    printf("またね\n");

    /* 苦手克服用のファイルを作成 */
    makeWeak(head);
  }

  return isContinue;
}

/* 弱点克服モード用の単語をリストアップ */
wrongList_t *wrongListAdd(wrongList_t *head, char wrongWord[], int wrongWordSize) {
  wrongList_t *tail;
  
  /* 間違えた単語のデータを格納 */
  tail = (wrongList_t *)malloc(sizeof(wrongList_t));
  tail->wrongWordSize = wrongWordSize;
  tail->wrongWord = (char *)malloc(sizeof(char) * wrongWordSize);
  for(int i = 0; i < wrongWordSize; i++) {
    tail->wrongWord[i] = wrongWord[i];
  }

  /* 次の構造体へのポインタはNULL（最後なので） */
  tail->next = NULL;
  
  /* リストに構造体をつけていく */
  if(head == NULL) {
    return tail;
  } else {
    wrongList_t *finder = head;
    while(finder->next != NULL) {
      finder = finder->next;
    }
    finder->next = tail;
    return head;
  }
}

/* 間違えた単語を表示する */
void wrongListDisp(wrongList_t *head) {
  if(head == NULL) {
    printf("間違えた単語はありません！！\n");
  } else {
    printf("間違えた単語一覧：[");
    wrongList_t *finder = head;

    /* 間違えた単語が属する構造体へのポインタがなくなるまで */
    while(finder->next != NULL) {
      printf("%s, ", finder->wrongWord);
      finder = finder->next;
    }

    printf("%s]\n", finder->wrongWord);
  }
}

/* 弱点克服モード用のファイルを作成 */
void makeWeak(wrongList_t *head) {
  FILE *fp;  // 苦手克服モードの単語帳のファイルポインタ

  fp = fopen("weak.txt", "w");

  /* 弱点克服モード用のファイルに書き込み */
  if(head != NULL) {
    wrongList_t *finder = head;
    while(finder->next != NULL) {
      fprintf(fp, "%s\n", finder->wrongWord);
      finder = finder->next;
    }
    fprintf(fp, "%s\n", finder->wrongWord);
  }

  fclose(fp);
}
