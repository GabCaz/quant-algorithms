"""
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1},
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at
(3, 3) from (0, 0) by two paths - DRDDRR
and DDRDRR, when printed in sorted order
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is
blocked.
"""

""" 
Prints all possible paths from (0, 0) to (n - 1, n - 1).

Start from the initial index (i.e. (0,0)) and look for the valid moves through the adjacent cells in the order 
    Down->Left->Right->Up (so as to get the sorted paths) in the grid.
    
If the move is possible, then move to that cell while storing the character corresponding to the move(D,L,R,U) and 
    again start looking for the valid move until the last index (i.e. (n-1,n-1)) is reached.
Also, keep on marking the cells as visited and when we traversed all the paths possible from that cell, then unmark 
    that cell for other different paths and remove the character from the path formed.
As the last index of the grid(bottom right) is reached, then store the traversed path.

Important takeaways:
    - No need to make deep copies of the map or the visited cells: just edit the parameters as you go through paths,
        and un-edit them the other way around as you are done with that node
    - Explore paths in the alphabetical orders to get solutions in the alphabetical order
 """

# in order for solutions to be in order
_POSSIBLE_MOVES = {
    "D",  # left
    "L",  # right
    "R",  # up
    "U",  # down
}


def find_path(m, n):
    possible_paths = set()  # possible solutions
    if _position_is_valid(x=0, y=0, m=m, n=n):
        possible_paths = _find_path_backtracking(x=0, y=0, move_seq="", m=m, n=n, possible_paths=possible_paths)
    sol = list(possible_paths)
    return sol


def _find_path_backtracking(x: int, y: int, move_seq: str, m, n, possible_paths):
    # make new moves if possible...
    _cell_is_blocked = (m[y][x] == 0)  # record whether this cell is blocked
    if not _cell_is_blocked:
        m[y][x] = 0  # remember we visited this cell -- we don't want a move that will get us right here

    for move in _POSSIBLE_MOVES:
        x_new, y_new = _make_move(x=x, y=y, move=move)
        move_seq_new = move_seq + move
        if _position_is_valid(x=x_new, y=y_new, m=m, n=n):
            # record the move if it is a solution, else recurse
            if x_new == n - 1 and y_new == n - 1:
                possible_paths.add(move_seq_new)
            else:
                possible_paths = _find_path_backtracking(x=x_new, y=y_new, move_seq=move_seq_new, m=m, n=n,
                                                         possible_paths=possible_paths)
    if not _cell_is_blocked:
        m[y][x] = 1  # re-mark this cell as available for other paths to select
    return possible_paths


def _make_move(x: int, y: int, move: str):
    if move == "L":
        x -= 1
    elif move == "R":
        x += 1
    elif move == "U":
        y -= 1
    elif move == "D":
        y += 1
    return x, y


def _position_is_valid(x: int, y: int, m, n: int) -> bool:
    if x < 0 or x >= n:
        return False  # literally out of the map
    if y < 0 or y >= n:
        return False  # vertically out of the map
    if m[y][x] == 0:
        return False  # blocked cell
    return True


""" G4G solution using "visited" array -- Mark cells as visited as visited as you go, but you don't need to make a
    deepcopy of the visited matrix every single time: you can just mark the cells as visited as you go along one 
    path, and then unmark them as visited
 """
from typing import List

MAX = 5


def is_safe(row: int, col: int, m: List[List[int]], n: int, visited: List[List[bool]]) -> bool:
    """ Returns True iif the position is valid """
    return not (row == -1 or row == n or col == -1 or col == n or visited[row][col] or m[row][col] == 0)


def print_path_util(row: int, col: int,
                    m: List[List[int]],
                    n: int, path: str,
                    possible_paths: List[str],
                    visited: List[List[bool]]) -> None:

    # Check the initial point (i.e. (0, 0)) to start the paths
    if (row == -1 or row == n or
            col == -1 or col == n or
            visited[row][col] or m[row][col] == 0):
        return

    # If reach the last cell (n-1, n-1), then store the path and return
    if row == n - 1 and col == n - 1:
        possible_paths.append(path)
        return

    # Mark the cell as visited
    visited[row][col] = True

    # Try for all the 4 directions (down, left, right, up) in the given order to get the paths in lexicographical
    # order
    if is_safe(row + 1, col, m, n, visited):
        path += 'D'
        print_path_util(row + 1, col, m, n, path, possible_paths, visited)
        path = path[:-1]

    if is_safe(row, col - 1, m, n, visited):
        path += 'L'
        print_path_util(row, col - 1, m, n,
                        path, possible_paths, visited)
        path = path[:-1]

    if is_safe(row, col + 1, m, n, visited):
        path += 'R'
        print_path_util(row, col + 1, m, n,
                        path, possible_paths, visited)
        path = path[:-1]

    if is_safe(row - 1, col, m, n, visited):
        path += 'U'
        print_path_util(row - 1, col, m, n,
                        path, possible_paths, visited)
        path = path[:-1]

    # Mark the cell as unvisited for other possible paths
    visited[row][col] = False


def print_path(m: List[List[int]], n: int):
    """ Store and print all the valid paths """
    # vector to store all the possible paths
    possible_paths = []
    path = ""
    visited = [[False for _ in range(MAX)]
               for _ in range(n)]
    print_path_util(0, 0, m, n, path,
                    possible_paths, visited)
    return possible_paths


""" More efficient and memory optimized G4G solution -- Instead of maintaining visited matrix, we can modify the given 
matrix to treat it as visited matrix. """
res = []


def isValid(row, col, m, n):
    if (row >= 0 and row < n and col >= 0 and col < n and m[row][col] == 1):
        return True

    return False


def findPathHelper(m, n, x, y, dx, dy, path):
    global res

    if (x == n - 1 and y == n - 1):
        res.append(path)
        return

    dir = "DLRU"
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if (isValid(row, col, m, n)):
            m[row][col] = 2  # used to track visited cells of matrix
            findPathHelper(m, n, row, col, dx, dy, path + dir[i])
            m[row][col] = 1  # mark it unvisited yet explorable


def findPath(m, n):
    global res

    res.clear()

    # dx, dy will be used to follow `DLRU` exploring approach
    # which is lexicographically sorted order
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    if (m[0][0] == 1):
        m[0][0] = 2
        findPathHelper(m, n, 0, 0, dx, dy, "")

    return res


if __name__ == "__main__":
    n = 4
    m = [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 0, 0],
         [0, 1, 1, 1]]
    my_sol = find_path(m=m, n=n)
    backtracking_sol = print_path(m=m, n=n)
    memory_efficient_sol = findPath(m=m, n=n)
    print("My solution: {}. Backtracking solution: {}.".format(my_sol, backtracking_sol))
