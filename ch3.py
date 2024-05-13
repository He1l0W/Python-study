# day3 3장 연산자(p.69 ~ 92)
# 산술 연산자

print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

print(2 ** 3)   # 제곱
print(10 % 3)   # 나머지
print(10 // 3)  # 몫 type int

# 비교 연산자

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)
print(1 != 3)

# 논리 연산자

print((3 > 0) and (3 > 5))
print((3 > 0) or (3 > 5))
print(not(1 != 3))

# 연산자의 우선순위
print(2 + 3 * 4)
print((2 + 3) * 4)

# 변수 연산

number = 2 + 3 * 4
print(number)
number = number + 2 # (2 + 3 * 4) + 2
print(number)

# 복합 대입 연산자
number += 2
print(number)
number -= 2
print(number) 
number *= 2
print(number) 
number /= 2
print(number) 

number **= 2
print(number) 
number //= 2
print(number) 
number %= 2
print(number) 

# 함수 연산

print(abs(-5))          # 절댓값
print(pow(4, 2))        # 거듭제곱
print(max(5, 12))       # 가장 큰 값
print(min(5, 12))       # 가장 작은 값
print(round(3.14))      # 반올림한 정수
print(round(4.678, 2))  # 소수점 3번째 자리에서 반올림한 값

# math 모듈 연산

from math import *

result = floor(4.99)
print(result)
result = ceil(3.14)
print(result)
result = sqrt(16)
print(result)

# math 모듈 연산 2

import math 

result = math.floor(4.99)
print(result)
result = math.ceil(3.14)
print(result)
result = math.sqrt(16)
print(result)

# ramdom 모듈

from random import *

print(random())
print(random())
print(random())

print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1 이상 46 미만에서 난수 생성
print(randint(1, 45))   # 1 이상 45 이하에서 난수 생성

