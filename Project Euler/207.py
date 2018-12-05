import math


def partition(a, b):
    perfect_count, total_count = 1, 1
    m = 2

    while perfect_count/total_count >= a/b:
        m += 1
        # Let x = 2 ** t (quadratic, two answers but ignore negative since 2 ** t strictly greater than 0)
        x_pos = 0.5 * (1 + ((1 + 4 * m) ** 0.5))
        # x_neg = 0.5 * (1 - ((1 + 4 * k) ** 0.5))
        t = math.log(x_pos, 2)
        # print(m, x_pos, t)

        # Check if x is an integer
        if not x_pos % int(x_pos):
            total_count += 1
            # Check if t is an integer as well
            if not t % int(t):
                perfect_count += 1

        # print(perfect_count / total_count)
    return m


if __name__ == "__main__":
    cases = [{'a': 2, 'b': 3}, {'a': 9, 'b': 20}]
    for case in cases:
        print(partition(*case.values()))
