import textwrap

def wrap(string, max_width):
    
    wrapper = textwrap.TextWrapper(width=max_width)
    return '\n'.join(wrapper.wrap(text=string))
    
    # OR
    
    return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)