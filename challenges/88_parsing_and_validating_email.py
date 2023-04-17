
import email.utils
import re
for _ in range(int(input())):
    input_tuple = email.utils.parseaddr(input())
    if re.match(r'^[A-Za-z][A-Za-z0-9_\-\.]+@[A-Za-z]+\.[A-Za-z]{1,3}$', input_tuple[1]):
        print(email.utils.formataddr(input_tuple))