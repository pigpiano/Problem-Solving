'''
DFS와 브루트포스 알고리즘. CCTV를 회전할 수 있기 때문에
이 회전 가능한 경우의 수를 모두 따져주어 사각지대 계산
'''

import copy # 원래 값이 담겨있는 배열을 깊은 복사하기 위함
n, m = map(int, input().split())
cctv = [] # cctv종류, x좌표, y좌표
graph = []
# cctv의 방향모든 정보
mode = [
	[],
	[[0],[1],[2],[3]], # 0부터 동 남 서 북, 1번, 한 쪽방향 감시
	[[0,2],[1,3]], # 2번, 양 쪽 방향 감시
	[[0,1],[1,2],[2,3],[0,3]], # 3번, 직각 방향 감시
	[[0,1,2],[0,1,3],[1,2,3],[2,3,0]], # 4번, 세 방향 감시
	[[0,1,2,3]], # 5번, 네 방향 감시
]

for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(m):
		if graph[i][j] in [1,2,3,4,5]:
			cctv.append([graph[i][j], i, j]) # CCTV의 종류, x좌표, y좌표
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV의 방향에 따라서 범위를 넘어가지 않거나, 벽을 만나지 않는 이상
# 계속 감시를 하며 감시 되는 위치는 -1로 표시
def check(graph, mode, x,y): # 감시, mode = 1 ~ 5
	for i in mode: #CCTV의 방향에 따라서
		nx, ny = x,y
		while True: # 범위 벗어나지 않고 벽을 만나지 않는 이상 계속 감시
			nx += dx[i]
			ny += dy[i]
			# 범위를 벗어나면 중단
			if nx < 0 or nx >= n or ny < 0 or ny >=m:
				break # 반복문 탈출
			# 벽이면 중단
			if graph[nx][ny] == 6:
				break
			elif graph[nx][ny] == 0: # 감시 가능
				graph[nx][ny] = -1 # 감시 가능 표시

# dfs 알고리즘 수행
#DFS를 돌려서 해당 cctv의 종류의 각도로 감시를 실행한 후,
#cctv 갯수만큼 CCTV로 감시를 다 했을 때
#사각지대의 최솟값을 갱신한다.

min_value = int(1e9)
def dfs(depth, graph): # 탐색
	global min_value # 최솟값
	if depth == len(cctv): # 탐색완료
		count = 0
		for i in range(n): # 사각지대 찾기
			# 각 행마다 0 카운트
			count += graph[i].count(0)
		# 최솟값 업데이트
		min_value = min(min_value,count)
		return
	else:
		temp = copy.deepcopy(graph) # 맵 복제
		cctv_num,x,y = cctv[depth] # 탐색할 cctv
		for i in mode[cctv_num]: # cctv방향에 따라서
			check(temp, i, x,y)
			dfs(depth+1, temp) # 재귀 호출
			# 재귀 호출이 끝나면 맵 다시 초기화, 다음 탐색을 위해
			temp = copy.deepcopy(graph)

dfs(0, graph)
print(min_value)

