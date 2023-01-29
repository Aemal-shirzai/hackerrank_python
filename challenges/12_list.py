"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of 
commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""

if __name__ == '__main__':
    N = int(input())
    data = []

    for a in range(1, N + 1):
        command = input().split()

        if command[0] in ['insert']:
            getattr(data, command[0])(int(command[1]), int(command[2]))
        elif command[0] in ['remove', 'append']:
            getattr(data, command[0])(int(command[1]))
        elif command[0] in ['pop', 'reverse', 'sort']:
            getattr(data, command[0])()
        else:
            print(data)