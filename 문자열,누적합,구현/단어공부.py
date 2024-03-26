
s = input().lower() # 대소문자 구분 X, 출력만 대문자로!
# 우선 각 문자를 중복 없이 따로 추출
s_list = list(set(s))
# print(s_list) ['a', 'z']
# 각 문자의 빈도를 담을 배열
cnt = []
for i in s_list:
	num = s.count(i)
	cnt.append(num)
# print(cnt) [1, 2]
# 그리고 이제 최단 빈도수인지 확인
if cnt.count(max(cnt)) > 1:
	print("?")
else:
	print(s_list[cnt.index(max(cnt))].upper())