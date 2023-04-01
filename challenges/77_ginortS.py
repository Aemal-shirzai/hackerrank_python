S = input()

lower_case = []
upper_case = []
odd_digits = []
even_digits = []
for char in S:
    if not char.isnumeric():
        lower_case.append(char) if char.islower() else upper_case.append(char)
    else:
        even_digits.append(char) if int(char) % 2 == 0 else odd_digits.append(char)    

print(''.join(sorted(lower_case) + sorted(upper_case) + sorted(odd_digits) + sorted(even_digits)))