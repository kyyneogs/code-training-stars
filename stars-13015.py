# *****       *****     <- input : 5        5 | 7 | 5
#  *   *     *   *
#   *   *   *   *       width : 5 + 7 + 5, height : 9, 
#    *   * *   *        middle_gap : (7) -> (5) -> (3) -> (1) -> (0) | <규칙, 초깃값> (1 + (N-1) * 2) 
#     *   *   *         left_gap : 0 -> 1 -> 2 -> 3 -> 4
#    *   * *   *        inside_gap : N-2
#   *   *   *   *
#  *   *     *   *
# *****       *****

# ** **                 <- input : 2        2 | 1 | 2
#  ***
# ** **

N = int(input())
M, L, I = (N-1)*2-1, 0, N-2
for layer in range(2*N-1):
    K = '*' if (layer==0 or layer==2*N-2) else ' '
    P = 1 if layer < N-1 else -1
    print(' ' * L + '*' + K * I + '*' * (lambda x : x!=N-1)(layer) + ' ' * M + '*' + K * I + '*')
    M, L = M-2*P, L+1*P