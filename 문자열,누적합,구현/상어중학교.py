from collections import deque
import sys
input = sys.stdin.readline

# 1. 크기가 가장 큰 블록을 찾는다.
def bfs(x,y, block_num):
	q = deque()
	q.append((x,y))

	normals = [[x,y]] # 일반 블록 위치 저장
	rainbows = [] # 무지개 블록 위치 저장

	while q:
		x,y = q.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if (0<=nx<n) and (0<=ny<n):
				# 무지개 블록을 만난 경우 : rainbow에 추가
				if graph[nx][ny] == 0 and not visited[nx][ny]:
					q.append((nx,ny))
					rainbows.append([nx,ny])
					visited[nx][ny] = True
				# 일반 블록을 만난 경우
				elif graph[nx][ny] == block_num and not visited[nx][ny]:
					q.append((nx,ny))
					normals.append([nx,ny])
					visited[nx][ny] = True
	# 무지개 블록은 다른 블록 그룹을 만들 때 중복 사용될 수 있기 때문
	# 에 BFS가 끝난 후 visited = False 해줘야한다.
	for x,y in rainbows:
		visited[x][y] = False
	# 정렬 기준에 맞게 return : 블록 수,  무지개 블록 수, 그룹 내 블록들 위치 정보(행, 열)
	return [len(normals+rainbows), len(rainbows), normals + rainbows]

# 2. bfs에서 찾은 모든 블록을 제거한다.
score = 0
def remove(group):
	global score

	score += group[0] ** 2
	for x,y in group[2]:
		graph[x][y] = -2 # 제거된 블록은 -2로 표시

# 격자에 중력 작용, 검은색 블록은 중력의 영향을 받지 않는 것에 주의
# 즉, 검색은 블록(-1)을 제외한 모든 블록이 아래(down) 방향으로 이동한다.
# 3. 중력작용
def gravity():
	for i in range(n-2,-1,-1): # 밑에서 부터 체크
		for j in range(n):
			if graph[i][j] != -1: # -1이 아니면 아래로 다운
				pointer = i
				# 다음 행이 인덱스 범위 안이면서 -2면 아래로 다운
				while pointer + 1 < n and graph[pointer+1][j] == -2:
					graph[pointer+1][j] = graph[pointer][j]
					graph[pointer][j] = -2
					pointer += 1
# 90도 반시계 방향으로 회전
def rotate():
	global graph
	temp = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			# 시계 방향이 아니라 반시계 방향으로 회전
			temp[n-j-1][i] = graph[i][j]
	graph = temp


# 격자 크기, 색상의 개수
n, m = map(int, input().split())
# 격자 정보 입력받기
graph = [list(map(int, input().split())) for _ in range(n)]
# 인접칸 이동을 위한 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 조건에 맞게 실행
while True:
	visited = [[False] * n for _ in range(n)] # 방문 여부 표시
	groups = [] # 블록 그룹 저장

	for i in range(n):
		for j in range(n):
			# 아직 방문하지 않은 일반 블록을 찾으면
			if graph[i][j] >= 1 and not visited[i][j]:
				# 방문표시
				visited[i][j] = True
				# BFS를 통해 블록 그룹 찾기
				group = bfs(i,j, graph[i][j])

				# 길이가 2 이상이라면 groups에 추가
				if group[0] >= 2:
					groups.append(group)
	# 가장 큰 블록 그룹을 찾기 위해 정렬
	groups.sort(reverse=True)

	if not groups:
		break # 종료 조건
	# 2. 블록 제거하기
	remove(groups[0])
	# 3. 중력 작용
	gravity()
	# 4. 격자 회전
	rotate()
	# 5. 다시 중력 작용
	gravity()

print(score)
