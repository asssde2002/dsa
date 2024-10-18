from typing import List


def knapsnack_01(weights: List[int], values: List[int], W: int):
    # TC: O(n*W), SC: O(n*W)
    n = len(weights)
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])
            else:
                dp[i][w] = dp[i-1][w]


    return dp[n][w]


def knapsnack_01_optimized(weights: List[int], values: List[int], W: int):
    # TC: O(n*W), SC: O(W)
    n = len(weights)
    dp = [0]*(W+1)

    for i in range(n):
        for w in range(W, weights[i]-1, -1):
            dp[w] = max(dp[w], dp[w-weights[i]]+values[i])
    
    return dp[W]


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    W = 5
    max_values = knapsnack_01(weights, values, W)
    # 7
    print(max_values)
    
    max_values = knapsnack_01_optimized(weights, values, W)
    # 7
    print(max_values)

