def minion_game(string):
    keven_score = 0 # Vowels
    stuart_score = 0 # constants
    
    s=len(string)
    for i in range(s):
        if string[i] in 'AEIOU':
           keven_score+=(s-i)
        else:
           stuart_score+=(s-i)
        
    if keven_score < stuart_score:
        print('Stuart ' + str(stuart_score))
    elif keven_score > stuart_score:
        print('Kevin ' + str(keven_score))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)