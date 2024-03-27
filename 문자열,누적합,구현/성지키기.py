'''
각 행과 열마다 X가 안들어 있는 행, 열의 개수를 구하고
그 중 큰 값을 출력하면 된다.
'''
n,m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
# for i in graph:
# 	print(*i)
row = 0
column = 0
# 행 탐색
for i in range(n):
	if 'X' not in graph[i]:
		row += 1
# 열 탐색
for j in range(m):
	if 'X' not in [graph[i][j] for i in range(n)]:
		column += 1
print(max(row, column))

