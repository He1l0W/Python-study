# *8장 입출력 (p.223 ~ 253)

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
print(type(answer))
print(type(int(answer)))
answer = 10
print(type(answer))

print("파이썬", "자바")
print("파이썬" + "자바")
print("파이썬", "자바")
print("파이썬", "자바", sep = ",")
print("파이썬", "자바", "자바스크립트", sep = " vs ")
print("파이썬", "자바", sep = ",", end = "?")
print("무엇이 더 재미있을까요?")

import sys
print("파이썬", "자바", file=sys.stdout)
print("파이썬", "자바", file=sys.stderr)

# 정렬 ljust(), rjust()
scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
    print(subject, score)

scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":")

for num in range(1,21):
    print("대기번호: " + str(num).zfill(3))

# 출력 형태 : farmat()

print("{0}".format(500))
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:_<10}".format(500))

print("{0:,}".format(100000000000000))
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

print("{0:^<+30,}".format(100000000000000))
print("{0}".format(5/3))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))


# 파일 열기/닫기
score_file = open("score.txt", "w", encoding = "utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

# 파일 쓰기
score_file = open("score.txt", "a", encoding = "utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()

# 파일 읽기
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# while 문.ver
score_file = open("score.txt", "r", encoding = "utf8")

while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
    
score_file.close()

# for 문.ver
score_file = open("score.txt", "r", encoding = "utf8")

lines = score_file.readlines()
for line in lines:
    print(line, end="")
    
score_file.close()

# pickle 모듈

import pickle

# wb 모드 = w 쓰기 b 바이너리
profile_file = open("profile.pickle", "wb")
profile = {"이름":"스누피", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)

pickle.dump(profile, profile_file) # profile 정보를 profile_file에 저장
profile_file.close()


profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile 에 불러오기

print(profile)
profile_file.close()

# with 문

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())