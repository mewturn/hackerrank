# Original Problem: https://www.hackerrank.com/challenges/mark-and-toys/problem

def maximumToys(prices, k):
    # Complete this function
    toys = 0
    
    for elem in sorted(prices):
        k = k - elem
        if k <= 0:
            break
        toys += 1
    return toys