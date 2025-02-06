#객체
#객체지향
#추상화
#클래스
#인스턴스
#생성자
#메소드 : 특정 객체는 필드(객체의 속성값이므로 함수가 하니라 변수형태로 사용)와 메소드(객체의 기능으로 함수형태로 사용)로 나뉜다.
from tkinter.font import names


#C언어를 제외한 프로그래밍 언어는 객체 지향 프로그래밍 언어이다.
#객체지향 : 객체를 중심으로 생각해서 작성하는 프로그래밍 방식이다.
#클래스를 기반으로 객체를 만든다.

#객체:속성과 메소드를 갖는것
#클래스: 객체를 만드는 틀

#추상화: 특정 프로그램을 만들때 필요한 요소가 무엇인지를 생각해서 정리하는 것을 추상화라고 한다. 코드를 쓰는 행위가 아닌 머리속에서 분리하는 것

#class Student:
    #def __init__(self): #init()함수는 생성자함수의 호출시 뭐할지를 써주는 함수이다..
        #print("생성") #생성이 7번 출력됨.

#student=Student() # 생성자 함수를 통해 객체를 만든다,
#인스턴스 : 클래스 구조를 통해 만들어진 객체를 의미

#students=[Student(),Student(),Student(),Student(),Student(),Student()]

#p467 예제
#클래스를 선언합니다
class Student: #이 student 클래스에서 만들어진 객체( 인스턴스)의 속성은 5개이고, 메소드는 2개이다.
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
    def __del__(self):
        print("객체 소멸",self.name) #소멸자 함수 , 객체를 소멸시킬때 어떤 행위를 하고 싶으면 쓰는 함수
#학생 리스트를 선언합니다.
students = [Student("윤인성",87,98,88,95),
            Student("연하진",92,98,96,98),
            Student("구지연",76,96,94,90),
            Student("나선주",98,92,96,92),
            Student("윤아린",87,98,88,95),
            Student("윤명월", 87, 98, 88, 95)
            ]
#student 인스턴스 속성에 접근하는 방법
print(students[0].name) #get
print(students[0].korean)
print(students[3].math)
print(students[0].english)
print(students[0].science)

class Student2:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

    def get_sum(self):
        return self.korean + self.math +self.english+self.science
    def get_average(self):
        return self.get_sum()/4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum,self.get_average())
#학생리스트를 선언합니다.
students=[ Student2("윤인성",87,98,88,95),
            Student2("연하진",92,98,96,98),
            Student2("구지연",76,96,94,90),
            Student2("나선주",98,92,96,92),
            Student2("윤아린",87,98,88,95),
            Student2("윤명월", 87, 98, 88, 95)
            ]


class Car:
    def __init__(self,a,b,c,y):
        self.name=a
        self.color=b
        self.company=c
        self.year=y
    def Run(self):
        return "앞으로 갑니다"
    def Stop(self):
        return "멈춥니다"
    def Klaxon(self):
        return "빵빵"
car=[Car("k3","white","kia",2020),
     Car("avante","black","hyundai",2019),
     Car("sportage","gray","kia",2024),
     Car("sonata","silver","hyundai",2010)
    ]
print(car[0].Run())
print(car[2].color)
print(car[3].Klaxon())





class gla:
    def __init__(self,type):
        self.sight=0.2
        self.type=type

myglass=gla("뿔태")

class Bag:
    def __init__(self,name,cat,mat,stuff,who,status):
        self.name=name
        self.cat=cat
        self.mat=mat
        self.inside=stuff
        self.own=who
        self.status=True
    def __del__(self):
        pass
    def open(self):
        print("가방을 열었습니다.")
        self.status=True
    def close(self):
        print("가방을 닫았습니다.")
        self.status=False
    def show_inside(self):
        for i in self.inside:
            print(i)
    def addItem(self,item):
        if self.status==True:
            self.inside.append(item)
            print("{}을 가방에 넣었습니다".format(item))
        else:
            print("가방 닫혀서 물건 못넣음")

b=Bag("책가방","백팩","가죽",[],"이윤서",True)
print(b.name)
if b.own=="이윤서":
    print("이윤서 가방입니다")


if b.status==True:
    b.open()
    b.addItem(myglass)
    b.addItem(gla("뿔테"))
    b.close()

print(b.inside[0].type,b.inside[1].sight)

#ATM(입금(잔액 쌓이기 메소드),출금(잔고 조회해서 출금한느 메소드),송금,종료,)과 ATM사용자, 통장 class 만들기

