n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

# 반복문을 통해 각 카드 개수의 지불하는 최대 금액 구하기
for i in range(1, n+1):
	for k in range(1, i+1):
		dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[n])