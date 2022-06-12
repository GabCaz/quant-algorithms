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
Output: false
"""

""" My correct solution using memoization, and remembering what indices are feasible """


def word_break(s, word_dict):
    feasible_indices = set()  # idx is in feasible_indices iif s[idx:] can be decomposed
    feasible_indices.add(len(s))  # the word is empty: nothing left to decompose
    infeasible_indices = set()
    output = word_break_recurse(s=s, word_dict=word_dict, idx=0, feasible_indices=feasible_indices,
                                infeasible_indices=infeasible_indices)
    # print(wordDict)
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
        # print("word: {}. Subset s: {}.".format(word, s[:i]))
        if word == s[idx: idx + i]:
            if word_break_recurse(s=s, word_dict=word_dict, idx=idx + i, feasible_indices=feasible_indices,
                                  infeasible_indices=infeasible_indices):
                feasible_indices.add(idx)
                return True
            else:
                infeasible_indices.add(idx)
    return False
