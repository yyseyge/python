#241230 p474
#클래스 추가 구문
#클래스 변수
#클래스 함수
#상속
#isinstance() -> 인스턴스인지 True,False로 확인하는 함수이다.
import random
from zipfile import stringEndArchive64Locator


#from collections.abc import async_generator


class person:
    def __init__(self,name,age,birth):
        self.name=name
        self.age=age
        self.birth=birth

class Stu:
    def __init__(self,num):
        self.num=num

#a=Stu() #a변수에 참조

#students=[Stu(),Stu(),person()] # 식별자가 없이 리스트인덱스 통함 참조

#for i in students:
    #isinstance(i,Stu) #i번째에 나타난 인스턴스가 Stu인스턴스인지 체크할수 있다.찾고자하는 클래스로 만들어진 instance만 찾을 수 있다.

#students.append(Stu(random.Random())) # 동적인 변수
#a=10 # 정적인 변수 , 정적 생성


class H:
    def __init__(self):
        self.name="Human"
    def htest(self):
        pass

class S(H):
    def __init__(self):
        self.age="50"


s=S()
print(s)
print(s.htest()) # S class는 H class를 상속받아서 H class에 있는 메소드를 사용가능 하다.

class Student:
    def study(self):
        print("공부를 합니다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

classroom=[Student(),Student(),Teacher(),Student(),Student()]

for person in classroom:
    if isinstance(person,Student):
        person.study()
    elif isinstance(person,Teacher):
        person.teach()

#isinstance()와 type()방식의 차이는 isinstance는 상속된 인스턴스도 True로 확인해줌
#type은 상속관계확인 불가


#__이름__() 형태의 메소드는 특수한 상황에 자동 호출
x=str(100) #class int안에 __str__ 함수가 호출되어 100이라는 숫자를 문자형태로 바꿔줌


class ss:
    x=100 #클래스 변수 -> 클래스변수는 self가 찍혀있지 않다. 공용
    def __init__(self,name,math,eng):
        self.name=name
        self.math=math
        self.eng=eng
        self.x=100 #객체변수, 인스턴스 변수, self전용 변수 , 필드값, 전용
    def __eq__(self, other):
        return self.eng==other.eng
print(ss.x)#클래스명.클래스변수명

aaa=ss("1번",80,80)
bbb=ss("2번",60,60)
print(aaa==bbb)
str()
int


class Student:
    def __init__(self,name,k,m,e,s):
        self.name=name
        self.k=k
        self.m=m
        self.e=e
        self.s=s

    def get_sum(self):
        return self.k+self.m+self.e+self.s

    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

    def __eq__(self, value):
        return self.get_sum()==value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self,value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

students=[Student("윤인성",87,98,88,95),
              Student("연하진",92,98,96,98),
              Student("구지연",76, 96, 94, 90),
              Student("나선주", 98, 92, 96, 92),
              Student("윤아린", 95, 98, 98, 98),
              Student("윤명월", 64, 88, 92, 92)]

student_a=Student("윤인성",87,98,88,95),
student_b=Student("연하진",92,98,96,98),

print("student_a==student_b=",student_a==student_b)
print("student_a!=student_b=",student_a!=student_b)
print("student_a>student_b=",student_a>student_b)
print("student_a>=student_b=",student_a>=student_b)
print("student_a<student_b=",student_a<student_b)
print("student_a<=student_b=",student_a<=student_b)

class Student:
    count=0

    def __init__(self,name,k,m,e,s):
        self.name=name
        self.k=k
        self.m=m
        self.e=e
        self.s=s

        Student.count+=1
        print("{}번째 학생이 생성되었습니다".format(Student.count))


students1 = [Student("윤인성", 87, 98, 88, 95),
            Student("연하진", 92, 98, 96, 98),
            Student("구지연", 76, 96, 94, 90),
            Student("나선주", 98, 92, 96, 92),
            Student("윤아린", 95, 98, 98, 98),
            Student("윤명월", 64, 88, 92, 92)]
print()
print("현재 생성된 총 학생수는 {}명 입니다.".format(Student.count))

class test:
    name=200 #클래스변수 #공용
    def __init__(self):
        self.name=100 #인스턴스변수 #전용
t=test()
print(t.name) #인스턴스 t의 name필드 #인스턴스일때만 호출가능
print(test.name)#test클래스의 name변수 #누구나 호출가능

tlist=[test(),test]
tlist[0].name #인스턴스 변수 #100출력됨.
tlist[1].name #클래스 변수, 200출력

#클래스 변수 만드는 이유는 count할때나 ,
class sss:
    total=0 #클래스 변수는 객체들의 공통사항을 위한 변수로 쓰인다.
    stulist=[] #self 를 모아놓는 리스트, 클래스 변수로 선언
    age=30
    def __init__(self,name,age):
        self.name=name
        if self.name=="김동현":
            self.age=age
        else:
            self.age=sss.age
        self.age=sss.age
        sss.total+=1
        sss.stulist.append(self)

#x=[sss("김동현"),sss("성진하"),sss("김준섭")]
#print(len(x)) #3출력됨
#print(sss.stulist) # 실제 생성된 객체 메모리 출력

sss("김준섭",1000)
sss("김동현",1)
print(sss.age) #1000출력됨


class stest:
    limit=4 #클래스변수 limit을 이용해서 선착순 3개의 객체만 stestlist에 저장하는 것
    stestList=[]
    def __init__(self,name):
        self.name=name
        stest.limit-=1
        self.ap()
    def ap(self):
        if stest.limit>0: #3번째 생성되는 객체까지는 클래스변수 stestlist에 저장 (append)
            stest.stestList.append(self)
        else:
            self.__del__() #3번째 객체 이후 생성 되는 객체는 강제로 소멸
    def __del__(self):
        print("소멸")
        pass
ll=[]
for i in range(10):
    ll.append(stest("1"))
print(stest.stestList)
print(ll) #객체 10개 다 추가돔.

#학생을 만드는 클래스를 정의하고 해당 클래스는 이름 나이 영어 수학 총 4가지 필드가 있음
#class 변수를 통해서 성이 김씨인 사람 중 영어 점수가 90 이상인 객체만 저장해라

#클래스함수 : self가 쓰이지 않는다. @데코레이터 붙임
#클래스변수 : self가 쓰이지 않는다.

#인스턴스변수: self.필드
#인스턴스함수: self.메소드

class test1:
    def __init__(self):
        pass

    def yyyy(self): #생성자 함수이고 인스턴스 함수이다. 객체만 사용가능. 객체.yyyy이렇게 써야함
        pass

    @classmethod
    def xxxx(cls): #위에 classmethod를 쓰고 함수를 선언하면 (self)대신 (cls)가 나온다, 클래스 함수이다.  클래스.xxxx이렇게 써야함
        pass
t=test1()
test1.xxxx() #가능
#test1.yyyy() #불가능
t.yyyy() #이렇게 써야함

class Student:
    count=0
    students=[]

    @classmethod
    def print(cls):
        print("==학생목록==")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------ ------ ------")

    def __init__(self,name,k,m,e,s):
        self.name=name
        self.k=k
        self.m=m
        self.e=e
        self.s=s
        Student.count+=1
        Student.students.append(self)

    def get_sum(self):
        return self.k+self.m+self.e+self.s

    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}\t".format(self.name,self.get_sum(),self.get_average())

Student("윤인성",87,98,88,95)
Student("연하진",92,98,96,98)
Student("구지연",87,98,88,95)
Student("나선주",92,98,96,98)
Student("윤아린",87,98,88,95)
Student("윤명월",92,98,96,98)
Student("김미화",87,98,88,95)
Student("김연화",92,98,96,98)
Student("박아현",87,98,88,95)
Student("서준서",92,98,96,98)

Student.print()

#491p
#클래스 내부의 프라이빗 private 변수
#public 의 반대

#Public 공용
#Private 내부적으로만 사용하고 비공개 처리한다.
#__변수 => 이렇게 사용하는게 프라이빗 변수
#프라이빗 변수를 직접 조회하려고 하면 attr error 발생.
#클래스의 필드는 직접조회보다는 어떤 함수를 통해 바꾸거나 어떤 함수를 통해 조회하는것이 좋다

class tt:
    def __init__(self):
        self.a=10
        self.b=20
t=tt()
t.a=500 #-> 이렇게 사용하는건 권장사항 아님

class ttt:
    def __init__(self):
        self.__name="김동현"
        self.__b=200

    def rename(self,rename): #set 값 할당 용도
        if type(rename) is str:
            self.__name=rename
        else:
            raise TypeError("이름 재설정은 문자열만 가능합니다.")

    def show_name(self): #get 조회용도
        return self.__name
 #=> 이렇게 쓰는 게 권장사항, 함수를 통해 값을 조회하거나 값을 변경하는 것이 좋다.

tt=ttt()
tt.rename("이윤서")
tt.rename([1,2,3]) # "이름재설정은 문자열만 가능합니다" 타입에러 발생
print(tt.show_name())

class tttt:
    def __init__(self):
        self.__b=200
    @property
    def name(self):
        self.__name="김동현"
    @name.setter
    def rename(self,r): #set 값 할당 용도
        if type(r) is str:
            self.__name=r
        else:
            raise TypeError("이름 재설정은 문자열만 가능")
    def show_name(self): #get조회 용도
        return self.__name

t=tttt()
t.name="성진하"
print()

#클래스기반 언어는 상속 기능이 있음.
class parent:
    def __init__(self):
        self.addr="대전"

class child(parent):
    def __init__(self):
        parent.__init__(self) #-> 자식생성자에서는 부모생성자를 강제로 한번 호출해야함, 이부분이 없으면 에러남
        self.fr=[1,2,3,4,5]

c=child()
print(c.addr)


class myExc(Exception):
    def __init__(self):
        Exception.__init__(self)
raise myExc

#상속 후 오버라이딩의 의미는?
#기본 메소드를 상속받은 후 자식 클래스에서 해당 메소드를 새로운 기능이지만, 같은 함수 이름으로 덮어쓰는 것을 오버라이딩이라고 함.

class student:
    name=10
    @classmethod
    def xx(cls):
        print("클래스메소드호출")
    def __init__(self,name):
        self.name=name
    def x(self):
        print("ㅌ호출")