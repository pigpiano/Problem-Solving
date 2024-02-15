
ans = '' # 바뀐 문자열을 담을 변수
for i in input():
	# 만약 대문자라면
	if i.isupper():
		if (65 <= ord(i) <= 77):
			ans += chr(ord(i)+13) # A ~ M
		else:
			ans += chr(ord(i)-13) # N ~ Z
	# 만약 소문자라면
	elif i.islower():
		if (97 <= ord(i) <= 109):
			ans += chr(ord(i)+13) # a ~ m
		else:
			ans += chr(ord(i)-13) # m ~ z
	else:
		ans += i
print(ans)


