# baekjoon 10993

# *****************************
#  *            *            *
#   *          * *          *
#    *        *   *        *
#     *      *******      *
#      *    *  ***  *    *
#       *  *    *    *  *
#        ***************
#         *           *
#          *         *
#           *       *
#            *     *
#             *   *
#              * *
#               *

# 높이(height) : 3 -> 7 -> 15 [2 x n + 1]
# 너비(width) : 5 -> 13 -> 29 [2 x height -1]

# blank -> 왼쪽기준 현재 문양의 (height+1)/2만큼, 위쪽 기준 현재 문양의 (height+1)/2 - 1만큼

N = int(input())

initial_pattern = [['*', '*', '*', '*', '*'],
                   [' ', '*', '*', '*', ' '],
                   [' ', ' ', '*', ' ', ' ']]

def draw_pattern(depth):
    if depth > 1:
        old_height, old_pattern = draw_pattern(depth-1)
        old_width = 2 * old_height - 1

        new_height = 2 * old_height + 1
        new_width = 2 * new_height - 1

        blank = (new_height + 1) // 2

        new_pattern = [[' ' for _ in range(new_width)] for _ in range(new_height)]

        for i in range(old_height):
            for j in range(old_width):
                new_pattern[(blank - 2) * int((lambda x: x%2==0)(depth)) + i + 1][blank + j] = old_pattern[i][j]

        (first_pointer, last_pointer) = (1, new_width-2)

        if depth%2==0:
            (start_seq, end_seq, adder , straight_line) = (new_height-2, -1, -1, new_height-1)
        else:
            (start_seq, end_seq, adder , straight_line) = (1, new_height, 1, 0)

        for i in range(start_seq, end_seq, adder):
            new_pattern[i][first_pointer], new_pattern[i][last_pointer] = '*', '*'
            first_pointer += 1
            last_pointer -= 1
        for i in range(new_width):
            new_pattern[straight_line][i] = '*'

        return new_height, new_pattern
    
    elif depth==1:
        return len(initial_pattern), initial_pattern
    
    else:
        return 1, ['*']

_, pattern = draw_pattern(N-1)


if (N-1)%2==0:
    j = len(pattern[0]) // 2 + 1
    adder = 1
else:
    j = len(pattern[0])
    adder = -1

for i in pattern:
    print("".join(i[:j]))
    j += adder



# *****************************29
#  *            *            *28
#   *          * *          *27
#    *        *   *        *26
#     *      *******      *25
#      *    *  ***  *    *24
#       *  *    *    *  *23
#        ***************22
#         *           *21
#          *         *20
#           *       *19
#            *     *18
#             *   *17
#              * *16
#               *15 

#       *7
#      * *8
#     *   *9
#    *******10
#   *  ***  *11
#  *    *    *12
# *************13