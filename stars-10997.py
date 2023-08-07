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
N = 1 + (N+1)*2
arr = [[' ' for _ in range(N)] for _ in range(N)]

def draw(x, y, max_x, max_y, flag_x=1, flag_y=0, flag_pm=1, cnt=1):
    if max_x==0 or max_y==0:
        return
    
    arr[x][y] = '*'
    x, y, cnt = x + flag_pm*flag_x*1, y + flag_pm*flag_y*1, cnt+1

    for i in arr:
        print(''.join(i))
    print('')

    if cnt*flag_x+1==max_x or cnt*flag_y==max_y+1:
        flag_x, flag_y = flag_y, flag_x
        if cnt*flag_y+1==max_y: flag_pm = flag_pm * -1
        max_x, max_y = max_x - 2*flag_x, max_y - 2*flag_y
        cnt=1
    draw(x, y, max_x, max_y, flag_x, flag_y, flag_pm, cnt)

for i in range(N):
    arr[0][i] = '*'

draw(1,0,10,8)