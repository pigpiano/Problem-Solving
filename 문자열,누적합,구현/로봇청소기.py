
# 맵의 크기 입력받기
n,m = map(int, input().split())
# 로봇의 위치와 방향 입력받기
x,y,direction = map(int, input().split())
# 맵정보 입력받기
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

# 로봇 이동을 위한 방향 정의, 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 왼쪽으로 90도 회전하는 함수
def turn_left():
	global direction
	direction -= 1
	if direction == -1:
		direction = 3
# 로봇 방문 처리를 위한 리스트
visited = [[0] * m for _ in range(n)]
# 현재 위치 방문 처리 -> 청소했다는 뜻
visited[x][y] = 1
# 따라서 현재 위치는 청소했기 때문에 1부터 시작
ans = 1
# 회전횟수를 담는 변수
turn_time = 0
# 종료될때까지 반복
while True:
	# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
	# 위에서 처리 함
	# 2. 4방향 모두 청소 했다면
	if turn_time == 4:
		# 후진 가능하면 후진 안되면 멈춤
		nx = x - dx[direction]
		ny = y - dy[direction]
		if graph[nx][ny] == 0:
			x,y = nx, ny
		else:
			break
		# 1번으로 돌아가기 위해 회전횟수 초기화
		turn_time = 0
	# 3. 청소되지 않은 곳이 있다면
	turn_left()
	nx = x + dx[direction]
	ny = y + dy[direction]
	# 청소되지 않은 칸이 있다면 한 칸 전진
	if graph[nx][ny] == 0 and visited[nx][ny] == 0:
		visited[nx][ny] = 1
		# 한 칸 전진
		x,y = nx,ny
		# 청소 영역 +1
		ans += 1
		# 다음 반복문을 위해 회전횟수 초기화
		turn_time = 0
		continue
	else: # 왼쪽으로 회전했는데, 가본 칸이라면
		turn_time += 1

print(ans)

