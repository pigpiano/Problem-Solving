n = int(input())

data = list(map(int, input().split()))

# 반복문을 1에서 시작하는 이유
# 이전까지 모든 숫자의 합 중 최댓값을 그때 그때 기록하는 것
# 데이터의 시작점이 0번 인덱스는 이전까지의 합이 0 자신 자체이기 때문에
# 아무런 필요가 없다.
for i in range(1, n):
	# i번째 데이터를 업데이트 하는 이유
	# i번째 인덱스는 핵심코드의 논리인 "이전까지 모든 숫자의 합 중 최댓값"
	# 이기 때문에 업데이트 해야한다.
	data[i] = max(data[i], data[i-1]+data[i])
print(data)
print(max(data))