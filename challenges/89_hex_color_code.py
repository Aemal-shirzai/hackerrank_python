import re
for _ in range(int(input())):
    for match in re.findall(r'#[0-9A-Fa-f]{3,6}(?=;|,|\))', input()):
        print(match)