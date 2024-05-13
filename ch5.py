# day 6 5장 자료구조(p.123 ~ 141)

# 리스트

subway = [10, 20, 30]
print(subway)

# 값 추가/삽입/삭제하기

subway = ["푸", "피글렛", "티거"]
print(subway)

print(subway.index("피글렛"))

subway.append("이요르")
print(subway)


subway.insert(1, "루") # 인덱스 1 위치에 삽입
print(subway)

# 뒤에서부터 리스트 값 하나씩 출력하고 삭제 (pop 메소드)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 리스트 초기화

subway.clear()
print(subway)

# 중복 값 확인

subway = ["푸", "피글렛", "티거"]
subway.append("푸")
print(subway)
print(subway.count("푸"))

# 리스트 정렬

num_list = [5, 2, 4, 3, 1]
num_list.sort() # 오름차순 정렬
print(num_list)

num_list.sort(reverse=True) # 내림차순 정렬
print(num_list)

num_list.reverse() # 순서 뒤집기
print(num_list)

# sorted() 정렬 리스트 새로 생성
your_list = [1, 3, 2]
new_list = sorted(your_list)
print(your_list)
print(new_list)

# 리스트 확장

mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
print(mix_list)

mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(mix_list)
print(num_list)

# 딕셔너리

cabinet = {3: "푸", 100: "피글렛"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

print(cabinet.get(5))
print("Hi")
print(cabinet[5])
print("Hi")

print(cabinet.get(5, "사용 가능"))
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# in 연산자
print("곰" in "곰돌이")     # True
print("돌이" in "곰돌이")   # True
print("푸" in "곰돌이")     # False

cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet)
cabinet["A-3"] = "티거"
cabinet["C-20"] = "이요르"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys()) # key만 출력
print(cabinet.values()) # values만 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)

# 튜플

menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])

name = "피글렛"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)

(departure, arrival) = ("김포", "제주")
print((departure, ">", arrival))

(departure, arrival) = (arrival, departure)
print((departure, ">", arrival))

# 세트

my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"푸", "피글렛", "티거"}
python = set(["푸", "이요르"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 추가, 삭제
python.add("피글렛")
print(python)

java.remove("피글렛")
print(java)

menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# 1분 퀴즈
# my_list = [1, 2, 3, 3, 3]
# my_set = set(my_list)
# my_list = list(my_set)
# print(my_list)