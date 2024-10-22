# Finding the longest palindromic substring in a given string.
# A string is palindromic if it reads the same forward and backward.
# ! Chuỗi không liên tiếp
# USE test.inp
def solve(n, s):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            compare_values = [dp[i - 1][j], dp[i][j - 1]]
            if s[n - i] == s[j - 1]:
                compare_values.append(dp[i - 1][j - 1] + 1)
            dp[i][j] = max(compare_values)
    result = ""
    cur_val = dp[n][n]
    row, col = n, n
    while cur_val > 0:
        if dp[row][col] == dp[row - 1][col]:
            row -= 1
        elif dp[row][col] == dp[row][col - 1]:
            col -= 1
        else:
            result += s[col - 1]
            cur_val -= 1
            row -= 1
            col -= 1

    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
# Result
# bab / aba
# bb
