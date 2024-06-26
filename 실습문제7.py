# 부동산 프로그램 만들기

class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시 
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억원", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억원", "2007년")
house3 = House("송파", "빌라", "월세", "500/50만원", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}가지 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()