
a,b,c = map(int, input().split())

arr = [0] * 101
for i in range(3):
	start, end = map(int, input().split())
	for j  in range(start, end): # 시작 포함 끝 미포함
		arr[j] += 1
#print(arr)
ans = 0
for i in arr:
	if i == 1:
		ans += a
	elif i == 2:
		ans += 2 * b
	elif i == 3:
		ans += 3 * c
print(ans)

