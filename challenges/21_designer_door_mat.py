import math

y, x = input().split()
y = int(y)
x = int(x)

num = -1
center_part = ''

for line in range(1, y+1):
    middle_line = math.ceil(y / 2)
    if line == middle_line:
        center_part = 'WELCOME'
    else:
        if line > middle_line:
            if line != middle_line + 1:
                num -= 2
        else:
            num += 2
        center_part = '.|.'* num 

    side = '-'* math.ceil((x-len(center_part)) / 2)
    print(side + center_part + side)