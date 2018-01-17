# Original Problem: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

def hackerrankInString(s):
    # Complete this function
    mystring = 'hackerrank'
    matches = 0
    for i in range(len(s)):
        if s[i] == mystring[matches]:
            matches += 1

            # Last Index
            if matches == len(mystring)-1:
                return "YES"
    return "NO"
