jumin = "211210-3234567"

print("주민번호: " + jumin[0:14])

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[0:6]) # 0부터 2 직전까지
print("생년월일 : " + jumin[:6]) # 0부터 2 직전까지
print("뒤 7자리 : " + jumin[7:14]) # 7부터 마지막까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 마지막까지

print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째 끝까지