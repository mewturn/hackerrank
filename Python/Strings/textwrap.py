# Original Problem: https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    output = ''
    step = max_width
    for i in range(0, len(string), step):
        output += string[i:i+step] + '\n'
    return output
