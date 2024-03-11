import sys
input = sys.stdin.readline

# 남은 기간 동안 일할 날짜 입력받기
n = int(input())
# [상담기간, 비용] 각각 입력받기
schedule = [list(map(int, input().split())) for _ in range(n)]
# print(schedule)
# [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]

# dp 테이블 초기화, i번째 날짜까지 일했을 때 얻을 수 있는 최대 수익 기록
dp = [0] * 16

for i in range(n): # 0 ~ n-1
    # 상담 시작 날(i) + 상담 기간부터 마지막 날까지
    # j는 즉 상담이 가능한 모든 날짜
	for j in range(i+schedule[i][0], n+1):
    # 최대 수익이 더 작다면 최댓값으로 갱신한다.
		if dp[j] < dp[i] + schedule[i][1]:
			dp[j] = dp[i] + schedule[i][1]
print(dp)
# [0, 0, 0, 10, 30, 30, 45, 45, 0, 0, 0, 0, 0, 0, 0, 0]
print(max(dp))