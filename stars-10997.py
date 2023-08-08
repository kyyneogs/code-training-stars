# *********     <- input : 3
# *             1 -> 5 -> 9 (4씩 추가.)
# * *******
# * *     *
# * * *** *
# * * * * *
# * * * * *
# * *   * *
# * ***** *
# *       *
# *********

N = int(input())
N = 1 + (N-1)*4
arr = [[' ' for _ in range(N)] for _ in range((N+2) if N>1 else 1)]

def draw(x, y, max_x, max_y, flag_x=1, flag_y=0, sign=1, cnt=0):
    if max_x>0:
        arr[x][y] = '*'

        if (cnt+1)*flag_x==max_x+1 or (cnt+1)*flag_y==max_y+1:
            if (cnt+1)*flag_y==max_y+1: sign = sign * -1
            max_x, max_y = max_x - 2*flag_x, max_y - 2*flag_y
            flag_x, flag_y = flag_y, flag_x
            cnt=0

        x, y, cnt = x + flag_x*sign, y + flag_y*sign, cnt+1
        draw(x, y, max_x, max_y, flag_x, flag_y, sign, cnt)
        return
    else:
        return

for i in range(N):
    arr[0][i] = '*'

if N-1!= 0 : draw(x=0, y=0, max_x=N+1, max_y=N-1)

for i, j in enumerate(arr):
    if i != 1:
        print(''.join(j))
    else:
        print('*')

# N = int(input())
# N = 1 + (N-1)*4
# arr = [[' ' for _ in range(N)] for _ in range((N+2) if N>1 else 1)]

# for i in range(N):
#     arr[0][i] = '*'

# x, y, max_x, max_y = 0, 0, N+1, N-1
# flag_x, flag_y, sign = 1, 0, 1
# cnt = 0

# while max_x>0 and N-1!=0:
#     arr[x][y] = '*'

#     if (cnt+1)*flag_x==max_x+1 or (cnt+1)*flag_y==max_y+1:
#         if (cnt+1)*flag_y==max_y+1: sign = sign * -1
#         max_x, max_y = max_x - 2*flag_x, max_y - 2*flag_y
#         flag_x, flag_y = flag_y, flag_x
#         cnt=0

#     x, y, cnt = x + flag_x*sign, y + flag_y*sign, cnt+1

# for i, j in enumerate(arr):
#     if i != 1:
#         print(''.join(j))
#     else:
#         print('*')