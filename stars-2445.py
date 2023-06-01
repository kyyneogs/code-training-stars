# baekjoon 2445

N = int(input())

for i,j in enumerate(range(N,0,-1)): print("*"*(i+1) + " "*(j-1)*2 + "*"*(i+1))
for i,j in enumerate(range(N-1,0,-1)): print("*"*j + " "*(i+1)*2 + "*"*j)