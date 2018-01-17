# Original Problem: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

def marcsCakewalk(calorie):
    miles = current = 0 # Set variables
    for cupcake in sorted(calorie, reverse=True):
        miles = miles + cupcake * (2 ** current)
        current += 1
        
    return miles