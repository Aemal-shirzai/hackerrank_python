"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    runner_up = False
    arr = list(arr)
    for el in arr:
        runner_up = el if not el == max(arr) and (not runner_up or (runner_up and el > runner_up )) else runner_up
    
    print(runner_up)