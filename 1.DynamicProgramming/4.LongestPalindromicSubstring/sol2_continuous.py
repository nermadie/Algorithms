# Finding the longest palindromic substring in a given string.
# A string is palindromic if it reads the same forward and backward.
# ! Chuỗi liên tiếp
# USE test.inp

# dp for babad
#       last b a b a d
# first
# b          1 0 1 0 0
# a          0 1 0 1 0
# b          0 0 1 0 0
# a          0 0 0 1 0
# d          0 0 0 0 1
# -> find small palindromic substring and expand it


def solve(n, s):
    max_diff = 1
    start = 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
            max_diff = 2
            start = i
    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                max_diff = diff + 1
                start = i
    return s[start : start + max_diff]


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
# Result
# bab / aba
# bb
# aca
# a
# cc
# bb
