# baekjoon 2446

N = int(input())

for i,j in enumerate(range(N,0,-1)): print(" "*(i) + "*"*(j*2-1))
for i,j in enumerate(range(N-1,0,-1)): print(" "*(j-1) + "*"*((i+2)*2-1))