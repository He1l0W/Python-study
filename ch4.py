# day4 4장 문자열 다루기(p.95 ~ 105)

# 문자열이란

sentence1 = '나는 소년입니다'
print(sentence1, type(sentence1))

sentence2 = "파이썬은 쉬워요"
print(sentence2, type(sentence2))

sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

# 문자열 슬라이싱

jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7])

print("연 : " + jumin[0:2]) # 0부터 2 직전까지(0, 1)
print("월 : " + jumin[2:4]) # 2부터 4 직전까지(2, 3)
print("일 : " + jumin[4:6]) # 4부터 6 직전까지(4, 5)

print("생년월일 : " + jumin[:6])
print("주민등록번호 뒷자리 : " + jumin[7:])
print("주민등록번호 뒷자리(뒤에서부터) : " + jumin[-7:])

# 함수로 문자열 처리하기

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1:3].islower())
print(python.replace("Python", "Java"))

find = python.find("n")
print(find)
find = python.find("n", find + 1)
print(find)
find = python.find("Java")
print(find)

index = python.index("n")
print(index)
find = python.index("n", index + 1)
print(index)
find = python.index("n", 2, 6)
print(index)
find = python.index("n", "Java")
print(index)

print(python.count("n"))
print(python.count("v"))

print(len(python))

# 문자열 포매팅

print("ab" + "ab")
print("ab", "ab")

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("백문이 불여일견\n백견이 불여일타")

print("저는 '나도코딩'입니다")
print('저는 "나도코딩"입니다')

print("저는 \"나도코딩\"입니다")
print("저는 \'나도코딩\'입니다")

print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace")

print("Red Apple\rPine")
print("Redd\bApple")
print("Red\tApple")

