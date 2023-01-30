def count_substring(string, sub_string):
    occurance = 0
    for i in range(len(string)):
        c_index = i
        match_text = ''
        while c_index < len(string) and len(match_text) < len(sub_string):
            match_text += string[c_index]
            if sub_string == match_text:
                occurance += 1
            c_index += 1
            
    return occurance

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)