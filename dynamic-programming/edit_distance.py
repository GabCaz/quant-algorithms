def editDistance(s, t):
    n_op = edit_distance_recursive(s=s, t=t, dp=dict())
    n_op_improved = edit_distance_recursive_improved(s=s, t=t, dp=dict())
    return n_op, n_op_improved

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


if __name__ == '__main__':
    s = "ecfbefdcfca"
    t = "badfcbebbf"
    operations = editDistance(s=s, t=t)
    print("Number of operations: {}.".format(operations))
