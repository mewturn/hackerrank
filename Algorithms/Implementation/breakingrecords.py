# Original Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(score):
    topbreak = botbreak = 0 # Set variables
    currenttop = currentbot = score[0] # First score is both the max and the min score
    
    for i in range(1,len(score)):
        if score[i] < currentbot:
            currentbot = score[i]
            botbreak += 1
        if score[i] > currenttop:
            currenttop = score[i]
            topbreak += 1
    return topbreak, botbreak
