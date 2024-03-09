import sys
input = sys.stdin.readline

# 수의 개수 N, 합을 구하는 횟수 M
n, m = map(int, input().split())
# n개의 수가 주어진다.
data = list(map(int, input().split()))
# init prefix_sum
prefix_sum = [0]

temp = 0
for i in data: # 각각의 합을 배열에 누적해서 저장
	temp += i
	prefix_sum.append(temp)
# print(prefix_sum): [0, 5, 9, 12, 14, 15]
for i in range(m):
	a, b = map(int, input().split())
	print(prefix_sum[b] - prefix_sum[a-1])