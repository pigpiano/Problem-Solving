# 1 <= n <= 1000000
n = int(input())

# DP 테이블 초기화
# 연산 횟수를 저장하는 배열
d = [0] * 1000001 # 1번 인덱스부터 시작 가능

# 다이나믹 프로그래밍 진행(bottom-up)
for i in range(2, n+1): # 2부터 n까지 각 숫자에 대해 반복
	# 현재의 수에서 1을 빼는 경우
	d[i] = d[i-1] + 1 # +1 은 연산 횟수 1 증가의미
	# 현재의 수가 2로 나누어 떨어지는 경우
	if i % 2 == 0:
		d[i] = min(d[i], d[i//2] + 1)
	# 현재의 수가 3으로 나누어 떨어지는 경우
	if i % 3 == 0:
		d[i] = min(d[i], d[i//3]+1)
# n을 1로 만드는 데 필요한 최소 연삿 횟수
print(d[n])
