n, m, k = map(int, input().split())
# x, y, m, s, d
fireball = []
for _ in range(m):
	r,c,m,s,d = list(map(int, input().split()))
	# 1 <= r,c <= N이므로 -1해준다. for 컴퓨터 읽고 계산
	fireball.append([r-1,c-1,m,s,d]) # 리스트 형태로 저장한다.
# 파이어볼의 질량, 속도, 방향 저장
graph = [[[] for _ in range(n)] for _ in range(n)]
# 8가지 방향 -> 북쪽 부터 시작. 12부터 시작 ~ 11시
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k): # k회 명령하기
	while fireball:
		x,y,m,s,d = fireball.pop(0)
		# 1. 파이어볼 이동하기
		# 조건이 0 <= d <=7 이므로 -1 할 필요 없다.
		nx = (x + dx[d] * s) % n # 1번 ~ N번 행 연결되어 있다. 이어진 격자!
		ny = (y + dy[d] * s) % n
		graph[nx][ny].append([m,s,d]) # 질량, 속력, 방향을 리스트 형태로 묶어서 저장
	# 2. 파이어볼이 2개인지 확인하기
	for i in range(n):
		for j in range(n):
			if len(graph[i][j]) > 1: # 2개 이상이면 4개의 파이어볼로 쪼개기
				# 2-1 파이어볼 합치기
				new_m = 0 # 합쳐진 질량
				new_s = 0 # 합쳐진 속력
				# (i,j)에 있는 파이어볼의 개수
				count = len(graph[i][j])
				odd = 0 # 홀수의 개수
				even = 0 # 짝수의 개수
				while graph[i][j]:
					mm, ss, dd = graph[i][j].pop(0)
					new_m += mm
					new_s += ss
					if dd % 2 == 0:
						even += 1
					else:
						odd += 1
				if new_m // 5: # 4개의 파이어볼로 쪼깨지면, 질량이 0인 경우는 소멸
					# 모두 홀수이거나 모두 짝수인 경우
					if even == count or odd == count:
						# 0, 2, 4, 6
						for d in [0,2,4,6]:
							fireball.append([i,j, new_m // 5, new_s // count, d])
					else:
						# 1, 3, 5, 7
						for d in [1,3,5,7]:
							fireball.append([i,j, new_m // 5, new_s // count, d])
			if len(graph[i][j]) == 1: # 그렇지 않고 하나의 파이어볼만 있다면
				fireball.append([i,j] + graph[i][j].pop(0))

ans = 0
for i in fireball:
	# r, c, m, s, d
	ans += i[2] # 남아 있는 파이어볼 질량을 다 더한다.
print(ans)


