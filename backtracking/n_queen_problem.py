"""
The N queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each
    other. Thus, a solution requires that no two queens share the same row, column, or diagonal.
"""

import copy


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


if __name__ == "__main__":
    my_sol = n_queen(n=4)
