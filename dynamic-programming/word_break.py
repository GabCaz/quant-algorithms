"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false.

Some interesting ideas:
- collections.deque has O(1) append and pop
"""

from typing import FrozenSet, List
from functools import lru_cache
from collections import deque

""" My correct solution using memoization, and remembering what indices are feasible """


def word_break(s, word_dict):
    feasible_indices = set()  # idx is in feasible_indices iif s[idx:] can be decomposed
    feasible_indices.add(len(s))  # the word is empty: nothing left to decompose
    infeasible_indices = set()
    output = word_break_recurse(s=s, word_dict=word_dict, idx=0, feasible_indices=feasible_indices,
                                infeasible_indices=infeasible_indices)
    return output


def word_break_recurse(s, word_dict, idx, feasible_indices, infeasible_indices):
    """ Return True iff s[idx:] can be decomposed using words in word_dict """
    if idx in feasible_indices:
        return True
    if idx in infeasible_indices:
        return False
    if s[idx:] in word_dict:
        feasible_indices.add(idx)
        return True
    for word in word_dict:
        i = len(word)
        if word == s[idx: idx + i]:
            if word_break_recurse(s=s, word_dict=word_dict, idx=idx + i, feasible_indices=feasible_indices,
                                  infeasible_indices=infeasible_indices):
                feasible_indices.add(idx)
                return True
            else:
                infeasible_indices.add(idx)
    return False


""" Leetcode cute solution using LRU cache """


def word_break_lru_cache(s: str, word_dict: List[str]) -> bool:
    @lru_cache
    def word_break_memo(s: str, word_dict: FrozenSet[str], start: int):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and word_break_memo(s, word_dict, end):
                return True
        return False

    return word_break_memo(s, frozenset(word_dict), 0)


""" Leetcode solution using BFS (Breadth-First-Search) """


def word_break_bfs(s: str, word_dict: List[str]) -> bool:
    """
    Similar to my solution.
    """
    word_set = set(word_dict)
    q = deque()
    visited = set()

    q.append(0)  # we are starting at 0...
    while q:
        start = q.popleft()  # for this possible start that we have...
        if start in visited:  # if we have already tried this point, then no need to go forward: we know is infeasible
            continue
        for end in range(start + 1, len(s) + 1):  # for each possible point we can go to from this start...
            if s[start:end] in word_set:  # if this point is reachable...
                q.append(end)  # Then save if. we will be able to start from this end point later on
                if end == len(s):
                    return True  # we reached the end of the string!
        visited.add(start)  # we already tried this start, and starting from this point is infeasible
    return False


if __name__ == "__main__":
    s = "applepenapple"
    word_dict = ["apple", "pen"]
    sol = word_break(s=s, word_dict=word_dict)
    sol_cache = word_break_lru_cache(s=s, word_dict=word_dict)
    sol_bfs = word_break_bfs(s=s, word_dict=word_dict)
