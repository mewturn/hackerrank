# https://code.google.com/codejam/contest/32003/dashboard
# Problem A. Alien Numbers


def convertToAlien(num, source, target):
    s = getSourceBase(source)
    t = getTargetBase(target)
    s_value = 0
    for i in range(len(num)):
        s_value += s[num[i]] * len(source) ** i

    # variables
    quotient = s_value
    out = ""

    while quotient > 0:
        remainder = quotient % len(target)
        quotient = int(quotient / len(target))
        out += t[remainder]

    return out[::-1]


def getTargetBase(base):
    base_dict = {}
    for k, v in enumerate(base):
        base_dict[k] = v

    return base_dict


def getSourceBase(base):
    base_dict = {}
    for v, k in enumerate(base):
        base_dict[k] = v

    return base_dict


if __name__ == "__main__":
    tc1 = "9 0123456789 oF8"
    tc2 = "Foo oF8 0123456789"
    tc3 = "13 0123456789abcdef 01"
    tc4 = "CODE O!CDE? A?JM!."

    tc = [tc1, tc2, tc3, tc4]

    for test in tc:
        test = test.split()
        n, s, t = test[0][::-1], test[1], test[2]
        print(convertToAlien(n, s, t))
