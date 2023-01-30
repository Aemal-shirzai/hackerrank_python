"""
Replace spaces with dash in string
"""

def split_and_join(line):
    return line.strip().replace(' ', '-')
    
    # Or
    
    return "-".join(line.strip().split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)