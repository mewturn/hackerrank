# Original Problem: https://www.hackerrank.com/challenges/pangrams/problem

def checkPangram(inp):
    inp_set = set(inp.lower())
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    
    for elem in alphabets:
        if elem not in inp_set:
            return "not pangram"
    return "pangram"
