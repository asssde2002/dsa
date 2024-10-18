from typing import List


def lcs(str_a: int, str_b: int):
    # TC: O(m*n), SC: O(m*n)
    len_a = len(str_a)
    len_b = len(str_b)

    dp = [[0]*(len_b+1) for _ in range(len_a+1)]

    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if str_a[i-1] == str_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len_a][len_b]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    # 4
    print("Length of LCS is ", lcs(X, Y)) 
