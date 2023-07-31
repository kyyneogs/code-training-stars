# baekjoon 10991

#    *
#   * *
#  * * *
# * * * *

import sys

N = int(sys.stdin.readline())

for i, j in enumerate(range(N-1, -1, -1)):
    print(' ' * j + '* ' * i + '*')