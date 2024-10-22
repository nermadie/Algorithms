# Finding the longest palindromic substring in a given string.
# A string is palindromic if it reads the same forward and backward.
# ! Chuỗi liên tiếp
# USE test.inp

# -> spread from the center


def solve(n, s):
    if n == 1:
        return s
    result = s[0]
    for i in range(0, n - 1):
        for j in range(1, n // 2 + 1):
            if i - j < 0 or i + j >= n:
                break
            if s[i - j] != s[i + j]:
                break
            if j * 2 + 1 > len(result):
                result = s[i - j : i + j + 1]
        for j in range(1, n // 2 + 1):
            if i - j + 1 < 0 or i + j >= n:
                break
            if s[i - j + 1] != s[i + j]:
                break
            if j * 2 > len(result):
                result = s[i - j + 1 : i + j + 1]
    return result


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
