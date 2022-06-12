"""
The N queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each
    other. Thus, a solution requires that no two queens share the same row, column, or diagonal.
"""

import copy

""" My solution: get all the possible solutions to the N queen problem """


def n_queen(n):
    """ Get all possible solutions to N queen problem """
    board_attacked = [[False] * n for _ in range(n)]  # board_attached[r][c] True iif cell (r, c) is attacked
    solutions = []
    solutions = recursive_n_queen(n=n, queen_no=0, board_attacked=board_attacked, solutions=solutions, temp_sol=[])

    # remember to switch back to 1-indexing (format solution)
    output = list(solutions)
    for s in output:
        for i in range(n):
            s[i] += 1
    return output


def recursive_n_queen(n, queen_no, board_attacked, solutions, temp_sol):
    queen_row = board_attacked[queen_no]
    for candidate_col in range(
            n):  # possible to iterate only from queen_no here (symmetry-breaking) and later get all reverted solutions?
        # can break symmetry by forcing the first queen to be in left side of the board
        if not queen_row[candidate_col]:
            temp_sol.append(candidate_col)
            if queen_no == n - 1:  # base case: all the queens have been placed. We have a solution
                solutions.append(copy.copy(temp_sol))
                temp_sol.pop()
                return solutions
            else:
                board_attacked, cells_already_attacked = mark_cells_attacked(r=queen_no, c=candidate_col,
                                                                             board_attacked=board_attacked, n=n)
                solutions = recursive_n_queen(n=n, queen_no=queen_no + 1, board_attacked=board_attacked,
                                              solutions=solutions, temp_sol=temp_sol)
                # recurse to the previous queen: remove position of that queen; remove cells attacked
            temp_sol.pop()
            board_attacked = unmark_cells_attacked(r=queen_no, c=candidate_col, board_attacked=board_attacked,
                                                   n=n, cells_already_attacked=cells_already_attacked)
    return solutions


def unmark_cells_attacked(r, c, board_attacked, n, cells_already_attacked):
    for r_attacked, c_attacked in get_cells_attacked_by_queen(r=r, c=c, n=n):
        if (r_attacked, c_attacked) not in cells_already_attacked:
            board_attacked[r_attacked][c_attacked] = False
    return board_attacked


def mark_cells_attacked(r, c, board_attacked, n):
    """ Mark the new attacked cells from putting a queen in (r, c). """
    cells_already_attacked = set()
    for r_attacked, c_attacked in get_cells_attacked_by_queen(r=r, c=c, n=n):
        if board_attacked[r_attacked][c_attacked]:
            cells_already_attacked.add((r_attacked, c_attacked))
        board_attacked[r_attacked][c_attacked] = True
    return board_attacked, cells_already_attacked


def get_cells_attacked_by_queen(r, c, n):
    """ Yield (row, column) attacked by a queen at given (r, c) """
    yield r, c
    for i in range(-n, n):
        if i != 0:
            # horizontal attacks
            c_attacked = c + i
            r_attacked = r
            if position_in_board(r=r_attacked, c=c_attacked, n=n):
                yield r_attacked, c_attacked
            # vertical attacks
            r_attacked = r + i
            c_attacked = c
            if position_in_board(r=r_attacked, c=c_attacked, n=n):
                yield r_attacked, c_attacked
            # diagonal attacks
            c_attacked = c + i
            r_attacked = r + i
            if position_in_board(r=r_attacked, c=c_attacked, n=n):
                yield r_attacked, c_attacked
            c_attacked = c - i
            r_attacked = r + i
            if position_in_board(r=r_attacked, c=c_attacked, n=n):
                yield r_attacked, c_attacked


def position_in_board(r, c, n):
    return 0 <= r <= n - 1 and 0 <= c <= n - 1


""" Another interesting algorithm: return True if another solution exists """


def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]

    This function is called when "col" queens are already placed in columns from 0 to col - 1, so we only need to
        check left side for attacking queens
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nq_dp(board, col, n):
    # base case: If all queens are placed
    # then return true
    if col >= n:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):

        if is_safe(board, i, col, n):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_nq_dp(board, col + 1, n) == True:
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this column col then return false
    return False


def solve_nq(n):
    board = [[0] * n for _ in range(n)]
    if solve_nq_dp(board, 0, n) == False:
        print("Solution does not exist")
        return False

    print_solution(board, n)
    return True

""" Geeks 4 Geeeks solution to printing all queens  """


# Python code to for n Queen placement
class GfG:
    def __init__(self):
        self.MAX = 10
        self.arr = [0] * self.MAX
        self.no = 0

    def breakLine(self):
        print("\n------------------------------------------------")

    def canPlace(self, k, i):

        # Helper Function to check
        # if queen can be placed
        for j in range(1, k):
            if (self.arr[j] == i or
                    (abs(self.arr[j] - i) == abs(j - k))):
                return False
        return True

    def display(self, n):

        # Function to display placed queen
        self.breakLine()
        self.no += 1
        print("Arrangement No.", self.no, end=" ")
        self.breakLine()

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if self.arr[i] != j:
                    print("\t_", end=" ")
                else:
                    print("\tQ", end=" ")
            print()

        self.breakLine()

    def nQueens(self, k, n):

        # Function to check queens placement
        for i in range(1, n + 1):
            if self.canPlace(k, i):
                self.arr[k] = i
                if k == n:
                    self.display(n)
                else:
                    self.nQueens(k + 1, n)


if __name__ == "__main__":
    n = 4
    my_sol = n_queen(n=n)
    print("All solutions to N Queens using my solution: {}.".format(my_sol))
    first_sol = solve_nq(n=n)
    obj = GfG()
    obj.nQueens(1, n)
