# Original Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(score):
    # Complete this function
    topbreak = 0
    botbreak = 0
    currenttop = currentbot = score[0]
    
    for i in range(1,len(score)):
        if score[i] < currentbot:
            currentbot = score[i]
            botbreak += 1
        if score[i] > currenttop:
            currenttop = score[i]
            topbreak += 1
    return topbreak, botbreak
