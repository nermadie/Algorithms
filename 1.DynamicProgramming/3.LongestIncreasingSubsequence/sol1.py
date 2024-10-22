# Given an integer array nums, return the length of the longest strictly increasing subsequence
# USE test.inp
def solve(n, arr):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))

# Result
# 4
# 4
# 1
# 6
