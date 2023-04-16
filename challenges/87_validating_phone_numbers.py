import re
for _ in range(int(input())):
    print('YES' if re.match(r'^[789]{1}[0-9]{9}$', input()) else 'NO')