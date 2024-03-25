
import sys
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
	m, n, k = map(int, input().split())
	graph = [[0] * m for _ in range(n)]
	for i in range(k):
		x,y = map(int, input().split()) # 열 행
		graph[y][x] = 1 # 배치가 있는 위치 1로 표시

	# dfs 함수 정의
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	def dfs(y,x):
		if x < 0 or x >=m or y < 0 or y >=n:
			return False
		if graph[y][x] == 1:
			graph[y][x] = 0
			dfs(y-1,x)
			dfs(y+1,x)
			dfs(y,x+1)
			dfs(y,x-1)
			return True
		return False
	ans = 0 # 최소 배추 흰지렁이 마리 수 구하기
	for i in range(n):
		for j in range(m):
			if dfs(i,j) == True:
				ans += 1
	print(ans)

