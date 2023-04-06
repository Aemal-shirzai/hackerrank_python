import re

vowels = "AEIOUaeiou"
result = re.findall(r"(?<=[^%s])[%s]{2,}(?=[^%s])" % (vowels, vowels, vowels), input())
print(*result, sep="\n") if result else print("-1")