'''
기준점 x,y와 경계의 길이 d1,d2가 가질 수 있는 모든
조합을 탐색하면서 선거구끼리의 인구수 차이 최솟값을
구해주면 된다.
'''

# 재현시의 크기
n = int(input())
# index 재조정
graph = [[]] # 행 과 열을 인덱스 조정
for i in range(n):
	graph.append([0]+list(map(int, input().split())))

def cal(x,y,d1,d2):
	# [0, 0, 0, 0, 0]
	arr = [0 for i in range(5)] # 선거구 당 인구수, 선거구는 5개
	temp = [[0] * (n+1) for _ in range(n+1)] # 선거구 1 ~ 5

	# 경계선을 5번 선거구로 할당
	for i in range(d1 + 1): # 왼쪽 경계
		temp[x + i][y - i] = 5 # 1번 조건 즉, 기준점
		temp[x + d2 + i][y + d2 - i] = 5 # 3번 조건
	for i in range(d2 + 1): # 오른쪽 경계
		temp[x + i][y + i] = 5 # 2번 조건
		temp[x + d1 + i][y - d1 + i] = 5 # 4번조건
	# 경계선 내부를 5번 선거구로 할당
	for i in range(x+1, x + d1 + d2):
		flag = False
		# 행을 기준으로 한번 경계구역을 만나면
		for j in range(1, n+1):
			if temp[i][j] == 5:
				flag = not flag # 다시 경계 구역을 만날 때까지
			if flag:
				temp[i][j] = 5 # 5번 구역
	# 선거구당 인원수 다 더하기
	for r in range(1, n+1):
		for c in range(1, n+1):
			if r < x + d1 and c <= y and temp[r][c] == 0:
				arr[0] += graph[r][c] # 1번 선거구
			elif r <= x + d2 and y < c and temp[r][c] == 0:
				arr[1] += graph[r][c] # 2번 선거구
			elif x + d1 <= r and c < y - d1 + d2 and temp[r][c] == 0:
				arr[2] += graph[r][c] # 3번 선거구
			elif x + d2 < r and y - d1 + d2 <= c and temp[r][c] == 0:
				arr[3] += graph[r][c] # 4번 선거구
			elif temp[r][c] == 5:
				arr[4] += graph[r][c] # 5번 선거구
	return max(arr) - min(arr) # 선거구 차이


ans = int(1e9)
# 완전 탐색
for x in range(1, n+1):
	for y in range(1, n+1):
		for d1 in range(1, n+1):
			for d2 in range(1, n+1):
				if (1<=x<x+d1+d2<=n) and (1<=y-d1<y<y+d2<=n):
					ans = min(ans, cal(x,y,d1,d2))
print(ans)

# n = int(input())
# graph = [[]]
# for i in range(n):
# 	graph.append([0] + list(map(int, input().split())))
# for i in graph:
# 	print(i)
# board = [[0] + list(map(int, input().split())) for _ in range(n)]
# for j in board:
# 	print(j)
'''
[]
[0, 1, 2, 3, 4, 1, 6]
[0, 7, 8, 9, 1, 4, 2]
[0, 2, 3, 4, 1, 1, 3]
[0, 6, 6, 6, 6, 9, 4]
[0, 9, 1, 9, 1, 9, 5]
[0, 1, 1, 1, 1, 9, 9]
'''
'''
[0, 1, 2, 3, 4, 1, 6]
[0, 7, 8, 9, 1, 4, 2]
[0, 2, 3, 4, 1, 1, 3]
[0, 6, 6, 6, 6, 9, 4]
[0, 9, 1, 9, 1, 9, 5]
[0, 1, 1, 1, 1, 9, 9]
'''