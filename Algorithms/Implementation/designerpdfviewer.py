# Original Problem: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    # Complete this function
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphadict = {}
    alphaset = {}
    for i in range(len(alphabets)):
        alphadict[alphabets[i]] = h[i]
    
    return len(word) * max([alphadict[letter] for letter in word])
