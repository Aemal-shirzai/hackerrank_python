import re
for _ in range(int(input())):
    res = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x[0] == '&&' else 'or', input())
    print(res)