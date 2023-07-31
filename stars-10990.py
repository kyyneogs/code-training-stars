# baekjoon 10990

# input:4
# output:
#    *
#   * *
#  *   *
# *     *

N = int(input())

for i, j in enumerate(range(N-1, -1, -1)):
    print(' ' * j + '*' + ' ' * (i*2-1) + '*' * int((lambda x : x>1)(i+1)))