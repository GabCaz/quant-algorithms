def editDistance(s, t):
    n_op = edit_distance_recursive(s=s, t=t, dp=dict())
    return n_op

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

if __name__ == '__main__':
    s = "ecfbefdcfca"
    t = "badfcbebbf"
    operations = editDistance(s=s, t=t)
    print("Number of operations: {}.".format(operations))
