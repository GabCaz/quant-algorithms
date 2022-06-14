"""
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both
    parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation:
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be
partitioned into two such parts.

"""


def equal_partition(arr):
    """
    Idea is to introduce new elements of arr one by one: we iteratively see the numbers we can form by selecting
        any subsets of arr[:i] (iterating over i). At each iteration, either we add the new element to the previously
        found subsets, or we do not, making clear how we can iterate to get the new sums we can make.
    Since we know all numbers are positive, we will eliminate those sums that are greater than the target, since we
        already know that those will not be reachable (they are already too big). If numbers can be negative, then
        we need to sort the array before we can use this trick.
    If we reach the target, then we stop and return.
    Otherwise, if we never return, we will have found no way to make a set that sums to the target using the elements
        in arr, so it is impossible.
     """
    sum_arr = sum(arr)
    if sum_arr % 2 != 0:
        return False  # no chance to have two equal sums if sum is not even
    target = sum_arr / 2  # we want to make a subset that sums to half the total
    reachable_numbers = {0}  # set of numbers that we can reach using the subsets
    for new_elt in arr:  # get all possible subsets using each new elt of arr
        # either we add i, or we do not
        further_candidates = set()
        for reachable_number in reachable_numbers:
            prev_set_plus_elt = reachable_number + new_elt
            if prev_set_plus_elt == target:
                return True
            if prev_set_plus_elt < target:
                further_candidates.add(prev_set_plus_elt)
        reachable_numbers.update(further_candidates)
    return False


if __name__ == "__main__":
    arr = [4, 1, 10, 12, 5, 2]
    my_sol = equal_partition(arr=arr)
