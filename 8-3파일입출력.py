# score_file = open("score.txt", "w", encoding="utf8") # w = write
# print("수학 : 50", file=score_file)
# print("영어: 100", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a = append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r = read
# print(score_file.read())  # read all file on one time
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r = read
# print(score_file.readline(), end="")  # read one line, 줄발꿈 없음
# print(score_file.readline())  # read one line
# print(score_file.readline(), end="")  # read one line, 줄발꿈 없음
# print(score_file.readline())  # read one line
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # r = read
# while True:
#   line = score_file.readline()
#   if not line:
#     break
#   print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r = read
lines = score_file.readlines() # 모든 화일을 리스트형태로 저장
for line in lines:
  print(line, end="")
score_file.close()