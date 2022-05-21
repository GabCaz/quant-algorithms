def longest_common_substr_non_contiguous(S1, S2, n, m):
    """
    Find largest common sub-string non-contiguous. E.g. for inputs
        S1 = "ABCDGH", S2 = "ACDGHR", output should be 5 (ACDGH)
    """
    # go progressively through each character of S1, and of S2. At each
    len_of_longest_subsequence = [([0] * (n + 1)) for i in range(m + 1)]

    for i_1 in range(n + 1):  # index i_1 of S1
        for i_2 in range(m + 1):  # index i_2 of S2
            # consider the longest_subsequence (i_1, i_2) between S1[:k_1] and S2[:k_2]
            if (i_1 - 1 < 0) or (i_1 - 1 < 0):  # no character: have no started going through strings
                pass  # the length of the longest subsequence is 0 since there is no character
            elif S1[i_1 - 1] == S2[i_2 - 1]:
                # there is a match: can add new element to previous longest common subsequence to make
                # a longer subsequence
                len_of_longest_subsequence[i_2][i_1] = len_of_longest_subsequence[i_2 - 1][i_1 - 1] + 1
            else:
                # there is no matcH; the new longest subsequence with i_1, i2 elements is either the previous one
                #  with i_1 - 1, i_2, or i_1, i_2 - 1
                len_of_longest_subsequence[i_2][i_1] = max(
                    len_of_longest_subsequence[i_2][i_1 - 1],
                    len_of_longest_subsequence[i_2 - 1][i_1]
                )
    # the overall longest subsequence is the one using all the elements at our disposal
    return len_of_longest_subsequence[-1][-1]



def largest_common_substr_contiguous(S1, S2, n, m):
    """
    Tabulated implementation
    """
    # go progressively through each character of S1, and of S2. At each step, record the length of the longest possible
    # substring that finishes at this item (if any)
    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.
    ans = 0
    len_of_longest_subsequence = [([0] * (n + 1)) for i in range(m + 1)]
    for i_2 in range(m + 1):  # index i_1 of S1
        for i_1 in range(n + 1):  # index i_2 of S2
            # consider the longest_subsequence (i_1, i_2) between S1[:k_1] and S2[:k_2]
            if (i_1 == 0) or (i_2 == 0):  # no character: have no started going through strings
                pass  # the length of the longest subsequence is 0 since there is no character
            elif S1[i_1 - 1] == S2[i_2 - 1]:
                # there is a match: can add new element to previous longest common subsequence to make
                # a longer subsequence
                len_of_longest_subsequence[i_2][i_1] = len_of_longest_subsequence[i_2 - 1][i_1 - 1] + 1
                ans = max(ans, len_of_longest_subsequence[i_2][i_1])
    # the overall longest subsequence is the one using all the elements at our disposal
    return ans


def lcs_contiguous_memoized(X, Y, m, n, dp):
    """ Source: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/ """
    if (m == 0 or n == 0):
        return 0

    if (dp[m][n] != -1):
        return dp[m][n]  # we already computed the longest substring finishing at X[m] using X[:m] and Y[:n]

    if X[m - 1] == Y[n - 1]:
        # there is a match, so longest substring finishing at X[m] using X[:m] and Y[:n] must be 1 + the longest
        #  substring finishing at X[m] using X[:m - 1] and Y[:n- 1]
        dp[m][n] = 1 + lcs_contiguous_memoized(X, Y, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(lcs_contiguous_memoized(X, Y, m, n - 1, dp), lcs_contiguous_memoized(X, Y, m - 1, n, dp))
    return dp[m][n]


if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    m = len(S1)
    n = len(S2)
    res_non_contiguous = longest_common_substr_non_contiguous(S1=S1, S2=S2, n=len(S1), m=len(S2))
    res = largest_common_substr_contiguous(S1=S1, S2=S2, n=m, m=n)
    g4g_res = lcs_contiguous_memoized(X=S1, Y=S2, m=m, n=n,
                                      dp=[[-1 for i in range(n + 1)]for j in range(m + 1)])
    print(0)