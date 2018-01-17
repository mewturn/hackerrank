# Original Problem: https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    # Complete this function
    for i in range(1,n+1):
        print (' ' * (n-i) + '#' * i)
