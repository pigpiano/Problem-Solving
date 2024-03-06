import sys
input = sys.stdin.readline

# 맵의 크기 입력받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
# 테트로미노를 놓았던 자리인지 확인하기 위한 배열
visited = [[False] * m for _ in range(n)]

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 최댓값 변수
max_value = 0
# ㅗ,ㅜ,ㅓ,ㅏ를 제외한 모양들 dfs를 돌며 최댓값 구하기
def dfs(x,y, temp, count):
	global max_value
	# 모양이 완성되었을 때 최댓값 구하기
	if count == 4:
		max_value = max(max_value, temp)
		return
	else:
		# 상 하 좌 우로 이동
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == False:
				visited[nx][ny] = True
				dfs(nx,ny,temp+graph[nx][ny],count+1)
				# 탐색 종료 후 다음 탐색을 위해 방문 해제
				visited[nx][ny] = False
# ㅜ,ㅗ,ㅓ,ㅏ 모양의 최댓값 계산
def excep(x,y):
	global max_value
	# 초기값은 시작점으로 설정
	temp = graph[x][y]
	# 4방향 탐색 값을 저장할 배열
	arr = []
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == False:
			arr.append(graph[nx][ny])
	length = len(arr)
	if length == 4:
		arr.sort(reverse=True)
		arr.pop() # 가장 오른쪽 데이터 추출 후 삭제!
		max_value = max(max_value, sum(arr) + graph[x][y])
	elif length == 3: # 3 방향만 들어가기 때문에 바로 sum
		max_value = max(max_value, sum(arr) + graph[x][y])
	return # length가 2 이하라면 ㅗ 모양이 아니므로 바로 return

# 이제 정답 출력하기
for i in range(n):
	for j in range(m):
		# 현재 위치는 방문처리
		visited[i][j] = True
		# dfs 탐색하기
		dfs(i,j,graph[i][j], 1)
		excep(i,j)
		# 다음 탐색을 위해 방문처리 해제
		visited[i][j] = False
print(max_value)

