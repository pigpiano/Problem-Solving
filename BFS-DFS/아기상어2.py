'''
안전거리는 그 칸과 가장 거리가 가까운 아기 상어와의 가리
안전거리의 최댓값 구하기.
즉, 가장 가까운 상어이면서 거리가 최대인 안전거리 구하기

모든 0에 대해서 bfs하는것 아니라 상어마다 bfs 한다.
bfs의 최단거리 문제와 유사.
'''

import sys
from collections import deque

n,m = map(int, input().split())
graph = []
q = deque() # 상어의 위치를 덱에 담는다.
for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(m):
		if graph[i][j] == 1:
			q.append((i,j))
# 방향 정의 8가지 방향
# 북서, 북, 북동, 동, // 남동, 남, 남서, 서
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
ans = 0 # 최장 거리 변수
while q:
	# 첫 번째 상어의 위치
	x,y = q.popleft()
	for i in range(8):
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= m:
			continue
		if graph[nx][ny] == 0:
			graph[nx][ny] = graph[x][y] + 1
			q.append((nx,ny))
			# 안전거리 최댓값 갱신
			ans = max(ans, graph[nx][ny])

print(ans-1) # 첫번째를 포함했기 때문에 마지막에 빼준다.


