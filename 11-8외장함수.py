# google > "list of python mudules" > https://docs.python.org/3/py-modindex.html

#glob (windows: dir) 경로내의 폴더/파일 목록 조회
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 화일

# os : o/s에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리


# folder = "sample_dir"

# if os.path.exists(folder):
#   print("이미 존재하는 {0} 폴더 입니다".format(folder))
#   os.rmdir(folder)
#   print(folder, "폴더를 삭제하였습니다.")

# else:
#   os.makedirs(folder) # folder생성
#   print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간 관련 함수
# import time
# # print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2021-12-11 20:52:56
# print(time.strftime("%y-%m-%d %H:%M:%S")) # 2021-12-11 20:52:56

import datetime
# print("오늘 날짜는 ", datetime.date.today()) # 오늘 날자는  2021-12-11

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜
td = datetime.timedelta(days=100) # 100d일 저장
print("오늘 부터 100일 후는 ", today + td) # 오늘 부터 100일 후