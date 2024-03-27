import sys
input = sys.stdin.readline

# 사이트 주소의 수, 찾으려는 주소의 수
n,m = map(int, input().split())
arr = {} # 딕셔너리 형태
for _ in range(n):
	address, password = map(str, input().split())
	arr[address] = password

for i in range(m):
	target_address = input().rstrip()
	print(arr[target_address])
