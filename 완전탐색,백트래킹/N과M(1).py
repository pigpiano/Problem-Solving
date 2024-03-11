
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [] # 수열을 저장할 리스트

def dfs():
	if len(arr) == m:
		# 한 줄에 하나씩, 각 수열은 공백을 구분해서 출력
		# 사전 순으로 증가
		print(' '.join(map(str, arr)))
		return
	else:
		for i in range(1, n+1):
			if i not in arr:
				arr.append(i)
				dfs() # 재귀적으로 다음 숫자 탐색
				# dfs() 함수 호출이 끝나면
				# 다음 탐색을 위해 이전 노드로 돌아간다.
				arr.pop()
dfs()