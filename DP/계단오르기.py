
# 계단의 개수입력받기. 1 <= n <= 300
n = int(input())
# 계산의 숫자를 초기화, 1층은 1번째(not 0번째) 인덱스에 저장
stair = [0] * 301
for i in range(1, n+1):
	stair[i] = int(input())
# dp 테이블 초기화
dp = [0] * 301 # 첫 번째 계단부터 시작.
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])

# 점화식을 계산한다.
for i in range(4, n+1):
	dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])
print(dp[n])
