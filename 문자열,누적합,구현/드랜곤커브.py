
n = int(input())
# 좌표가 드래곤 커브에 포함되는지 체크해줄 리스트
check = [[0] * (101) for _ in range(101)]

# 방향 정의  0 1 2 3, x,y 좌표가 바뀜
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# n번 반복
for _ in range(n):
	x,y,d,g = map(int, input().split())
	# 주어진 g세대 동안 움직인 방향들을 담아둘 리스트
	dragon = [d] # 초기 방향 미리 삽입
	# 먼저 시작하는 x,y좌표는 방문처리
	check[x][y] = 1
	# 세대 만큼 For문을 돌면서
	for i in range(g):
		temp = []
		# 시작 세대 d로 초기화한 dragon의 길이만큼 for문을 돌린다.
		# 앞으로 계속 추가해줄 것이기 때문에 길이는 늘어난다.
		for j in range(len(dragon)):
			# 이전 세대들을 돌면서 뒤에서부터 방향에 1을 더하고 4로나눠
			# 방향을 tmp에 추가한다.
			temp.append((dragon[-j-1]+1) % 4)
		# dragon에 tmp를 extend 시켜서 뒤에 그대로 붙여준다.
		dragon.extend(temp)

	# g세대만큼 실행한 뒤
	# dragon에 있는 방향들을 확인하면서 좌표를 계산해주고, check처리한다.
	for i in dragon:
		nx = x + dx[i]
		ny = y + dy[i]
		check[nx][ny] = 1 # 체크 처리
		x,y = nx,ny # 좌표를 현재 움직인 방향으로 갱신

ans = 0
# 100,100 좌표를 돌면서 한 좌표가 1로 체크되어있을 때,
# 나머지 오른쪽, 아래, 오른쪽 아래대각선이 1로 체크되어있으면
# answer += 1  을 해준다.
for i in range(100):
	for j in range(100):
		if check[i][j] == 1 and check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
			ans += 1
print(ans)
