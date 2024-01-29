'''
완전 탐색 + bfs 탐색 알고리즘
점프를 뛸 때마다 0이면 이전값으로 1이면 이전 값에 + 1
'''
# 데이터를 빨리 읽어오기 위해 sys 가져오기
import sys
from collections import deque
input = sys.stdin.readline
#맵의 크기 입력받기
n, m = map(int, input().split())
# 경찰과 도둑의 위치
x1,y1,x2,y2 = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(str, input().rstrip())))

# 방문 여부 확인을 위한 2차원 리스트 만들기
# 방문 여부와 해당 정점까지의 거리를 기록 용도
visited = [[-1] * m for _ in range(n)]
# 이동을 위한 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# bfs 탐색 알고리즘 수행
def bfs(x,y):
	q = deque() # 덱을 생성해서 큐로 사용
	q.append((x,y)) # 시작점을 큐에 추가
	# 시작점을 방문처리하고 0으로 설정
	visited[x][y] = 0
	while q: # 큐가 빌 때까지 반복
		# 큐에서 원소 하나 꺼내 현재 위치로 설정
		x,y = q.popleft()
		for i in range(4):
			nx,ny = x + dx[i], y + dy[i]
			# 만약 주어진 범위를 벗어나지 않고 한번도 방문하지 않았다면
			if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == -1:
				# 다음 위치가 1이나 #인 경우 (이동가능한 경로)
				if graph[nx][ny] == '1' or graph[nx][ny] == '#':
					visited[nx][ny] = visited[x][y] + 1 # 거리 증가
					q.append((nx,ny)) # 큐에 다음 위치 추가, 큐의 오른쪽에 추가
				# 다음 위치가 0인 경우
				elif graph[nx][ny] == '0':
					# 거리 변경 없음
					visited[nx][ny] = visited[x][y]
					# 우선적으로 탐색하기 위해, 앞쪽에 삽입. bfs 우선처리
					q.appendleft((nx,ny)) # 큐의 앞쪽에 다음 위치 추가
'''
그래프 내에서 특정 조건의 경로를 우선적으로 탐색하고자 할 때 유용. 
예를 들어, 어떤 게임 맵에서 '0'이 빠른 이동 경로를 나타내고
'1', '#'이 일반 경로를 나타낸다면, 이 알고리즘은 빠른 경로를 우선적으로 
탐색하여 더 효율적인 경로를 찾는 데 도움을 준다.
'''
bfs(x1-1,y1-1)
print(visited[x2-1][y2-1])