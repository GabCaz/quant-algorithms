def editDistance(s, t):
    n_op = edit_distance_recursive(s=s, t=t, dp=dict())
    n_op_improved = edit_distance_recursive_improved(s=s, t=t, dp=dict())
    str1 = s
    str2 = t
    n = len(str1)
    m = len(str2)
    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    n_op_improved_recursive = min_dis_recursive_using_indices(s1=s, s2=t, n=n, m=m, dp=dp)
    return n_op, n_op_improved, n_op_improved_recursive


def edit_distance_recursive(s, t, dp):
    """
    My solution.
    s, t two strings
    dp a dict to store the number of operations for each sub string. dp[(s, t)] contains the
        number of operations needed to match s with t
    """
    if len(s) == 0:
        return len(t)  # need to add elements of t to s, since s is empty

    if len(t) == 0:
        return len(s)  # need to remove all elements from s, since t is empty

    if (s, t) in dp:
        return dp[(s, t)]  # have already stored

    if s == t:
        dp[(s, t)] = 0
        return 0

    # if both strs start the same way, then remove first str and continue. The number of operations needed to match
    #  them both (with full index) is just the number of operations to match them without the first char
    if s[0] == t[0]:
        dp[(s, t)] = edit_distance_recursive(
            s=s[1:], t=t[1:], dp=dp
        )
        return dp[(s, t)]

    # now, if both chars don't start the same way, we can look at our operations
    # insert t[0] at the beginning of s
    s_inserted = t[0] + s
    # remove t[0] at the beginning of t
    s_removed = s[1:]
    # replace s[0] with t[0]
    s_replaced = t[0] + s[1:]
    operations_inserted = 1 + edit_distance_recursive(s=s_inserted, t=t, dp=dp)
    operations_removed = 1 + edit_distance_recursive(s=s_removed, t=t, dp=dp)
    operations_replaced = 1 + edit_distance_recursive(s=s_replaced, t=t, dp=dp)
    dp[(s, t)] = min(operations_inserted, operations_removed, operations_replaced)  # one operation
    return dp[(s, t)]


def edit_distance_recursive_improved(s, t, dp):
    """
    My solution improved after hint from G4G: no need to re-compute s, t after each operation. Simply remember that
        operations give you the flow for next iteration:
            1. Insert: Recur for m and n-1
            2. Remove: Recur for m-1 and n
            3. Replace: Recur for m-1 and n-1
    s, t two strings
    dp a dict to store the number of operations for each sub string. dp[(s, t)] contains the
        number of operations needed to match s with t
    """
    if len(s) == 0:
        return len(t)  # need to add elements of t to s, since s is empty

    if len(t) == 0:
        return len(s)  # need to remove all elements from s, since t is empty

    if (s, t) in dp:
        return dp[(s, t)]  # have already stored

    if s == t:
        dp[(s, t)] = 0
        return 0

    # if both strs start the same way, then remove first str and continue. The number of operations needed to match
    #  them both (with full index) is just the number of operations to match them without the first char
    if s[0] == t[0]:
        dp[(s, t)] = edit_distance_recursive(
            s=s[1:], t=t[1:], dp=dp
        )
        return dp[(s, t)]

    # now, if both chars don't start the same way, we can look at our operations
    # inserted: the first element of t is now matching, and the inserted element in s can be ignored
    operations_inserted = 1 + edit_distance_recursive(s=s, t=t[1:], dp=dp)
    # removed: the first element of s is gone, t is unchanged
    operations_removed = 1 + edit_distance_recursive(s=s[1:], t=t, dp=dp)
    # replaced: the first elements of s, t are now matching, and can be ignored on both sides
    operations_replaced = 1 + edit_distance_recursive(s=s[1:], t=t[1:], dp=dp)
    dp[(s, t)] = min(operations_inserted, operations_removed, operations_replaced)
    return dp[(s, t)]


def min_dis_recursive_using_indices(s1, s2, n, m, dp):
    # If any string is empty,
    # return the remaining characters of other string
    if (n == 0):
        return m
    if (m == 0):
        return n

    # To check if the recursive tree
    # for given n & m has already been executed
    if (dp[n][m] != -1):
        return dp[n][m]

    # If characters are equal, execute
    # recursive function for n-1, m-1
    if (s1[n - 1] == s2[m - 1]):
        if (dp[n - 1][m - 1] == -1):
            dp[n][m] = min_dis_recursive_using_indices(s1, s2, n - 1, m - 1, dp)
            return dp[n][m]
        else:
            dp[n][m] = dp[n - 1][m - 1]
            return dp[n][m]

    # If characters are nt equal, we need to
    # find the minimum cost out of all 3 operations.
    else:
        if (dp[n - 1][m] != -1):
            m1 = dp[n - 1][m]
        else:
            m1 = min_dis_recursive_using_indices(s1, s2, n - 1, m, dp)
    if (dp[n][m - 1] != -1):
        m2 = dp[n][m - 1]
    else:
        m2 = min_dis_recursive_using_indices(s1, s2, n, m - 1, dp)
    if (dp[n - 1][m - 1] != -1):
        m3 = dp[n - 1][m - 1]
    else:
        m3 = min_dis_recursive_using_indices(s1, s2, n - 1, m - 1, dp)

    dp[n][m] = 1 + min(m1, min(m2, m3))
    return dp[n][m]


def edit_dist_dp_tabulated_g4g(str1, str2, m, n):
    """
    Tabulated solution from Geeks 4 Geeks.

    Idea is to add chars of str1 one by one, and to compute the number of edits needed every time, using the
        previous results.

    For each new char, either we have a match, or we experiment with the three operations and get the most efficient
        one
    """
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


def buffered_tabulated_solution_edit_distance_g4g(str1, str2):
    """
    To fill a row in DP array we require only one row the upper row. For example, if we are filling the i = 10 rows in
    DP array we require only values of 9th row. So we simply create a DP array of 2 x str1 length.
    """
    len1 = len(str1)
    len2 = len(str2)

    # Create a DP array to memoize result
    # of previous computations
    DP = [[0 for i in range(len1 + 1)]
          for j in range(2)]

    # Base condition when second String
    # is empty then we remove all characters
    for i in range(0, len1 + 1):
        DP[0][i] = i

    # Start filling the DP
    # This loop run for every
    # character in second String
    for i in range(1, len2 + 1):

        # This loop compares the char from
        # second String with first String
        # characters
        for j in range(0, len1 + 1):

            # If first String is empty then
            # we have to perform add character
            # operation to get second String
            if (j == 0):
                DP[i % 2][j] = i

            # If character from both String
            # is same then we do not perform any
            # operation . here i % 2 is for bound
            # the row number.
            elif (str1[j - 1] == str2[i - 1]):
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1]

            # If character from both String is
            # not same then we take the minimum
            # from three specified operation
            else:
                DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
                                        min(DP[i % 2][j - 1],
                                            DP[(i - 1) % 2][j - 1])))

            # After complete fill the DP array
            # if the len2 is even then we end
            # up in the 0th row else we end up
            # in the 1th row so we take len2 % 2
            # to get row
            return DP[len2 % 2][len1]


if __name__ == '__main__':
    s = "ecfbefdcfca"
    t = "badfcbebbf"
    operations = editDistance(s=s, t=t)
    solution_g4g = edit_dist_dp_tabulated_g4g(str1=s, str2=t, m=len(s), n=len(t))
    print("Number of operations: {}.".format(operations))
    print("G4G tabulated -- Number of operations: {}.".format(solution_g4g))
    solution_buffered_g4g = buffered_tabulated_solution_edit_distance_g4g(str1=s, str2=t)
    print("G4G buffered tabulated -- Number of operations: {}.".format(solution_buffered_g4g))
