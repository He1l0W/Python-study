# 보고서 파일 만들기

for week in range(1,51):
    with open(f"{week}주차.txt", "w", encoding="utf8") as data:
        data.write(f"-- {week} 주차 주간보고 --")
        data.write("\n부서 :")
        data.write("\n이름 :")
        data.write("\n업무 요약 :")