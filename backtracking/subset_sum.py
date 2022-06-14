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

""" My correct solution  """


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


""" 
Solution using dynamic programming (Geeks 4 Geeks) in pseudo-polynomial time
    
There are two cases:
    1. Consider the last element and now the required sum = target sum – value of ‘last’ element and number of 
        elements = total elements – 1
    2. Leave the ‘last’ element and now the required sum = target sum and number of elements = total elements – 1
    
I.E. isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) || isSubsetSum(set, n-1, sum-set[n-1])

Time Complexity: O(sum*n), where sum is the ‘target sum’ and ‘n’ is the size of array.
Auxiliary Space: O(sum*n), as the size of 2-D array is sum*n. + O(n) for recursive stack space
"""


def is_subset_sum(arr, n, target):
    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..i-1] with sum equal to j
    subset = ([[False for i in range(target + 1)]
               for i in range(n + 1)])

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, target + 1):
        subset[0][i] = False

    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < arr[i - 1]:
                # the target is smaller than the element: do not select element. So, we could only reach
                #  the value if we could reach the value with the previous elements we had
                subset[i][j] = subset[i - 1][j]
            if j >= arr[i - 1]:
                # the target is greater than the element: see if any of previous states have already experienced the
                #   sum=’j’ (I.E. do not select the new element) OR any previous states experienced a value
                #   ‘j – A[i]’ (I.E. we select the new element)
                subset[i][j] = (subset[i - 1][j] or
                                subset[i - 1][j - arr[i - 1]])
    return subset[n][target]


""" 
Space optimized dynamic programming: for filling a row only the values from previous row is required. So alternate 
rows are used either making the first one as current and second as previous or the first as previous and second as 
current.  
"""


def is_subset_target_space_optimized(arr, n, target):
    """ Trick: use modulo 2 to define current and previous index """
    # The value of subset[i%2][j] will be true
    # if there exists a subset of sum j in
    # arr[0, 1, ...., i-1]
    subset = [[False for j in range(target + 1)] for i in range(3)]

    for i in range(n + 1):
        for j in range(target + 1):
            # A subset with sum 0 is always possible
            curr_i = i % 2
            prev_i = (i + 1) % 2
            if j == 0:
                subset[curr_i][j] = True

            # If there exists no element no sum
            # is possible
            elif i == 0:
                subset[curr_i][j] = False
            elif arr[i - 1] <= j:
                subset[curr_i][j] = subset[prev_i][j - arr[i - 1]] or subset[prev_i][j]
            else:
                subset[curr_i][j] = subset[prev_i][j]

    return subset[n % 2][target]


if __name__ == "__main__":
    arr = [4, 1, 10, 12, 5, 2]
    my_sol = equal_partition(arr=arr)
    target = sum(arr) / 2
    n = len(arr)
    solution_dp = is_subset_sum(arr=arr, n=n, target=int(target))
    space_optimized_res = is_subset_target_space_optimized(arr=arr, n=n, target=int(target))
