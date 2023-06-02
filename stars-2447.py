# baekjoon 2447
# 이번 문제는 잘 모르겠습니다. 많이 배워야 할 것 같네요.

N = int(input())


def pattern(x, flag):
    if x==1:
        if flag==True: print(" ", end='')
        else: print("*", end='')
    else:
        for i in range(9):
            if i==4: pattern(x//3, flag or True)
            else: pattern(x//3, flag or False)

pattern(3**N, False)