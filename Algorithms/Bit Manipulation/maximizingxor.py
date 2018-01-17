# Original Problem: https://www.hackerrank.com/challenges/maximizing-xor/problem

def maximizingXor(l, r):
    upp = max(l,r) + 1
    bot = min(l,r)
    return max([x^y for x in range(bot,upp) for y in range(bot,upp)])