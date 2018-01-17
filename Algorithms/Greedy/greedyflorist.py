# Original Problem: https://www.hackerrank.com/challenges/greedy-florist/problem

def getMinimumCost(n, k, c):
    # Each time the number of purchases % number of people == 0, cost increases by one time (taken into account in mult)
    # Initialise multiplier, purchase count and total expenditure to = 0
    mult = purchases = total = 0
    
    # We buy the cheapest flowers last, hence sort by reverse=True
    for flower in sorted(c, reverse=True):
        if purchases % k == 0:
            mult += 1
        total = total + mult * flower
        purchases += 1
    return total