
# 격자의 크기 입력 받기
n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
# 시작 좌표 -> 중앙 좌표
# 0~ n-1
now = [n//2, n//2]
# 모래가 퍼져 나갈 때 각 방향으로 퍼지는 비율
left = [(-2,0, 0.02),(2,0, 0.02),
        (-1,0, 0.07),(-1,0, 0.07),
        (0,-2, 0.05),(0,-1, 0),
        (-1,-1, 0.1), (-1,1, 0.01),
        (1,-1, 0.1), (1,1, 0.01)
        ]
# 오른쪽 방향
right = [(x,-y,z) for x,y,z in left]
down = [(-y,x,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]
rate = {'left': left, 'right': right, 'down': down
        , 'up': up}
ans = 0# 격자 밖에 퍼진 모래의 양 결과
# move함수 정의
def move(cnt, dx, dy, direction):
	global ans
	# 좌표 이동하기
	for _ in range(cnt+1):
		# 현재 좌표 업데이트
		now[0], now[1] = now[0] + dx, now[1] + dy
		# 회오리를 돌다가 끝나버린 경우
		if now[0] < 0 or now[1] < 0:
			break
		# 이동함에 따라 현재 칸에서 퍼진 모래의 양 저장
		spread = 0
		# 퍼지는 모래의 양 계산
		for dx, dy, r in rate[direction]:
			nx = now[0] + dx
			ny = now[1] + dy
			if r == 0: # 퍼지지 않는다면
				sand = graph[now[0]][now[1]] - spread
			else:
				# 퍼지는 모래의 양 계산
				sand = int(graph[now[0]][now[0]] * r)
			# 범위 안에 있다면
			if (0 <= nx < n) and (0 <= ny < n):
				graph[nx][ny] += sand
			else:
				ans += sand # 밖으로 퍼짐
			spread += sand # 현재 자리에서 퍼져 나간 모래양

# 격자 밖으로 나간 모래 양
for i in range(n):
	if i % 2 == 0:
		move(i, 0, -1, 'left')
		move(i, 1, 0, 'down')
	else:
		move(i, 0, 1, 'right')
		move(i, -1, 0, 'up')
print(ans)

