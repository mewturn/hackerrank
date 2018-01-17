# Original Problem: https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a):
    num_dict = {}
    
    for elem in a:
        if elem in num_dict:
            num_dict[elem] += 1
        else:
            num_dict[elem] = 1
    
    prev_num = None
    max_diff = diff =  0
    
    for num in sorted(num_dict):
        if prev_num == None:
            prev_num = num
            continue
        
        if num - prev_num == 1:
            diff = num_dict[num] + num_dict[prev_num]
            if diff > max_diff:
                max_diff = diff
        prev_num = num
        
    return max_diff
