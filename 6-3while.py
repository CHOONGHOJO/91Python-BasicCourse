# customer = "토르"
# index = 5
# while index >= 1:
#   index -= 1
#   print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다".format(customer, index))
#   if index == 0:
#     print("커피는 폐기되었습니다.")

customer = "Tor"
person = "unknown"

while person != customer :
  print("{0}님, 커피가 준비되었습니다.".format(customer))
  person = input("이름이 어떻게 되세요?")