# Original Problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def isLeap(year):
    if year > 1918:
        return (year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0))
    return (year % 4 ==0)

def solve(year):
    # Complete this function
    if year == 1918:
        return '26.09.1918'
    elif isLeap(year):
        return '12.09.%s' % year
    return '13.09.%s' % year
