# baekjoon 10992

#    *
#   * *
#  *   *
# *******

import sys

N = int(sys.stdin.readline())

for i, j in enumerate(range(N-1, 0, -1)):
    print((' ' * j) + ('*') + (' ' * (i*2-1)) + ('*' * int((lambda x : x>0)(i))))
print('*' * (N*2-1))