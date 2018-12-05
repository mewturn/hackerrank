def partition(a, b):
    perfect_count, total_count = 1, 1
    m = 3
    
    while total_count == 0 or perfect_count/total_count >= a/b:
        k = m
        # Let x = 2 ** t (quadratic, two answers but ignore negative since 2 ** t strictly greater than 0)
        x_pos = 0.5 * (1 + ((1 + 4 * k) ** 0.5))
        # x_neg = 0.5 * (1 - ((1 + 4 * k) ** 0.5)) 
        print(m, x_pos)
        m += 1
        
        if m > 10:
            break
    return m
    

if __name__ == "__main__":
    cases = [{'a': 2, 'b': 3 }, {'a': 9, 'b': 20}]
    for case in cases:
        print(partition(*case.values()))