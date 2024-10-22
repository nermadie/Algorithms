# Tìm số cách khác nhau để chọn ra các đồng xu sao cho tổng khối lượng của chúng là S. Với điều kiện, các cách lấy đồng xu là hoán vị của nhau không được coi là khác nhau.
# Kết quả tính toán với n = 3, w = [1, 3, 5] như sau:
#  S = 0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11
#  ------+--+--+--+--+--+--+--+--+--+--+--
#  k = 1 |1 |1 |2 |2 |3 |4 |4 |5 |6 |7 |8


# USE test2.inp
def solve(n, S, W):
    dp = [[0] * n for _ in range(S + 1)]
    dp[0] = [1] * n
    for i in range(1, S + 1):
        for j in range(n):
            left = 0
            top = 0
            if j != 0:
                left = dp[i][j - 1]
            if i >= W[j]:
                top = dp[i - W[j]][j]
            dp[i][j] = left + top
    return dp[S][n - 1]


t = int(input())
for _ in range(t):
    n, S = map(int, input().split())
    W = list(map(int, input().split()))
    print(solve(n, S, W))
