'''
inorder 순회를 반대로 하면 된다.
중위 순회 순서: 왼쪽 자식 노드 -> 현재 노드 -> 오른쪽 노드
'''

k = int(input())
inorder = list(map(int, input().split()))

# 순회 순서를 리스트에 담는다.
ans = [[] for _ in range(k)]

def dfs(inorder, depth):
	# root 노드 index를 찾는다.
	mid = len(inorder) // 2 # index of root node
	# 해당 깊이에 해당하는 노드를 추가
	ans[depth].append(inorder[mid])
	#재귀는 기저사례를 항상 고려
	if len(inorder) == 1:
		return
	# 재귀적으로 방문
	dfs(inorder[:mid], depth+1)
	dfs(inorder[mid+1:], depth+1)
dfs(inorder, 0) # 깊이는 0부터 시작
for i in ans:
	print(*i)
