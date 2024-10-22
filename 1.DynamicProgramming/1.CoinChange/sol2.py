# Tìm số cách khác nhau để chọn ra các đồng xu sao cho tổng khối lượng của chúng là S.
# Công thức đệ quy cho bài toán quy hoạch động
#   {dp[0] = 1;
#   {dp[P] = sum(dp[P-Wi]);   (for Wi <= P)
#
# Với đầu vào như sau: n = 3, S = 11, W = [1, 3, 5]
# Mảng kết quả quy hoạch động sẽ là
#  P = 0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11
#  ------+--+--+--+--+--+--+--+--+--+--+--
#  k = 1 |1 |1 |2 |3 |5 |8 |12|19|30|47|74


# USE test2.inp
def solve(n, S, W):
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(1, S + 1):
        for item in W:
            if item > i:
                break
            dp[i] += dp[i - item]
    return dp[S]


t = int(input())
for _ in range(t):
    n, S = map(int, input().split())
    W = list(map(int, input().split()))
    print(solve(n, S, W))
