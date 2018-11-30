# https://www.hackerrank.com/challenges/strange-advertising/problem


def recurse(n):
    if n == 1:
        return 2
    return int(1.5 * int(recurse(n-1)))


def viralAdvertising(n):
    if n == 0:
        return 0
    return recurse(n) + viralAdvertising(n-1)


if __name__ == "__main__":
    print(viralAdvertising(5))
