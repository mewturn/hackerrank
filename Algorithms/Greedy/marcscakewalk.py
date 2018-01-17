# Original Problem: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

def marcsCakewalk(calorie):
    # Complete this function
    # Set variables
    miles = current = 0
    for cupcake in sorted(calorie, reverse=True):
        miles = miles + cupcake * (2 ** current)
        current += 1
        
    return miles