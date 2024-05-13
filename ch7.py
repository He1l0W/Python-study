# 7장 함수 (p.191 ~ 220)
# def open_account(): # 계좌 개설 함수
#     print("새로운 계좌를 개설합니다.")

# open_account() # open_account()  함수 호출

# def deposit(balance, money): # 입금 처리 함수
#     print(f"{money}원을 입급했습니다. 잔액은 {balance + money}원입니다.")
#     return balance + money # 잔액 반환

# def withdraw(balance, money): # 출금 처리 함수
#     if balance >= money: # 잔액이 출금액 보다 많으면 
#         print(f"{money}원을 출금했습니다. 잔액은 {balance - money}원입니다.")
#         return balance - money # 출금 후 잔액 반환
#     else:
#         print(f"잔액이 부족합니다. 잔액은 {balance}원 입니다.")
#         return balance # 기존값 반환
    
# def withdraw_night(balance, money): # 업무 시간 외 출금
#     commission = 100 # 수수료 100원
#     print(f"업무 시간 외에 {money}원을 출금했습니다.")
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)

# # 출금
# # balance = withdraw(balance, 2000)  # 2000원 출금 시도
# # balance = withdraw(balance, 500)   # 500원 출금 시도

# commission, balance = withdraw_night(balance, 500)
# print(f"수수료 {commission}이며, 잔액은 {balance}원입니다.")

# def profile(name, age, main_lang):
#     print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

# profile("찰리", 20, "파이썬")
# profile("루시", 25, "자바")

# def profile(name, age=20, main_lang="파이썬"):
#     print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

# profile("찰리")
# profile("루시")

# profile("찰리")
# profile("찰리", 22)
# profile("찰리", 24, "자바")


########### 7장 함수 (p.191 ~ 220)
# def open_account(): # 계좌 개설 함수
#     print("새로운 계좌를 개설합니다.")

# open_account() # open_account()  함수 호출

# def deposit(balance, money): # 입금 처리 함수
#     print(f"{money}원을 입급했습니다. 잔액은 {balance + money}원입니다.")
#     return balance + money # 잔액 반환

# def withdraw(balance, money): # 출금 처리 함수
#     if balance >= money: # 잔액이 출금액 보다 많으면 
#         print(f"{money}원을 출금했습니다. 잔액은 {balance - money}원입니다.")
#         return balance - money # 출금 후 잔액 반환
#     else:
#         print(f"잔액이 부족합니다. 잔액은 {balance}원 입니다.")
#         return balance # 기존값 반환
    
# def withdraw_night(balance, money): # 업무 시간 외 출금
#     commission = 100 # 수수료 100원
#     print(f"업무 시간 외에 {money}원을 출금했습니다.")
#     return commission, balance - money - commission



