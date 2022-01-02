try:
  print("나누기 전용 계산기")
  num1 = int(input("첫 번째 숫자 입력 : "))
  num2 = int(input("두 번째 숫자 입력 : "))
  print("{0} / {1} = {2}".format(num1, num2, num1/num2))

except ValueError:
  print("에러! 잘못된 값을 입력하였음")
except ZeroDivisionError as err:
  print(err)
except Exception as err:
  print("알 수 없는 오류 발생")
  print(err)