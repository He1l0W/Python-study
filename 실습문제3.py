# 비밀번호 만들기(4장 p.117)

site = "http://naver.com"
# site = http://daum.net
# site = http://google.com
# site = http://youtube.com

# http:// 를 공백으로 변환
Pw1 = site.replace("http://", "") 

# 문자열 슬라이싱으로 naver.com 에서 . 이전만 추출
Pw1 = Pw1[:Pw1.find(".")]

# str 형변환자로 type int를 문자열로 변환해 변수에 저장
Pw1 = Pw1[:3] + str(len(Pw1)) + str(Pw1.count("e")) + "!"

# f-포메팅 기법으로 결과값 출력
print(f"{site}의 비밀번호는 {Pw1}입니다.")

# 셀프체크 4장

# 주어진 문장 : the early bird catches the worm.
sentence1 = "the early bird catches the worm."
print(sentence1[0].upper() + sentence1[1:])

# 또다른 방법
# print(sentence1.capitalize())

# 주어진 문장 : Actions Speak Louder Than Words.
sentence2 = "Actions Speak Louder Than Words."
print(sentence2[0] + sentence2[1:].lower())

# print(sentence2.capitalize())


# 주어진 문장 : PRACTICE MAKES PERFECT.
sentence3 = "PRACTICE MAKES PERFECT."
print(sentence3[0] + sentence3[1:].lower())

# print(sentence3.capitalize())


