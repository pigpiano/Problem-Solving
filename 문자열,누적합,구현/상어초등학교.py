
n = int(input())
# 정보를 담을 리스트 만들기
data = [[0] * n for _ in range(n)]
students = []
for _ in range(n**2):
	# 학생의 번호, 좋아하는 학생의 번호
	students.append(list(map(int, input().split())))
# 상 하 좌 우 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for student in students:
	available = [] # 해당 학생의 (행,열,좋아하는 학생의 수, 빈칸 수) 저장할 배열
	for i in range(n):
		for j in range(n):
			# 빈자리가 있다면
			if data[i][j] == 0:
				prefer, empty = 0,0 # 먼저, 초기화 0
				# 4가지 방향 확인
				for k in range(4):
					nx = i + dx[k]
					ny = j + dy[k]
					# 범위내에 있다면
					if (0 <= nx < n) and (0 <= ny < n):
						# 좋아하는 학생이 주위에 있다면 더해준다.
						if data[nx][ny] in student[1:]:
							prefer += 1
						# 빈자리가 있다면 더해준다.
						if data[nx][ny] == 0:
							empty += 1
				# available 배열에 (행, 열, 좋아하는 사람 수, 빈칸 수)
			    # 를 모두 더 해준다.
				available.append((i,j,prefer,empty))
	# 정렬해준다.
	# 1. 좋아하는 사람 많은 수 2. 빈칸 많은 수 3. 행의 번호가 낮은 순
	# 4. 열의 번호가 낮은 순
	# -붙으면 내림차순, +이면 오름차순
	available.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))
	# 학생을 배치한다.
	data[available[0][0]][available[0][1]] = student[0]

# 최종 결과 변수 -> 학생 만족도 합
ans = 0
# 각 만족도
score = [0, 1, 10, 100, 1000]
students.sort() # 학생을 정렬해서 순서대로 만족도를 계산한다.
# 만족도 계산은 위에서 자리 배치가 모두 끝난 후 진행 한다. 이제 만족도 계산하기
for i in range(n):
	for j in range(n):
		count = 0 # 주변에 좋아하는 학생의 수
		for k in range(4):
			nx = i + dx[k]
			ny = j + dy[k]
			if (0 <= nx < n) and (0 <= ny < n):
				# 인접칸에 좋아하는 학생이 있다면
				if data[nx][ny] in students[data[i][j] - 1]:
					count += 1 # 주변에 좋아하는 학생 수에 따라 더한다.
		ans += score[count]
print(ans)
