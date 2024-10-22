# Longest Common Subsequence
# Given two strings, find the length of the longest common subsequence.
def solve(n, m, s1, s2):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            compare_value = [dp[i - 1][j], dp[i][j - 1]]
            if s1[i - 1] == s2[j - 1]:
                compare_value.append(dp[i - 1][j - 1] + 1)
            dp[i][j] = max(compare_value)
    return dp[n][m]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s1 = input()
    s2 = input()
    print(solve(n, m, s1, s2))

# Result
# 3
# 3
# 0
# 6
# 4
# 5
