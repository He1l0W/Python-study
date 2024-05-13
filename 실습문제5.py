# 6장 p.185 
# 실습 문제 : 택시 승객 수 구하기

from random import *

passenger = 0
for i in range(1, 50):
    travel_time = randint(5, 50)
    if 5 <= travel_time <= 15:
        print(f"[0] {i}번째 손님 (소요시간 : {travel_time}분)")
        passenger += 1
    else:
        print(f"[] {i}번째 손님 (소요시간 : {travel_time}분)")
        
print(f"총 탑승객 : {passenger}")
        