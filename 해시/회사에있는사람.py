
import sys

n = int(input()) # 사람의 수 입력 받기
arr = dict() # 딕셔너리 형

# 반복문을 통해 출입 기록을 확인 한다.

#{key:value} -> {이름 : 출입여부}
for _ in range(n):
	a, b = map(str, input().split())

	# 출입 했으면 딕셔너리로 받는다.
	if b == 'enter':
		arr[a] = b
	# 퇴근 했으면 삭제해준다.
	elif b == 'leave':
		del arr[a] # 퇴근
# 사전 순의 역순으로 정렬한다.
arr = sorted(arr.keys(), reverse=True)

for i in arr:
	print(i)

