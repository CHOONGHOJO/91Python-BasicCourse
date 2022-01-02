cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(3))
# print(cabinet[5]) # KeyError: 5 program terminated
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet) # True

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 값
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 값 지우기
del cabinet["A-3"]
print(cabinet)

# key, value
print(cabinet.items())
# key
print(cabinet.keys())
#  value
print(cabinet.values())

# data clear
cabinet.clear()
print(cabinet)