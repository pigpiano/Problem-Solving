
arr = []
for i in range(9):
	arr.append(int(input()))

one = 0
two = 0

for i in range(len(arr)):
	for j in range(i+1, len(arr)):
		if sum(arr) - (arr[i] + arr[j]) == 100:
			one = arr[i]
			two = arr[j]
			arr.remove(one)
			arr.remove(two)
			break
for i in sorted(arr):
	print(i)
