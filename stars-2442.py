# baekjoon 2442

N = int(input())

for i,j in enumerate(range(N, 0, -1)): print(" "*(j-1) + "*"*((i+1)*2-1))