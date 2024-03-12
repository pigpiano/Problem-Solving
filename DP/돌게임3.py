
import sys
input = sys.stdin.readline

n = int(input())

dp = ["", "SK","CY","SK","SK"]
doll = [1, 3, 4]

for i in range(5, n+1):
	if dp[i-1] == "CY" or dp[i-3] == "CY" or dp[i-4] == "CY":
		dp.append("SK")
	else:
		dp.append("CY")
print(dp[n])

