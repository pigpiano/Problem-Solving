import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

n,m = map(int, input().split())
graph = [list(map(int, input().split()))]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus_pos = []
for x in range(n):
	for y in range(n):
		if graph[x][y] == 2:
			virus_pos.append((x,y))
def bfs(v):
	q = deque(v)
	visited = [[-1] * n for _ in range(n)]
	time = 0

	for x,y in q:
		if visited[x][y] == -1:
			visited[x][y] = 0
	while q:
		x,y = q.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if (0<=nx<n) and (0<=ny<n) and visited[nx][ny] == -1:
				visited[nx][ny] = visited[x][y] + 1
				q.append((nx,ny))
				# 예시로 6초
				time = max(time, visited[nx][ny])
	# BFS 탐색 이후 바이러스를 퍼뜨릴 수 없는 경우를 고려
	for x in range(n):
		for y in range(n):
			if visited[x][y] == -1 and graph[x][y] != 1:
				return INF
	return time

INF = int(1e9)
ans = INF
for v in list(combinations(virus_pos,m)):
	ans = min(ans, bfs(v))
if ans == INF:
	print(-1)
else:
	print(ans)
