# baekjoon 2447
# 핵심은 입력받을때마다 3으로 나눠가면서 검사를 진행하는 것?

N = int(input())

arr = [['*']*N for _ in range(N)]

def pattern(x, y, num):
    if (x//num)%3==1 and (y//num)%3==1:
        arr[x][y]=' '
    else:
        if num > 2: pattern(x, y, num/3)


for i in range(N):
    for j in range(N): pattern(i, j, N)

print('\n'.join(arr(N)))

# def pattern(x, flag):
#     if x==1:
#         if flag==True: print(" ", end='')
#         else: print("*", end='')
#     else:
#         for i in range(9):
#             if i==4: pattern(x//3, flag or True)
#             else: pattern(x//3, flag or False)

# pattern(3**N, False)

# input = 9
# *********
# * ** ** * (1,1) (4,1) (7,1)
# *********
# ***   *** (3,3) (3,4) (3,5)
# * *   * * (4,3) (4,4) (4,5)
# ***   *** (5,3) (5,4) (5,5)
# *********
# * ** ** *
# *********