import sys
input = sys.stdin.readline

# queue 구현을 위해 deque 사용
from collections import deque

# 파이어스톰을 총 q번 시전하려한다.
n, q = map(int, input().split())
# 얼음 배열 입력받기
graph = [list(map(int, input().split())) for _ in range(2**n)]
level = list(map(int, input().split())) # L단계
# 얼음덩어리 방문 배열
visited = set() # 중복제거, 순서 고려x
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 배열의 길이
length = 2**n

# 격자 나눠숴 90도 회전 시키기
def divide(graph, L):
	cnt = 2**L # 격자의 길이
	for i in range(0, length, cnt):
		for j in range(0, length, cnt):
			temp = [] # 임시 배열
			for k in range(cnt): # 격자의 길이만큼
				temp.append(graph[i+k][j:j+cnt]) # 임시 배열 만들기
			temp=list(zip(*temp[::-1])) # 오른쪽 90도회전
			for k in range(cnt):
				graph[i+k][j:j+cnt]=temp[k] # 원래 배열에 반영
	return graph

# 얼음양 줄어들기
def reduce(graph):
	# 임시 배열만들기
	temp = [[0] * length for _ in range(length)]
	for x in range(length):
		for y in range(length):
			cnt = 0 # 인접한 칸중 얼음이 있는 개수
			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]
				if (0<=nx<length) and (0<=ny<length):
					# 인접하고 얼음이 있으면
					if graph[nx][ny] > 0:
						cnt += 1
			# 카운트 2 이하면
			if cnt <= 2 and graph[x][y] > 0:
				temp[x][y] -= 1 # 얼음 1 줄이기 임시 배열에 반영
	for x in range(length):
		for y in range(length):
			# 원배열에 한번에 적용
			graph[x][y] += temp[x][y]
	return graph

# 얼음 덩어리 개수 세기
def bfs(x,y):
	q = deque()
	q.append((x,y)) # 큐에 저장
	visited.add((x,y)) # 방문
	cnt = 1 # 덩어리 개수
	while q:
		x,y = q.popleft()
		for i in range(4): # 네 방향에 대하여
			nx = x + dx[i]
			ny = y + dy[i]
			if (0<=nx<length) and (0<=ny<length):
				# 방문하지 않았고 0이 아니면
				if (nx,ny) not in visited and graph[nx][ny] != 0:
					q.append((nx,ny))
					visited.add((nx,ny))
					cnt += 1 # 덩어리 개수 증가
	return cnt

# 단계 실행
for L in level:
	divide(graph, L)
	reduce(graph)
ans = 0 # 남아 있는 얼음의 합
max_ans = 0 # 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
for i in range(length):
	for j in range(length):
		if graph[i][j] > 0:
			ans += graph[i][j] # 누적합
			max_ans = max(max_ans, bfs(i,j)) # 최대 덩어리 값
print(ans)
print(max_ans)


