
# 격자의 크기 입력 받기
n = int(input())
# 맵 정보 입력받기
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
# 시작 좌표. (x좌표, y좌표)
now = [n // 2, n // 2]
# 왼쪽 방향으로 퍼질 때, y기준
# 중앙에서 외부로 퍼트릴 때 발생하는 상황 모델링
# 모래가 퍼져 나갈 때 각 방향으로 퍼지는 모래의 비율을 나타낸다.
# left 정의를 기반으로 오른쪽, 아래쪽, 위쪽 방향으로의 비율과 방향을 계산
left = [(-2,0, 0.02),(2,0, 0.02),(-1,-1, 0.1),(-1,0, 0.07),(-1,1, 0.01)
        ,(1,-1, 0.1),(1,0, 0.07),(1,1, 0.01),(0,-2, 0.05),(0,-1, 0)]
# 오른쪽 방향 -> x좌표와 y좌표를 반대로
# 방향별 모래 퍼짐 비율을 딕셔너리에 저장
right = [(x,-y,z) for x,y,z in left] # 오른쪽 방향으로 퍼질 때
down = [(-y,x,z) for x,y,z in left] # 아래쪽 방향으로 퍼질 때
up = [(y,x,z) for x,y,z, in left] # 위쪽방향으로 퍼질 때
rate = {'left': left, 'right': right, 'down': down, 'up': up }

ans = 0 # 격자 밖으로 나간 모래의 총량을 저장할 변수 초기화
#모래를 흩날리는 함수
def move(cnt, dx, dy,direction):
	global ans
    # 좌표 이동하기
	for _ in range(cnt+1):
		# 현재 좌표 업데이트
		now[0], now[1] = now[0] + dx, now[1] + dy
		# 회오리를 돌다가 끝나버린 경우
		if now[0] < 0 or now[1] < 0:
			break
		spreads = 0  # 현재 칸에서 퍼진 모래의 양을 저장할 변수 초기화
		# 퍼지는 모래의 양 계산
		for dx, dy, r in rate[direction]:
			nx,ny = now[0] + dx, now[1] + dy
			if r == 0: # 퍼지지 않는 모래들은 현재 자리에 누적
				sand = graph[now[0]][now[1]] - spreads
			else: # 퍼지는 모래의 양 계산
				sand = int(graph[now[0]][now[1]] * r)

			# 격자 안에 있는 경우 모래양 업데이트, 격자 밖인 경우 ans 업데이트
			if (0 <= nx < n) and (0 <= ny < n): # 범위 안
				graph[nx][ny] += sand
			else: # 범위 밖: 정답 누적값 업데이트
				ans += sand
			spreads += sand # 현재 자리 계산을 위한 퍼지는 모래의 누적값

for i in range(n):
	if i % 2 == 0:
		move(i,0,-1,'left') # 왼쪽
		move(i,1,0,'down') # 아래
	else:
		move(i,0,1,'right') # 오른쪽
		move(i,-1,0,'up') # 위
print(ans)
