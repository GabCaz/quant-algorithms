"""
https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1

Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].

Matrix [r+1] [c]
Matrix [r+1] [c-1]
Matrix [r+1] [c+1]
Starting from any column in row 0 return the largest sum of any of the paths up to row N-1.

Example 1:

Input: N = 2
Matrix = {{348, 391},
          {618, 193}}
Output: 1009
Explanation: The best path is 391 -> 618.
It gives the sum = 1009.
"""


def get_max_cost_using_recursive(N, Matrix):
    possible_costs_to_last_row = [-1 for _ in range(N)]  # all possible costs to go to any cell of the last row
    dp = [[-1] * N for _ in range(N)]  # don't know any costs at first
    for c in range(N):  # for any possible column in the last row
        cost_to_that_col = recursive_max_cost(N=N, Matrix=Matrix, dp=dp, r=N - 1, c=c)
        possible_costs_to_last_row[c] = cost_to_that_col
    return max(possible_costs_to_last_row)  # the overall max is max to very last row with highest col score


def recursive_max_cost(N, Matrix, dp, r, c):
    """
    Get the max cost for that Matrix to go from first row (anywhere) to (r, c)
    Matrix: contains the costs
    dp: dp[r][c] contains the maxCost to go to [r][c] if it was computed,
        or -1 if it was not computed
    """
    # cost is infinite if we cannot go there (never select)
    if r < 0 or r >= N or c < 0 or c >= N:
        return float("-inf")

    if dp[r][c] >= 0:
        return dp[r][c]  # was already computed: return

    # base case: we just want to go to the first row
    if r == 0:
        dp[r][c] = get_cost_of_cell(Matrix=Matrix, N=N, r=r, c=c)
        return dp[r][c]

    # recusion: the maximum cost to go to (r, c) is the cost of (r, c)
    #  plus the maximum cost to go to any cell from which we can go to (r, c)
    else:
        max_cost_upper = recursive_max_cost(N=N, Matrix=Matrix, dp=dp, r=r - 1, c=c)
        max_cost_upper_right = recursive_max_cost(N=N, Matrix=Matrix, dp=dp, r=r - 1, c=c + 1)
        max_cost_upper_left = recursive_max_cost(N=N, Matrix=Matrix, dp=dp, r=r - 1, c=c - 1)
        dp[r][c] = get_cost_of_cell(Matrix=Matrix, N=N, r=r, c=c) + max(max_cost_upper, max_cost_upper_right,
                                                                        max_cost_upper_left)
        return dp[r][c]


def get_cost_of_cell(Matrix, N, r: int, c: int):
    """
    r, c: coordinates. Get the cost of passing by m, n
    Cost is read out if in grid, or infinite otherwise (impossible)
    """
    if (0 <= r <= N - 1) and 0 <= c <= N - 1:
        return Matrix[r][c]
    return float("-inf")  # impossible to go through (m, n): infinite cost (never select)
