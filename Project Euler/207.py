import math


def partition(a, b):
    # Initialize variables
    perfect_count, total_count = 0, 0
    m = 0
    growth = 2

    while total_count == 0 or perfect_count/total_count >= a/b:
        # Starting from m = 0, for 2 ** t to be an integer, m needs to grow by growth and growth grows by 2 each iteration (based on previous observations).
        # We can thus skip iterating through every m and instead iterate through the following growth rates.
        m += growth
        growth += 2

        # Let x = 2 ** t (quadratic, two answers but ignore negative since 2 ** t strictly greater than 0)
        x_pos = 0.5 * (1 + ((1 + 4 * m) ** 0.5))
        # x_neg = 0.5 * (1 - ((1 + 4 * m) ** 0.5))

        # Calculate the t value to check if it is perfect (i.e. integer)
        t = math.log(x_pos, 2)

        # Check if x is an integer (should always be - possible to remove this??)
        if not x_pos % int(x_pos):
            total_count += 1
            print(m, x_pos, t)

            # Check if t is an integer as well
            if not t % int(t):
                perfect_count += 1

        # print(perfect_count / total_count)

    return m


if __name__ == "__main__":
    cases = [{'a': 2, 'b': 3}, {'a': 9, 'b': 20}]
    for case in cases:
        print(partition(*case.values()))
