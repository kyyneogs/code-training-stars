# baekjoon 2444

N = int(input())

for i,j in enumerate(range(N, 0, -1)): print(" "*(j-1) + "*"*((i+1)*2-1))
for i,j in enumerate(range(N-1, 0, -1)): print(" "*(i+1) + "*"*(j*2-1))