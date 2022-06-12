"""
islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

""" My correct solution for "number of islands" """


def num_islands(grid) -> int:
    n_islands = 0
    n_rows = len(grid)
    n_cols = len(grid[0])
    # for each 1 in the grid...
    for r in range(n_rows):
        for c in range(n_cols):
            # print("r: {}; c: {}".format(r, c))
            # print(grid)
            if _can_explore(grid=grid, r=r, c=c, n_rows=n_rows, n_cols=n_cols):
                # explore all the 1's that are connected to it, and mark them as explored
                _visit_island(grid=grid, r=r, c=c, n_rows=n_rows, n_cols=n_cols)
                # increment the number of islands by 1 (we found a new island)
                n_islands += 1
    # return the number of islands
    return n_islands


def _visit_island(grid, r: int, c: int, n_rows: int, n_cols: int):
    """ Mark the island that contains point (r, c) as visited """
    if _can_explore(grid=grid, r=r, c=c, n_rows=n_rows, n_cols=n_cols):
        # mark point (r, c) as visited
        grid[r][c] = "0"
        # recurse: from (r, c), we could go...
        _visit_island(grid=grid, r=r - 1, c=c, n_rows=n_rows, n_cols=n_cols)  # up
        _visit_island(grid=grid, r=r + 1, c=c, n_rows=n_rows, n_cols=n_cols)  # down
        _visit_island(grid=grid, r=r, c=c - 1, n_rows=n_rows, n_cols=n_cols)  # left
        _visit_island(grid=grid, r=r, c=c + 1, n_rows=n_rows, n_cols=n_cols)  # right


def _can_explore(grid, r: int, c: int, n_rows: int, n_cols: int) -> bool:
    """ Whether cell (r, c) can be explored """
    return (0 <= r <= n_rows - 1) and (0 <= c <= n_cols - 1) and (grid[r][c] == "1")
