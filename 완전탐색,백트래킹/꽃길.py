'''
파이썬 조합 라이브러리를 사용한 뒤 완탐으로 해결
모든 꽃잎이 서로 닿지 않고 피어야하므로 씨앗을 심을 수 없는
가장자리를 제외하고, 배열에 꽃잎 좌표를 넣으면서 닿는지 체크
그리고 최소값을 갱신해준다.
'''
from itertools import combinations

n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

# 꽃이 상 하 좌 우로 만개
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 꽃이 안죽으려면 가장자리는 피해서 심어야한다. 안쪽 좌표만
result = []
# result에 담기
for i in range(1, n-1):
	for j in range(1, n-1):
		result.append((i,j))
#겹치는지 확인하기 위해 check 함수 정의
ans = int(1e9)
def check(result_list):
	global ans
	# visited로 꽃이 겹치는 지 확인
	visited = []
	total = 0 # 비용을 비교하기 위한 변수 정의
	for x,y, in result_list:
		visited.append((x,y))
		total += graph[x][y]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 안 겹친다면 total에 더하기
			if (nx,ny) not in visited:
				total += graph[nx][ny]
				visited.append((nx,ny))
			else: # 겹친다면
				return # 바로 함수 종료
	# 최솟값을 구해야하므로
	ans = min(ans, total)

# 그래서 이 result에서 좌표를 골라 3개를 심는 모든 경우를 따져야한다.
# combinations으로 씨앗을 심을 수 있는 좌표를 check에 모두 담기
for i in combinations(result, 3):
	check(i)

print(ans)