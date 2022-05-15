"""The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
Source: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
"""

from typing import List, Tuple


def longest_increasing_subsequence(seq: List[float]) -> Tuple[int, List[float]]:
    """ My solution for LIS: get all LIS at each index, starting from the end """
    # maps index to LIS (if I start at index i in list, LIS is...)
    longest_subsequence_given_start_index = dict()
    n = len(seq)
    longest_subsequence_given_start_index[n - 1] = [seq[n - 1]]  # only one element
    # compute subsequences length one by one
    for i in range(n - 2, -1, -1):
        item = seq[i]
        longest_subseq_length_start_at_item = 0  # how many items we can append after this one
        longest_subseq_start_at_item = []  # the longest subsequence that starts at this item
        # the length of the subsequence starting at this index is...
        for sub_seq_start, subseq in longest_subsequence_given_start_index.items():
            if item < subseq[0]:  # then can append this sequence after item
                if len(subseq) > longest_subseq_length_start_at_item:
                    longest_subseq_length_start_at_item = len(subseq)
                    longest_subseq_start_at_item = subseq
        # the final longest subseq is the item followed by the longest possible following
        longest_subsequence_given_start_index[i] = [item] + longest_subseq_start_at_item
    # finally, retrieve the longest streak and return it
    longest_streak_len = 0
    longest_streak = []
    for start_index, long_streak in longest_subsequence_given_start_index.items():
        if len(long_streak) > longest_streak_len:
            longest_streak_len = len(long_streak)
            longest_streak = long_streak
    return longest_streak_len, longest_streak


def lis_g4g(arr):
    """ Solution from https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
    Same as me but the other way around: build LIS from the left, going towards the right, checking
    that next item is greater than previous one
    """
    n = len(arr)

    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


def g4g_reduce_to_finding_subsequence(seq):
    """longest increasing subsequence of our array must be present as a subsequence in our sorted array. That’s why our
    problem is now reduced to finding the common subsequence between the two arrays. From G4G """
    n_elements_seq = len(seq)
    # Creating the sorted list
    sorted_seq_unique_elts = sorted(list(set(seq)))
    n_elements_seq2 = len(sorted_seq_unique_elts)

    # Creating dp table for storing the answers of sub problems
    dp = [[-1 for i in range(n_elements_seq2 + 1)] for j in range(n_elements_seq + 1)]

    # Finding Longest common Subsequence of the two arrays
    for index_seq in range(n_elements_seq + 1):

        for index_seq2 in range(n_elements_seq2 + 1):
            new_elt_seq1 = seq[index_seq - 1]
            new_elt_seq2 = sorted_seq_unique_elts[index_seq2 - 1]
            if index_seq == 0 or index_seq2 == 0:
                dp[index_seq][index_seq2] = 0  # with zero element, zero common sequence
            elif new_elt_seq1 == new_elt_seq2:  # if elements match...
                # then, longest common streak with new element is longest common streak w/0 element + 1
                dp[index_seq][index_seq2] = 1 + dp[index_seq - 1][index_seq2 - 1]
            else:
                # else, longest streak is either the one with the same amount of unique elts but one less index in sequence, or the one
                #  with the same amount of indices in sequence, but one less in the amount unique elements
                dp[index_seq][index_seq2] = max(dp[index_seq - 1][index_seq2], dp[index_seq][index_seq2 - 1])
    return dp[-1][-1]


def ceil_index(seq, l, r, key):
    """ Binary search (note boundaries in the caller) """
    while (r - l > 1):

        m = l + (r - l) // 2
        if (seq[m] >= key):
            r = m
        else:
            l = m
    return r


def Longest_increasing_subsequence_length(A, size):
    """
    Even more efficient (O(n Log n) time) solution from
    https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
    Idea: as you go, keep only the subsequences which, for a given length, finish with the smallest possible
        element.

    At all times, "end element of smaller list is smaller than end elements of larger lists"
    """
    # at index "length", there is the last element of the current list of length "length"
    #  (by "current" list, we mean the one that has this length and ends with the smallest possible element)
    tail_table = [0 for i in range(size + 1)]
    tail_table[0] = A[0]
    length = 1
    for i in range(1, size):

        if (A[i] < tail_table[0]):
            # new smallest value
            tail_table[0] = A[i]

        elif (A[i] > tail_table[length - 1]):

            # A[i] wants to extend
            # largest subsequence
            tail_table[length] = A[i]
            length += 1

        else:
            # A[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # ceil value in tail_table
            tail_table[ceil_index(tail_table, -1, length - 1, A[i])] = A[i]

    return length


if __name__ == '__main__':
    seq = [3, 10, 2, 1, 20]
    my_sol = longest_increasing_subsequence(seq=seq)
    g4g_1_sol = lis_g4g(arr=seq)
    g4g_2_sol = g4g_reduce_to_finding_subsequence(seq=seq)
    Longest_increasing_subsequence_length(seq, len(seq))

    print(0)

