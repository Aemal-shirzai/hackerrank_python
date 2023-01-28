"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)

    unique_scores = list(set(scores))
    unique_scores.sort()
    second_lowest_score = unique_scores[1]
    second_lowest_list = [item[0] for item in students if item[1] == second_lowest_score ]
    second_lowest_list.sort()

    for item in second_lowest_list:
        print(item)