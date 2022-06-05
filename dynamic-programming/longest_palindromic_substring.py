"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

""" My solution: each palindrome is composed of a left part, a central part, and a right part. Check all. """


def longest_palindrome_my_sol(s: str) -> str:
    # basic central elements are just all suites of characters that can be the center of a palindrome, and they have
    #  two lists: one on the right, one on the left,
    #  which we want to check for a palindrome aorund the central element
    palindrome_candidates = []  # list of tuples (left, right, central element) that we need to consider for palindromes
    for i, c in enumerate(list(s)):
        if not i:
            _central_element = str(s[i])
            continue
        if c == _central_element[-1]:  # central element can have duplicated letters: it does not change anything
            _central_element = _central_element + c
        else:
            left = s[:i - len(_central_element)]
            right = s[i:]
            palindrome_candidates.append((left, _central_element, right))
            _central_element = str(c)
    # append the very last piece (end of string
    palindrome_candidates.append(("", _central_element, s[:-len(_central_element)]))

    _len_longest_palindrome = 1
    _longest_palindrome = str(s[0])
    # now, check how well we can make palindromes around each central element
    for left, central_element, right in palindrome_candidates:
        left_palindromic, right_palindromic = _get_palindromic_subseq(left=left, right=right)
        if 2 * len(left_palindromic) + len(central_element) > _len_longest_palindrome:
            _longest_palindrome = left_palindromic + central_element + right_palindromic
            _len_longest_palindrome = len(_longest_palindrome)
    return _longest_palindrome


def _get_palindromic_subseq(left, right):
    left_palindromic = ""
    for i in range(len(left)):
        char_left = left[len(left) - i - 1]
        if i >= len(right) or char_left != right[i]:  # the mirror around the center stops here
            return left_palindromic, left_palindromic[::-1]
        left_palindromic = char_left + left_palindromic
    return left_palindromic, left_palindromic[::-1]
