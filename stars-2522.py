# baekjoon 2522
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

N = int(input())

for i, j in enumerate(range(N-1,-1,-1), start=1):
    print(' ' * j + '*' * i)

for k, l in enumerate(range(N-1, 0, -1), start=1):
    print(' ' * k + '*' * l)

#   *
#  **
# ***
#  **
#   *