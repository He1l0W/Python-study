# *8장 클래스 (p.259 ~ 323)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0}유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
soldier1 = Unit("보병", 40, 5)
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크", 150, 35)

stealth1 = Unit("전투기", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage))

stealth2 = Unit("업그레이드한 전투기", 80, 5)
stealth2.cloaking = True
if stealth2.cloaking == True:
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))
    

# 메서드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp # 체력
        self.damage = damage # 공격력

    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1}방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage) :
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp)) #남은 체력 출력
        if self.hp <= 0: # 남은 체력이 0이하면
            print("{0} : 파괴됐습니다.".format(self.name)) #유닛 파괴 처리

flamethrower1 = AttackUnit("화염방사병", 50, 16)
flamethrower1.attack("5시") # 5시 방향으로 공격 명령
flamethrower1.damaged(25) # 25만큼의 공격 2번 받음
flamethrower1.damaged(25) # 남은 체력은 0

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): #Unit클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
        self.damage = damage

    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다.[공격력 {2}]".format(self.name, location, self.damage ))
    
    def damaged(self, damage): # damage만큼 유닛 피해
        print("{0} : {1}만큼 피해를 입었습니다." .format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하라면
            print("{0} : 파괴됐습니다." .format(self.name)) # 유닛 파괴 처리

flamethrower1 = AttackUnit("화염방사병", 50, 16) 
flamethrower1.attack("5시") 
flamethrower1.damaged(25) 
flamethrower1.damaged(25) 

class Flyable:
    def __init__(self, flying_speed): # 비행 속도
        self.flying_speed = flying_speed

    def fly(self, name, location): # 유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): # Unit 클래스의 move() 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

interceptor = FlyableAttackUnit("요격기",200, 6, 5)
interceptor.fly(interceptor.name, "3시")

hoverbike = AttackUnit("호버 바이크", 80, 10, 20)

spacecruiser = FlyableAttackUnit("우주 순양함", 500, 3, 25)

hoverbike.move("11시") 
spacecruiser.move("9시")

# PASS

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
    
# 보급고 : 건물유닛,  1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("보급고", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass
game_start() #[알림] 새로운 게임을 시작합니다.
game_over()


# PASS 부분 추가본
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) # 추가한 부분
        super().__init__(name, hp, 0) # 부모 클래스 접근. self 없이 사용
        self.location = location # 추가한 부분
    
# 보급고 : 건물유닛,  1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("보급고", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass
game_start() #[알림] 새로운 게임을 시작합니다.
game_over()


class Unit:
    def __init__(self):
        print("Unit 생성자")
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
class FlyableUnit(Unit, Flyable):
# class FlyableUnit(Flyable,Unit): # 상속순서 변경
    def __init__(self):
        super().__init__(self)
        
# 수송선
troopship = FlyableUnit()

# class Tank(ATtackUnit):
#     siege_developed = False #시지모드 개발여부, 클래스변수로 정의
#     def __init__(self):
#         AttackUnit.__init__(self,"탱크",150,35,1)
#         self.siege_mode = False





# #게임 시작
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# #게임 종료
# def game_over():
#     print("Player : Good Game")
#     print("[Player]님이 게임에서 퇴장했습니다.")

# #실제 게임 진행
# game_start()

# #보병 3기 생성
# # so1 = Soldier()
# # so2 = Soldier()
# # so3 = Soldier()

# #탱크 2기 생성
# ta1 = Tank()
# ta2 = Tank()

# #전투기 1기 생성
# # st1 = Stealth()

# #유닛 일괄 관리(생성된 모든 유닛 추가)
# attack_units = []
# attack_units.append(so1)
# attack_units.append(so2)
# attack_units.append(so3)
# attack_units.append(ta1)
# attack_units.append(ta2)
# attack_units.append(st1)

# #전군 이동
# for unit in attack_units:
#     unit.move("1시")

# #탱크 시지 모드 개발
# Tank.siege_developed = True
# print("[알림] 탱크의 시지 모드 개발이 완료되었습니다.")

# #공격 모드 준비(보병 : 강화제, 탱크 : 시지모드, 전투기 : 은폐모드)
# for unit in attack_units:
#     if isinstance(unit, Soldier): #Soldier클래스의 인스턴스라면 강화제
#         unit.booster()
#     elif isinstance(unit, Tank): #Tank클래스의 인스턴스이면 시지모드
#         unit.set_siege_mode()
#     elif isinstance(unit, Stealth): #Stealth클래스의 인스턴스이면 은페모드
#         unit.cloaking()

# #전군 공격
# for unit in attack_units:
#     unit.attck("1시")

# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,20)) #피해는 무작위로 받음(5~20)

# #게임 종료
# game_over()