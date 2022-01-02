python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python. find("n")) # 5
print(python. find("Java")) # -1 not found
# print(python. index("Java")) # ValueError: substring not found => progrm terminated !!

print(python.count("n")) # 2