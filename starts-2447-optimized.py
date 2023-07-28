# baekjoon 2447 - runtime optimized

N = int(input())

arr = [['***' for _ in range(N//3)] for _ in range(N)]

def pattern(row, col, num, flag=True):
    if num < 3:
        if flag==True:
            arr[row+1][col] = '* *'
        else:
            arr[row][col], arr[row+1][col], arr[row+2][col] = '   ', '   ', '   '
    
    else:
        if ((row//3)//(num//3)) % 3 == 1 and (col//(num//3)) % 3 == 1: flag_T = False
        else: flag_T= True
        pattern(row, col, num//3, flag * flag_T)

for i in range(0,N,3):
    for j in range(0,N//3): 
        pattern(i, j, N)

for i in range(0,N):
    for j in range(0,N//3):
        print(arr[i][j], end='')
    print('')

# input = 9
# *** *** ***
# * * * * * * (1,0) (1,1) (1,2)
# *** *** ***
# ***     *** (3,1)
# * *     * * (4,1)
# ***     *** (5,1)
# *** *** ***
# * * * * * *
# *** *** ***

# 우선, '***',  '* *', '   ' 3가지의 패턴으로 분류한 뒤, 해당 패턴이 언제 나타나는 지를 파악해야할 것 같음.

# 너비를 input / 3으로 만들고, 높이는 9 그대로.

# 전부 빈 경우 -> (높이) // (input/3) == 1 && (너비) // (input/9) == 1
# 0'1'2,, 012'345'678
# 한 칸만 빈 경우 -> (높이) % (input/3) == 1 && (너비) // (input/9) != 1
# 꽉 채워진 경우 -> (높이) % (input/3) != 1 && (너비) // (input/9) != 1