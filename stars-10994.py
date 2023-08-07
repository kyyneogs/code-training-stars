# *********     <- input : 3
# *       *     height : 1 -> 5 -> 9 (4씩 증가)
# * ***** *     width : 1 -> 5 -> 9 (4씩 증가)
# * *   * *     모서리로부터 (N-1)*2 가 떨어져 있는 곳에다가 별찍기 ->
# * * * * *
# * *   * *
# * ***** *
# *       *
# *********

def draw(N, w, h, d=0):
    if d > N//2:
        print(' ', end='')
    else:
        if (w>=d and w<=N-d-1) and (h==d or h==N-d-1):
            print('*', end='')
        elif (h>=d and h<=N-d-1) and (w==d or w==N-d-1):
            print('*', end='')
        else: 
            draw(N, w, h, d+2)

N = int(input())
K = 4 * (N - 1) + 1

for i in range(K):
    for j in range(K):
        draw(K, i, j)
    print('')