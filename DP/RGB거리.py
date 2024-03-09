# 다이나믹 프로그래밍
n = int(input())

# 각 집마다 비용 입력받기
RGB = [list(map(int, input().split())) for _ in range(n)]

# 두번째 집 부터 확인
for i in range(1, n):
	# 만약 빨간집이 최소라면
	RGB[i][0] = min(RGB[i-1][1],RGB[i-1][2]) + RGB[i][0]
	# 만약 초록집이라면
	RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
	# 만약 파란집이라면
	RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]
# for loop 다 돌고 마지막 출력
print(min(RGB[n-1]))

