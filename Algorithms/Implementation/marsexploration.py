# Original Problem: https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    mylist = ['S', 'O', 'S']
    return sum([1 for i in range(len(s)) if s[i] != mylist[i%len(mylist)]])
