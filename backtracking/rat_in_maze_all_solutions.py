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

""" My solution with backtracking """
import copy

_POSSIBLE_MOVES = {
    "L",  # left
    "R",  # right
    "U",  # up
    "D",  # down
}


def find_path(m, n):
    possible_paths = {
        (0, 0): {""}  # mapping of possible positions reachable with sets of moves that allows to reach them
    }
    possible_paths = _find_path_backtracking(x=0, y=0, move_seq="", m=m, n=n, possible_paths=possible_paths)
    sol = list(possible_paths.get((n - 1, n - 1), {}))
    sol.sort()
    return sol


def _find_path_backtracking(x: int, y: int, move_seq: str, m, n, possible_paths):
    # make new moves if possible...
    m = copy.deepcopy(m)  # remember where we are -- we don't want a move that will get us right here
    m[y][x] = 0
    # print(possible_paths)

    for move in _POSSIBLE_MOVES:
        # we need to keep track of the cells that we visited as we make paths, otherwise there is a risk to
        #  get stuck doing L - R - L - R, etc.
        x_new, y_new = _make_move(x=x, y=y, move=move)
        move_seq_new = move_seq + move
        if _position_is_valid(x=x_new, y=y_new, m=m, n=n):
            # record the move, and recurse
            pos = (x_new, y_new)
            if pos in possible_paths:
                possible_paths[pos].add(move_seq_new)
            else:
                possible_paths[pos] = {move_seq_new}
            possible_paths = _find_path_backtracking(x=x_new, y=y_new, move_seq=move_seq_new, m=m, n=n,
                                                     possible_paths=possible_paths)

    # if that position is clearly infeasible, then just give up right here
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


if __name__ == "__main__":
    N = 4
    m = [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 0, 0],
         [0, 1, 1, 1]]
    my_sol = find_path(m=m, n=N)
    print(my_sol)
