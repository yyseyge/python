#342p
from traceback import print_tb


#스택 , 힙
#메모리영역

def primitive_change(b):
    b=20 #->지역변수

a=10 #-> 전역변수
print(a) #-> 전역변수 출력,10출력
primitive_change(a) #->
print(a) #10출력

def object_change1(d):
    d.append(4)
c=[1,2,3]
print(c) # [1,2,3]출력됨
object_change1(c)
print(c) #[1,2,3,4]출력됨

def object_change2(f):
    f=[4,5,6]
e=[1,2,3]
print(e) #->{1,2,3]출력됨
object_change2(e)
print(e) #->[1,2,3]출력됨

a=10
def x(): #-> a가 바라보는 것을 출력할때는 문제 없음, 근데 a가 바라보는 주소10말고 다른주소20을 봐 라고 할땐 global써줘야함
    global a
    print(a) #->10나옴
    a=20

x()
print(a) #->20나옴

b=[1,2,3]
def xx(): #-> 글로벌에 있는 b는 힙에 있는 [1,2,3]을 바라보고 있다.지역에 있는b도 글로벌에 있는 b가 바라보고 있는 [1,2,3]을 보고 있음, 스택에 있는 값이 아닌 힙에 있는 [1,2,3]에 4를 추가하는 것이므로 가능함,
                #글로벌 b자체의 값을 바꾸는게 아닌 바라보고 있는 object의 값을 추가하는것이기 때문에 가능, 만약 b자체한테 너 [1,2,3]말고 다른 주소인[4,5,6]쳐다봐 하는것은 global써야함.
    print(b)
    b.append(4)
xx()
print(b)

c=[1,2,3]
def xxx(): #-> 지역변수에 있는 c가 글로벌에 있는 c한테 [1,2,3]말고 [4,5,6]을 바라보라고 시키는것은 안됨, 그럼 글로벌 써줘야됨.

    c=[4,5,6]
xxx()
print(c) #[1,2,3]나옴, 만약에 함수안에 global c를 선언해주면 [4,5,6]으로 출력됨
#전역변수, 지역변수는 스택에 저장되고, object는 힙에 저장된다. 리스트는 object이므로 힙엥 ㅣㅇㅆ음


#하노이문제
#x는 원판

#재귀함수는 if문이 최소 두개가 있다, 하나는 함수가 끝나는 if문 하나는 그것이 아닐시 다시 함수 호출해서 재귀시키는 if문

#하노이탑 문제(재귀호출사용)
import time

def draw(): # 타워 그리기
    print(f"count: {count}")

    output = ""
    for i in range(height - 1, -1, -1):
        for t in tower:
            if len(t) <= i:
                output += " " * (height + 2)
            else:
                output += "*" * t[i] + " " * (height + 2 - t[i])
        output += "\n"
    print(output + "──────────────────────────────")

import time

def hanoi_tower(n, a, b, c): # 개수, 시작, 경유, 도착
    global count

    if n == 1:
        tower[c].append(tower[a].pop()) # a > c
        count += 1
        draw()
        time.sleep(interval)
        return

    hanoi_tower(n - 1, a, c, b) # 맨 아래 빼고 나머지 a > b

    tower[c].append(tower[a].pop()) # 맨 아래거 a > c
    count += 1
    draw()
    time.sleep(interval)

    hanoi_tower(n - 1, b, a, c) # 맨 아래 빼고 나머지 b > c
    return

height = 2 # 높이
count = 0 # 이동 횟수
interval = 1 # 시간 간격
tower = [[i for i in range(height, 0, -1)], [], []]

draw() # 처음 상태 출력
time.sleep(interval)

hanoi_tower(height, 0, 1, 2) # tower[0] tower[1] tower[2]

#p360
#예외처리
#1.조건문을 사용하여 예외를 처리 -> 내가 예상하고 있는 오류
x=input("X메뉴번호를 입력하세요")
if x.isdigit():
    x=int(x)

#2.try except 구문을 이용하는 방법
try:
    y=int(input(" Y메뉴번호 입력하세요."))
except:
    #예외발생했을때 실행할 코드
    pass


try:
    f=open("info22222.txt",'w') #-> info2222라는 파일을 f라는 객체에 담아놓는다
    print(f.mode)
    f.close()
    print(f.closed)
except Exception as e:
    print(e)

try:
    file=open("info22222.txt",'w')
    예외.발생해라() #-> . 찍어서 사용했으니까 예외는 객체인데, 예외라는 객체 만든적 없고, 발생해라는 ()있으니까 함수인데 발생해라라는 함수 만든적 없어서 오류난다.ㅣ
except:
    print("오류가 발생했습니다.")
finally: #-> try실행하다가 오류생겨서 except실행해도 꼭 finally는 들려서 기능 실행해야함
    file.close()

def test():
    print("1")
    try:
        print("2")
        return #-> return만나면 탈출함 , return밑에 는 못 읽음 . return은 함수를 탈출 시킴, 그래서 "함수 내부 마지막 줄"을 출력하지 못함. 대신 finally는 무조건 출력하고 나가야함 .

        print("3")
    except:
        print("exc")
    finally:
        print("final")
    print("함수 내부 마지막 줄 ")
test()



