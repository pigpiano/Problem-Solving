
# 테케 수 입력받기
t = int(input())

for _ in range(t):
	# 정수 n 입력받기
	n = int(input())
	# dp 테이블 초기화
	dp = [0] * (n+1) # 1부터 시작

	for i in range(1, n+1):
		if i == 1:
			dp[i] = 1
		elif i == 2:
			dp[i] = 2
		elif i == 3:
			dp[i] = 4
		else:
			dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	print(dp[n])