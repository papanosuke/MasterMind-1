# Master Mind
# 数当てゲーム いわゆる Hit and Blow

# 仕様：
# 答えは3つの数字
# 数字は0から9
# 先頭に0が来ても良い
# 重複はなし
# 入力する文字列も同様．

import random

# 正解の数列を作成
def makeAnswer():
    # 重複なしを達成するため，ランダムシャッフルを行って，先頭3文字を答えにする
    val = [str(i) for i in range(10)]
    random.shuffle(val)
    answer = val[0:3]
    return answer

# ユーザの入力を受け取る．
# 3つの文字列
# 各文字は0から9でなければならない
def getNumber():
    flag = 1
    while(flag):
        flag = 0
        print("input number = ", end='')
        number = list(input())

        # 3文字かチェック
        if len(number)!=3:
            flag = 1

        # 各文字が数字かチェック
        for i in range(len(number)):
            if (number[i]<'0' or '9'<number[i]):
                flag = 1
                break

        # 3つの数字に重複がないかチェック
        for i in range(len(number)):
            for j in range(i+1,len(number)):
                if(number[i]==number[j]):
                    flag = 1
                    break

    return number
    
def check_hit(answer, number):
    ct = 0
    for i in range(3):
        if (number[i]==answer[i]):
            ct += 1
    return ct

def check_blow(answer, number):
    ct = 0
    for i in range(3):
        for j in range(3):
            if (answer[i]==number[j] and i!=j):
                ct += 1
    return ct

if __name__ == '__main__':

    answer = makeAnswer()

    ct = 1
    hit = 0
    while(hit!=3):
        print("Challenge Count: %d" % (ct))

        number = getNumber()
        hit = check_hit(number, answer)
        blow = check_blow(number, answer)
        print("Hit=%d, Blow=%d" % (hit, blow))
        print('')

        if (hit!=3):
            ct += 1

    print("Game Clear!")
    print("Challenge Count=%d" % (ct))
