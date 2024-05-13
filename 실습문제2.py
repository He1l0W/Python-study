# 스터디 날짜 정하기(3장 p.88)
from random import randint

print("오프라인 스터디 모임 날짜는 매월 " + str(randint(2, 28)) + "일로 선정됐습니다.") # str 형변환자 이용

dDay = randint(2, 28)
print(f"오프라인 스터디 모임 날짜는 매월 {dDay}일로 선정됐습니다.") # f-포매팅 기법 이용

# 셀프 체크 3장

# 섭씨 온도가 30도일 때
c_temp = 30
f_temp = (c_temp * 9 / 5) + 32
print("섭씨 온도 : " + str(c_temp))
print("화씨 온도 : " + str(f_temp))

# 섭씨 온도가 10도일 때
c_temp = 10
f_temp = (c_temp * 9 / 5) + 32
print("섭씨 온도 : " + str(c_temp))
print("화씨 온도 : " + str(f_temp))

