# Original Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    # Complete this function
    return sum([1 for i in range(n) for j in range(i+1,n) if not (ar[i] + ar[j]) % k])
