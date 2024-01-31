'''
1 <= M <= 13 -> 최대 13개에서 M개를 선택하는 조합
13 Combination M < 100,000, 즉 완탐가능
치킨집 중에서 M개를 고르는 모든 경우에 대해서 치킨 거리의
합을 계속하여, 치킨 고리의 최솟값을 구하자.
'''
from itertools import combinations
n,m = map(int, input().split())
graph = []
# 치킨의 위치를 담는 리스트
# 집의 위치를 담는 리스트
h, c = [], []
for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(n):
		if graph[i][j] == 1: # 집
			h.append((i,j)) # 집의 좌표
		elif graph[i][j] == 2: # 치킨 집
			c.append((i,j)) # 치킨 집의 좌표

# 모든 치킨집 중에서 m개를 고르는 모든 경우
# 선택된 치킨 집들의 좌표를 담은 리스트를 반환
candidates = list(combinations(c, m)) # 리스트 형태로 전환해서 반환
# for i in candidates:
# 	print(i)
#치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
	ans = 0
	# 모든 집에 대하여
	for hx,hy in h:
		# 가장 가까운 치킨집 찾기
		temp = int(1e9) # 거리 비교를 위한 변수
		for cx, cy in candidate:
			temp = min(temp, abs(hx-cx) + abs(hy-cy))
		# 가장 가까운 치킨집까지의 거리 더하기
		ans += temp
	return ans

# 치킨 거리의 최소합을 출력
result = int(1e9)
for i in candidates:
	result = min(result, get_sum(i))

print(result)