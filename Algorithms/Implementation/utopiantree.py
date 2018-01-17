# Original Problem: https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(n):
    # Recurrence
    if n == 0:
        return 1
        
    elif n % 2:
        return 2 * utopianTree(n-1)
        
    else: 
        return 1 + utopianTree(n-1)
