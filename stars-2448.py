# baekjoon 2448

# 첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)

N = int(input())

# 가장 기초가 되는 패턴 형성
basic = [[' ',' ','*',' ',' '],
         [' ','*',' ','*',' '],
         ['*','*','*','*','*']]

def make_pattern(N):
    if N != 3:
        width = N * 2 - 1
        height = N

        new_pattern = [[' ' for _ in range(width)] for _ in range(height)] # test
        old_pattern = make_pattern(N//2)

        old_width = (width - 1) // 2
        old_height = height // 2

        for i in range(old_height):
            for j, k in enumerate(range(old_height, old_height + old_width)):
                new_pattern[i][k] = old_pattern[i][j]
        
        for i, j in enumerate(range(old_height, height)):
            for k, l in enumerate(range(old_width)):
                new_pattern[j][l], new_pattern[j][l + old_width + 1] = old_pattern[i][k], old_pattern[i][k]

    else:
        return basic

    return new_pattern

    

pattern = make_pattern(N)

# basic[1][1] = basic[0][0]

for i in pattern:
    print(''.join(i))

# 너비 = N * 2 - 1
# 높이 = N
# 다음 패턴에서는 N * (N * 2 - 1)의 직사각형에서 기존에 있던 패턴이 (N/2) 만큼 떨어진 뒤 나타나버림.
#                        *                        
#                       * *                       
#                      *****                      
#                     *     *                     
#                    * *   * *                    
#                   ***** *****                   
#                  *           *                  
#                 * *         * *                 
#                *****       *****                
#               *     *     *     *               
#              * *   * *   * *   * *              
#             ***** ***** ***** *****             
#            *                       *            
#           * *                     * *           
#          *****                   *****          
#         *     *                 *     *         
#        * *   * *               * *   * *        
#       ***** *****             ***** *****       
#      *           *           *           *      
#     * *         * *         * *         * *     
#    *****       *****       *****       *****    
#   *     *     *     *     *     *     *     *   
#  * *   * *   * *   * *   * *   * *   * *   * *  
# ***** ***** ***** ***** ***** ***** ***** *****