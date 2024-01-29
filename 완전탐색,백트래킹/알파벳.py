'''
시간 초과 문제로 인해 deque -> set 자료구조 활용
자료 탐색시 set의 경우 O(1)이고, deque의 경우 O(N)
'''
# 큐를 구현하기 위해 deque 라이브러리 사용
from collections import deque
# 입력을 빠르게 받기 위해
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
	graph.append(list(input()))
# 말의 이동을 위한 상 하 좌 우 살펴보기
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 시작 위치를 포함해서 카운트
result = 1
# bfs 탐색알고리즘 활용
def bfs(x,y):
	global result
	# set은 중복제거, 순서 상관x
	# {(x, y, graph[x][y])}
	q = set([(x,y, graph[x][y])]) # set에 리스트 형태, 원소는 튜플
	# 큐가 빌 때까지 반복
	while q:
		x,y,ans = q.pop() # 리스트 형태로 꺼낸다.
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 만약 주어진 범위 안에 있고 새로운 방문이라면
			if ((0 <= nx < r) and (0 <= ny < c)) and (graph[nx][ny] not in ans):
				q.add((nx,ny, ans + graph[nx][ny]))
				result = max(result, len(ans)+1)
bfs(0,0) # 좌측 상단에서 말이 출발
print(result)
