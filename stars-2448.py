# baekjoon 2448

# 첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)

N = int(input())

def draw(K):
    floor = K%3
    if floor == 0:
        print('*', end='')
    elif floor==1:
        print('* *', end='')
    else:
        print('*****', end='')

for i in range(N):
    for j in range(0, N-i-1):
        print(' ', end='')
    draw(i)
    print('')