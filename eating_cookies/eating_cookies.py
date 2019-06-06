#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
memoization = {}


def eating_cookies(n, cache=None):
    global memoization
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    if n not in memoization:
        memoization[n] = eating_cookies(
            n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return memoization[n]

# eating_cookies(4)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
