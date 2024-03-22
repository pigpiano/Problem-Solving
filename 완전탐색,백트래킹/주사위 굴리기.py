import sys
input = sys.stdin.readline

n, m, x,y, k = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
# for i in graph:
# 	print(i)

# 이동 명렁 주어진다. 동 서 북 남 -> 1 2 3 4
move_list = list(map(int, input().split()))

# 이동 방향 정의하기
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 가장 처음에 주사위에는 모든 면이 0이다.
# 윗면, 북 동 서 남 아랫면
dice = [0,0,0,0,0,0]
# 초기 방향 설정

# 이동할 때 마다 주사위의 윗 면에 쓰여 있는 수를 출력
for i in range(k):
	direction = move_list[i]
	# 이동 좌표 정의
	nx = x + dx[direction-1]
	ny = y + dy[direction-1]
	if nx < 0 or nx >=n or ny < 0 or ny >=m:
		continue

	if direction == 1: # 동쪽
		dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
	elif direction == 2: # 서쪽
		dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
	elif direction == 3: # 북쪽
		dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
	elif direction == 4: # 남쪽
		dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]

	# 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면
	if graph[nx][ny] == 0:
		graph[nx][ny] = dice[-1]
	# 0이 아닌경우
	elif graph[nx][ny] != 0:
		dice[-1] = graph[nx][ny]
		graph[nx][ny] = 0

	print(dice[0])
	x,y = nx,ny
