# Source: https://www.geeksforgeeks.org/solve-dynamic-programming-problem/

# Given 3 numbers {1, 3, 5}, we need to tell the total number of ways we can form a number
# 'N' using the sum of the given three numbers.

def solve(n: int, lookup: dict):
    # Base cases
    # negative number can't be
    # produced, return 0
    if n < 0:
        return 0

    # 0 can be produced by not
    # taking any number whereas
    # 1 can be produced by just taking 1
    if n == 0:
        return 1

    # Checking if number of way for
    # producing n is already calculated
    # or not if calculated, return that,
    # otherwise calculate and then return
    if n not in lookup:
        lookup[n] = (solve(n - 1, lookup) +
                     solve(n - 3, lookup) +
                     solve(n - 5, lookup))

    return lookup[n]


if __name__ == '__main__':
    solve(n=7, lookup=dict())
