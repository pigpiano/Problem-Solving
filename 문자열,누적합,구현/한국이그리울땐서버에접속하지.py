import sys # 입력을 빠르게 받기 위해
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

ans = []
# 초기화, 첫 번째 실행해서 ans 에 담기
ans.append(sum(data[:k]))
# 두 번째 부터 실행하기 때문에 n-k
for i in range(n-k):
	ans.append(ans[i] - data[i] + data[i+k])
print(max(ans))