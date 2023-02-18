import re
regexs_count = int(input())
for i in range(0, regexs_count):
    regex_raw = input()
    try:
        regex = re.compile(regex_raw)
    except:
        print(False)
    else:
        print(True)