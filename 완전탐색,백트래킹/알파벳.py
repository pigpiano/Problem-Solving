
import sys
input = sys.stdin.readline

r,c = map(int, input().split())
graph = []
for _ in range(r):
	graph.append(list(input().rstrip()))
# for i in graph:
# 	print(i)
cnt = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	global cnt
	q = set([(x,y, graph[x][y])])
	while q:
		x,y,ans = q.pop()
		for i in range(4):
			nx,ny = x + dx[i], y + dy[i]
			if (0 <= nx < r) and (0 <= ny < c) and graph[nx][ny] not in ans:
				q.add((nx,ny, ans + graph[nx][ny]))
				cnt = max(cnt, len(ans)+1)
bfs(0,0)
print(cnt)
