import re
pattern = r'^(?!.*(.).*\1)(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[A-Za-z0-9]{10}$'
for _ in range(int(input())):
    print('Valid' if re.match(pattern, input()) else 'Invalid')