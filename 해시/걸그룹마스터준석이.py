import sys
input = sys.stdin.readline

# 총 걸그룹 수, 문제 수
n, m = map(int, input().split())

# 딕셔너리 형태 key:팀 이름, value:멤버 이름
zero_arr = {}
# key:멤버 이름, value:팀 이름
one_arr = {}

for _ in range(n):
	# 팀명
	team_name = input().rstrip()
	# 그룹에 속한 인원 수
	num = int(input())
	zero_arr[team_name] = [] # 배열을 하나 만들어준다. 멤버들이 들어감
	for j in range(num):
		# 멤버 이름 입력받기
		personal_name = input().rstrip()
		zero_arr[team_name].append(personal_name)
		one_arr[personal_name] = team_name

# 문제 입력받기
for i in range(m):
	# 팀명 혹은 멤버 이름 입력받기
	name = input().rstrip()
	# 종류 입력받기
	kind = int(input())
	if kind == 0: # 멤버 이름 전부 출력
		for i in sorted(zero_arr[name]):
			print(i)
	else: # 팀 이름 출력
		print(one_arr[name])

