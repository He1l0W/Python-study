# 5장 p.152 
# 실습 문제 : 당첨자 뽑기

from random import shuffle, sample

usr_lst = list(range(1, 21))
shuffle(usr_lst)

chicken = sample(usr_lst, 1)
usr_lst.remove(chicken[0])
coffee = sample(usr_lst, 3)

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {chicken[0]}")
print(f"커피 당첨자 : {coffee}")
print("-- 축하합니다! --")
