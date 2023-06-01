# baekjoon 2443

N = int(input())

for i,j in enumerate(range(N, 0, -1)): print(" "*(i) + "*"*(j*2-1))