# Coin Change Problem
# Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.
# If the target amount cannot be met, return -1.
# USE test1.inp
def solve(n, amount, coins):
    dp = [-1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        valid_value = [
            dp[i - item] for item in coins if i >= item and dp[i - item] != -1
        ]
        if valid_value:
            dp[i] = min(valid_value) + 1
    return dp[amount]


t = int(input())
for _ in range(t):
    n, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    print(solve(n, amount, coins))

# Result
# 3
# 3
# -1
# 0
# 3
