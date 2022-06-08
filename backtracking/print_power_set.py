"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List, Tuple, Set


def cascading_print_subset(nums: List[int]) -> List[List[int]]:
    """
    Let's start from empty subset in output list. At each step one takes new integer into consideration and generates
     new subsets from the existing ones.
     Time complexity: \mathcal{O}(N \times 2^N)O(N×2
        N
         ) to generate all subsets and then copy them into output list.

    Space complexity: \mathcal{O}(N \times 2^N)O(N×2 N). This is exactly the number of solutions for subsets
        multiplied by the number NN of elements to keep for each subset.
    """
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output


def backtracking_print_subset(nums: List[int]) -> List[List[int]]:
    """
    his time let us loop over the length of combination, rather than the candidate numbers, and generate all
        combinations for a given length with the help of backtracking technique.
    :return:
    """

    def backtrack(first, curr):
        # if the combination is done
        if len(curr) == k:
            output.append(curr[:])
            return
        for i in range(first, n):
            """ Idea: get all sets of length k, where we we build set of lengths k iteratively, knowing that
             in each set of length k that is unique, the int is going to appear only once """
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()

    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack(first=0, curr=[])
    return output


""" My initial solution below (not very efficient because of all the object conversions), but takes advantage of 
 object structures
 """


def subsets(nums: List[int]) -> List[List[int]]:
    all_sublists = get_all_sublists(nums=tuple(nums), all_lists=set())
    # convert set of tuples to list of list
    sol = []
    for s in all_sublists:
        sol.append(s)
    sol.append([])  # add the size - subset
    return sol


def get_all_sublists(nums: Tuple[int], all_lists: Set[Tuple[int]]) -> Set[Tuple[int]]:
    """ Get all lists of non-zero sublength """
    if len(nums) == 1:
        all_lists.add(nums)
        return all_lists
    all_lists.add(nums)  # add that list
    for i in range(len(nums)):
        # recurse on every possible smaller sublist
        sublist = list(nums)
        sublist.pop(i)
        sublist = tuple(sublist)
        get_all_sublists(nums=sublist, all_lists=all_lists)
        return all_lists


if __name__ == '__main__':
    nums = [1, 2, 3]
    backtrack_sol = backtracking_print_subset(nums=nums)
