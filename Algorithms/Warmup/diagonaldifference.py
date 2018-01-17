# Original Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem

# Not so efficient :(
def diagonalDifference(a):
    leftdiag = 0
    rightdiag = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                leftdiag += a[i][j]
            if i + j == len(a)-1:
                rightdiag += a[i][j]
    return abs(leftdiag - rightdiag)
