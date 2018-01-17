# Original Problem: https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k, a):
    # Complete this function
    if sum([1 for student in a if student <= 0]) >= k:
        return "NO"
    return "YES"
