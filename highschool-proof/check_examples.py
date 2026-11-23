#!/usr/bin/env python3
"""Exact finite checks for the exposition; these are not a proof of all cases."""
from fractions import Fraction
from math import isqrt, lcm
import json


def ceiling_two_sqrt(n):
    r = isqrt(4 * n)
    return r if r * r == 4 * n else r + 1


def main():
    report = {}
    count = 0
    for length in range(1, 81):
        for k in range(-6, 7):
            middle = k * length
            left = middle - length
            images = {}
            for a in range(1, length):
                u = (middle // a) * a
                if middle % a:
                    image = (u, u + a)
                elif 2 * a < length and middle % (2 * a):
                    image = (middle - 2 * a, middle + 2 * a)
                else:
                    image = (middle - a, middle + a)
                assert left < image[0] < middle < image[1] < left + 2 * length
                assert image[0] % a == image[1] % a == 0
                assert image not in images
                images[image] = a
                count += 1
    report['special_branch_element_checks'] = count

    count = 0
    for length in range(1, 41):
        for denominator in (1, 2, 3, 5):
            for numerator in range(-2 * denominator * length, 2 * denominator * length + 1):
                left = Fraction(numerator, denominator)
                if (left / length).denominator == 1:
                    continue
                images = set()
                for a in range(1, length + 1):
                    u = ((left + length) // a) * a
                    image = (u, u + a)
                    assert left < u <= left + length < u + a < left + 2 * length
                    assert image not in images
                    images.add(image)
                    count += 1
    report['ordinary_branch_element_checks'] = count

    # Two-by-two example in the upper-bound chapter.
    array = (114, 115, 126, 127)
    z = 2176147
    actual = {a: [b for b in range(2176047, 2176300) if b % a == 0] for a in array}
    assert actual == {114: [z - 1, z + 113], 115: [z - 2, z + 113],
                      126: [z - 1, z + 125], 127: [z - 2, z + 125]}
    assert lcm(114, 126) == 2394 and lcm(115, 127) == 14605
    assert 909 * 2394 - 149 * 14605 == 1
    report['upper_bound_example'] = 'passed'

    # Six left numbers, exactly five eligible right integers.
    n = 69898816
    array = (51, 52, 57, 58, 63, 64)
    actual = {a: [b for b in range(n - 85, n + 42) if b % a == 0] for a in array}
    expected = {51: [n - 52, n - 1], 52: [n - 52, n],
                57: [n - 58, n - 1], 58: [n - 58, n],
                63: [n - 64, n - 1], 64: [n - 64, n]}
    assert actual == expected
    assert len({b for row in actual.values() for b in row}) == 5
    matching = [(51, n - 1), (58, n), (52, n - 52), (57, n - 58), (63, n - 64)]
    assert len({a for a, _ in matching}) == len({b for _, b in matching}) == 5
    assert all(b in actual[a] for a, b in matching)
    report['six_number_example'] = 'passed'

    for m in range(1, 10001):
        k = isqrt(m)
        s, t = (k, k) if m == k * k else ((k, k + 1) if m <= k * (k + 1) else (k + 1, k + 1))
        assert s * t >= m and s + t == ceiling_two_sqrt(m)
    assert [min(m, ceiling_two_sqrt(m)) for m in range(1, 17)] == [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8]
    report['rounding_integer_checks'] = 10000
    report['status'] = 'PASS'
    report['scope'] = 'Finite exact-arithmetic checks only; not an independent formal proof.'
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
