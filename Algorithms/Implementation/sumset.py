# Original Problem: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def sumSet(arr):
    myset = set()
    
    # Build dictionary
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    mydict = {}    
    for i in range(1, len(alphabets)+1):
        mydict[alphabets[i-1]] = i
    
    current_substring = arr[0]
    myset.add(mydict[arr[0]]) 
    
    for i in range(1, len(arr)):        
        value = mydict[arr[i]]
        if arr[i] not in current_substring:
            current_substring = arr[i]
            mysum = value
            
        else:
            current_substring += arr[i]          
            mysum = value * len(current_substring)
        
        myset.add(mysum)
    
    return myset
