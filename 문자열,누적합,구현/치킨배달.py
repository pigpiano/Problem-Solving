
# 파이썬의 조합 라이브러리 활용
from itertools import combinations

n, m = map(int, input().split())
# 치킨 집
chicken = []
# 하우스
house = []
# 도시 정보 입력받기
graph = []
for i in range(n):
	data = list(map(int, input().split()))
	for j in range(n):
		if data[j] == 1: # 일반 집
			house.append((i,j))
		elif data[j] == 2: # 치킨 집
			chicken.append((i,j))

# 모든 치킨 집 중에서 m개를 뽑는 조합
# 조합을 튜플 형태로 반환해서 리스트로 변환해서 할당
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 구하는 함수
def get_sum(candidate):
	result = 0
	# 모든 집에 대하여
	for hx, hy in house:
		# 가장 가까운 치킨집을 찾기
		temp = 1e9
		for cx, cy in candidate:
			temp = min(temp, abs(hx-cx) + abs(hy-cy))
		result += temp
	return result # 치킨 거리의 합 반환
# 치킨 거리의 합의 최소를 찾아 출력
ans = 1e9
for candidate in candidates:
	ans = min(ans, get_sum(candidate))
print(ans)