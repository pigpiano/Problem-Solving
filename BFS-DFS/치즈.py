'''
외부 공기와 접촉한 치즈만을 녹이기 위해서는 값이 0인 부분에
대해서만 BFS 진행

치즈가 다 녹았는지 어떻게 알 수 있나? 판의 초기 상태에서 치즈의 개수를
먼저 카운트한다.
'''

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = []
cnt = 0 # 전체 치즈의 개수를 카운트하기 위한 변수
for i in range(n):
	graph.append(list(map(int, input().split())))
	cnt += sum(graph[i])
# 이동을 위한 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
	# bfs의 시작지점은 가장 자리의 한 지점에서 가능
	# 판의 가장자리에는 치즈가 놓여 있지 않다
	q = deque([(0,0)])
	melt = deque([]) # 녹은 치즈를 담기위한 deque
	while q: # 큐 가 빌 때까지 반복
	# 큐가 다 비었으면 모든 공기를 탐색했다는 것이다.
		x,y = q.popleft() # 시작 탐색 위치 꺼내기
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny]:
				visited[nx][ny] = 1 # 방문처리
				if graph[nx][ny] == 0: # 공기면 계속 탐색히가 위해 큐에 넣음
					q.append((nx,ny))
				elif graph[nx][ny] == 1: # 치즈면 한번에 녹이기 위해 melt에 담아
					melt.append((nx,ny))
	# 한번에 치즈 녹이기
	for x,y in melt:
		graph[x][y] = 0 # 공기와 닿은 치즈를 한번에 녹임
	return len(melt) # 녹은 치즈의 수 반환


time = 1
while True:
	visited = [[0] * m for _ in range(n)]
	meltCnt = bfs() # 녹은 치즈의 개수
	cnt -= meltCnt
	if cnt == 0: # 치즈가 다 녹으면
		print(time, meltCnt, sep='\n')
		break
	else:
		time += 1 # 다 녹지 않았으면 한 시간 추가