import sys
input = sys.stdin.readline

# 포켓몬 수와 문제수 입력받기
n, m = map(int, input().split())

# 이름: 번호
str_key = {} # key가 이름인 딕셔너리
# 번호: 이름
int_key = {} # key가 정수인 딕셔너리

# 포켓몬 이름 입력받기
for i in range(1,n+1):
	# 딕셔너리를 읽으면 개행문자로 함께 읽어서 제거해주기위함
	name = input().rstrip()
	# key가 문자열
	str_key[name] = i
	# key가 정수
	int_key[i] = name
# 이제 문제 받고 정답 출력
for i in range(m):
	item = input().rstrip()
	if item.isdigit() == True:
		# 정수면 이름으로 출력
		print(int_key[int(item)])
	else: # 문자열이면 숫자 출력
		print(str_key[item])

