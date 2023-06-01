k=27

tree = 0

# 가운데의 빈 공간 (n/3) * (n/3)을 크기 n/3의 패턴으로 감싸는 형태.
# 규칙이 layer123 456 789 

def square(x, length, pattern):

    blank = []
    result = []
    for i in range(x//3 * x//3):
        blank.append('False')

    for i in range(9):
        if i==4: result.extend(blank)
        else: result.append()

square(k)