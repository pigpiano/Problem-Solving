# virus_pos : 모든 바이러스의 x,y 좌표를 저장한 배열
# m : 활성 상태로 만들 바이러스 수
# blank_cnt : 빈 칸의 수
# INF : 100000 (임의의 큰 수)
# ans : 결과 값


import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
# 맵 크기 입력받기
n, m = map(int, input().split())
# 연구소 정보 입력받기
graph = [list(map(int, input().split())) for _ in range(n)]
# 바이러스 이동을 위한 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

virus_pos = [] # 바이러스 위치 정보 저장
blank_cnt = 0 # 빈 칸의 개수

def bfs(q, blanks):
	visited = [[False] * n for _ in range(n)]

	time = 0
	while True:
		length = len(q) # 큐의 길이 (=1초 동안 새롭게 추가된 바이러스 수)

		if blanks == 0 or length == 0:
			if blanks == 0: # 옵션 1. 모든 빈 칸에 바이러스 퍼뜨리면 종료
				return time
			else: # 옵션 2. 바이러스를 어떻게 놓아도 전체에 퍼뜨릴 수 없는 경우
				return INF
		time += 1
		for i in range(length): # 큐 길이만큼 반복해 주는 for 문이 이문제 핵심
			x,y = q.popleft()
			if visited[x][y] == False:
				visited[x][y] = True

			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]

				if (0<=nx<n) and (0<=ny<n) and not visited[nx][ny]:
					if graph[nx][ny] == 0: # case 1: 빈 칸을 만난 경우
						q.append((nx,ny))
						visited[nx][ny] = True
						blanks -= 1
					elif graph[nx][ny] == 2: # case 2: 비활성된 바이러스 만난 경우
						q.append((nx,ny))
						visited[nx][ny] = True




# 1. 완전탐색을 통해 빈 칸의 개수를 구하고, 모든 바이러스의 위치 정보 저장
# O(N^2)
for i in range(n):
	for j in range(n):
		if graph[i][j] == 0: # 빈 칸이라면
			blank_cnt += 1
		elif graph[i][j] == 2:  # 바이러스 라면
			virus_pos.append((i,j))
# 2. 어떤 바이러스를 활성 상태로 만들까? -> 조합 사용
virus_combi = combinations(virus_pos, m)
INF = int(1e9) # 임의의 큰 수
ans = INF
# 모든 조합 결과에 대하여
for virus in virus_combi:
	q = deque()
	for i in virus:
		q.append(i)

	temp = bfs(q, blank_cnt)
	ans = min(ans, temp)

if ans == INF: # 옵션 2. 바이러스를 어떻게 놓아도 전체에 퍼뜨릴 수 없는 경우
	print(-1)
else:
	print(ans)



