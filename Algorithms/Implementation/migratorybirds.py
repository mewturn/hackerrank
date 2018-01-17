# Original Problem: https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(n, ar):
    birdtypes = {}
    max_count = high_freq = 0
    
    for bird in ar:
        if bird in birdtypes:
            birdtypes[bird] += 1
        else:
            birdtypes[bird] = 1
            
    for bird in birdtypes:
        if birdtypes[bird] > max_count:
            max_count = birdtypes[bird]
            high_freq = bird
            
    return high_freq
