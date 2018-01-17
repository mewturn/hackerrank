# Original Problem: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    return "".join([character.upper() if character.islower() else character.lower() for character in s])
