
n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
# 비바라기 시전했을 때 생기는 비구름 좌표
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
# 구름이 이동하는 8가지 방향 정의
dx8 = [0, -1, -1, -1, 0, 1, 1, 1]
dy8 = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m): # m회 실행
	d, s = map(int, input().split())
	next_clouds = [] # 비구름 이동후 좌표
	visited = [[False] * n for _ in range(n)]
	# 1. d방향으로 s만큼 이동 후 이동 좌표를 next_clouds 에 담는다.
	for cloud in clouds:
		x, y = cloud[0], cloud[1] # 비구름 좌표
		nx = (n + x + dx8[d-1] * s) % n # 1번행과 n번행이 이어져 있음
		ny = (n + y + dy8[d-1] * s) % n # 1번열과 n번열이 이어져 있음
		next_clouds.append((nx,ny))
	# 2. 비내리기
	for cloud in next_clouds:
		x,y = cloud[0], cloud[1]
		graph[x][y] += 1 # 비구름이 있는 바구니의 물의양 1 증가시키기
		visited[x][y] = True # 방문처리
	# 3. 구름 제거
	clouds = []
	# 4. next_clouds에 있는 칸에서 대각선 방향으로 1 거리의 칸에서
	# 물의 양이 바구니의 수만큼 증가
	# 단, 이때는 대각선 방향으로 1번열 & n번열 이어지지 않는다.
	# 대각선 방향 정의
	dx4 = [-1,-1,1,1]
	dy4 = [-1,1,-1,1]
	for cloud in next_clouds:
		x,y = cloud[0], cloud[1]
		# '물이 있는 즉, graph[x][y] >= 1 바구니의 수를 센다'
		count = 0
		for i in range(4):
			nx = x + dx4[i]
			ny = y + dy4[i]
			if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] >= 1:
				count += 1
		graph[x][y] += count # 바구니의 수만큼 물의양을 증가 시킨다.
	# 5. 물의 양이 2 이상인 칸에 구름 생성 하기
	for i in range(n):
		for j in range(n):
			# 3에서 구름이 사지진 칸이 아니라는 것 -> 방문한적이 없는 칸
			if graph[i][j] >= 2 and visited[i][j] == False:
            #바구니에 저장된 물의 양이 2 이상인 모든 칸에 "구름이 생기고"
				clouds.append((i,j))
                # 물의 양이 2 줄어든다.
				graph[i][j] -= 2
ans = 0
for i in range(n): # 모든 행에 대하여
	ans += sum(graph[i])
print(ans)