print("갤러그 게임 시작")
print("적 비행기 발생")
print("1. 발사 2. 오른쪽이동 3. 왼쪽이동")
number = input("숫자를 입력하세요: ")
print("당신의 입력값? ",number)
# 만약에 1번을 누르면 총알 발사
# 숫자를 ""로 묶어서 숫자를 문자로 만들어 줌
if number == "1":
    print("탕---!")
# 만약에 2번을 누르면 오른쪽
# 문자를 int()로 묶어줌
if int(number) == 2:
    print("오른쪽으로 이동")
# 만약에 3번을 누르면 원쪽
if number == "3":
    print("왼쪽으로 이동")