# Original Problem: https://www.hackerrank.com/challenges/pangrams/problem

def checkPangram(inp):
    inp_set = set(inp.lower()) # Set to lower-case
    alphabets = set('abcdefghijklmnopqrstuvwxyz')
    
    # Check that all of the alphabets are in the input set
    for elem in alphabets:
        if elem not in inp_set:
            return "not pangram"
    return "pangram"
