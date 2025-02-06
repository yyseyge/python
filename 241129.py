#데이터 타입 중 튜플이 있다
#튜플은 리스트와 비슷한데 차이점은 , 리스트는[] 튜플은()이렇게 묶는다
#튜플도 리스트와 마찬가지로 여러 요소를 담는 데이터 타입이다
#리스트는 요소의 삭제 수정 추가 가능하지만 튜플은 안됨.
#튜플은 보통 생성보다는 함수의 결과로 나오는 경우가 많음.
from cgi import print_environ_usage

#튜플의 생성방법
tupule1=() #비어있는 튜플
tupule2=(1,) #튜플은 요소가 하나인 경우 값을 쓰고 뒤에 쉼표를 작성해야함
tupule3=(1,2)
tupule4=(1,2,3)
tupule5=1,2,3 # 괄호 없이 변수에 여러값을 쉼표로 동시에 주면 튜플로 묶여서 변수에 할당됨.
tupule6=('a','b',('aaa','ccc')) #중첩

print(tupule4[0]) #인덱스를 통한 조회 : 읽기
#tupule4[0]=100 #튜플은 인덱스를 통한 값 재할당이 되지 않는다.
#del tupule4[0] #del 키워드를 통한 요소 삭제 안됨

#튜플은 인덱싱 슬라이싱은 사용 가능하다.
print(tupule4[:]) #슬라이싱 사용가능
print(tupule1+tupule3) #더하기 연산 가능
print(tupule1*3) #곱하기 연산 사용 가능
len(tupule2) #len()함수 사용가능
#튜플은 반복문의 대상이 가능하다.
#문자열과 튜플은 인덱싱으로 특정한 값을 수정 삭제 할 수 없다.

#함수
#호출은 사용자가 한다
#매개변수는 함수 안에 선언되어있는 재료를 받는 칸이다
#리턴값은 함수가 호출한 사람한테 뱉어주는 값이다.
#가변 매개변수
#기본 매개변수
int("500") #이 안에 있는 500이라는 문자는 전달인자이다. 함수의 손이 매개변수이다.
#len()함수 쓸수 있는 것은 문자열 리스트 딕셔너리 튜플이있다
# .append()이렇게 함수 앞에 점이 찍히면 전용함수이다. 앞에 대산 전용으로 사용하는 함수이다.
#print()함수는 리턴값이 없기 때문에 어떤 변수에 저장할 수 없다, 즉 x=print()이런거 안됨.

#함수의 구분
#내장함수(파이썬에 기본적으로 구현되어 있는 함수) vs 사용자 정의 함수(우리가 직접 만드는 함수)
#지금까지 우리가 썻던 것은 내장함수이다.

#함수생성방법
"""
def 함수이름():
    함수내에서 실행하려는 문장
"""

#함수 정의하는 방법
def print3():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print3()

#함수의 정의 기준은 반복사용성이 있는지에 따라, 많이 쓸 것 같으면 함수를 생성하여 사용한다.

def print_n_times(value,n):
    for i in range(n):
        print(value)
print_n_times("안녕하세요",5) #매개변수와 인자를 맞춰야함 print_n_times("123",n,n) 이러면 에러남
#가변 매개변수란 변할 수 있는 매개변수이며, 앞에*이 찍힌다.

#def print(n,*v):
    #for i in range(n):
        #for j in v:
            #print(j)
        #print()

#print(3,"안녕하세요","123","2332","ㅎㅎ")

#가변매개변수(*매개변수로 여러값 받는 매개변수)
#기본매개변수(기본값을 가진 매개변수)

#키워드 매개변수
#*value
#n=2
#while True:
    #print("123",end='\n') #키워드 매개변수



def test(a,b=10,c=200):
    print(a+b+c)
test(100)  #210이 출력됨
test(10,20,30) #60출력됨
test(10,c=200) #220출력됨.

def test(a,b=10,c=100):
    if type(a)!=int:
        return
    else:
        return a+b+c
print(test(a=10,b=20,c=30)) #60출력됨
#return은 함수의 탈출 역할을 한다. for,while같은 반복문은 break로 탈출함

#return이 없는 함수의 반환 결과는 None이 나온다.
"""
def 함수명(매개변수):
    변수=초깃값
    실행문
    실행문
    실행문
    :return변수


"""

x=100
x=200
x=200+x
print(x)
def x(x,y): #우리가 지어주는 함수의 이름도 식별자이다. 위에서 x에는 값을 남아놓았는데 여기서 바로 x식별자를 함수명으로 써버려서 밑에서부터는 x가 함수로 취급됨.
    x=5
    x=x+100 #지역변수 #함수 내 변수
    print(x)
x(1000,x)
print(x)
abc=x
aaa=[abc,abc,abc]
#def로 만드는 사용자 정희 함수의 이름도 식별자이다.
#def x() 함수를 정의 후 a=x라는 코드를 작성하면 a()호출 형태로 x함수 호출 가능

def func1():
    print("1번함수 실행")

def xx(l):
    for i in l:
        return i
s=func1
lists=[s,s,s,s,s]
xx(lists)()
print('######################################')
a=["111","123123",1,2,'400']
print(a)
print(id(a)) # id()를 쓰면 실제 메모리 주소가 나온다.
import time
t=str(time.time()).split(".")[0][-1]
def func1():
    print("1번 함수 실행 5보다 크다")
def func2():
    print("5보다 작다")
def xx(l):
    hello="xx함수 내 지역변수" #hello는 지역변수이다. 지역변수는 호출된 지역에서만 실행될 수 있다
    print(hello)
    print(id(hello),"hello의 실제 메모리 위치")
    if int(t)>5:
        return l[0]
    else:
        return l[3]
s=func1
lists=[]
for i in range(10):
    lists.append(s)
xx(lists)()
xx(lists)()
print(id(a))
for i in range(500):
    print(id(i),"주소 실제 데이터:",i) #256까지는 고정된 데이터가 나온다.

#파이썬의 메모리 영역은 크게 힙과 스택으로 분류 가능하다. 그 외에 정적 영역 등이 존재하기도 한다
#각 영역마다 메모리 할당 및 객체 관리 방법이 다르다.

#256까지 정수 형태 데이터가 일정한 주소로 나타난 이유는
#메모리 효율성을 위해 고정된 메모리 영역에 256까지 미리 생성해놓기 때문이다.
#따라서 해당 범위 내 숫자는 이미 생성되어 있는 것을 참조하는 것

#힙영역은 파잉썬에서 동적으로 할당되는 객체를 저장하는 공간
#숫자,문자열,리스트,튜플 등 객체들이 이 힙 영역에 실제로 저장됨.
#동적으로 할당된다는 것을 실행 중에 할당이 된다/해체가 된다의 의미


#데이터 타입
#집합 set
s1=set([1,2,3]) #set라는 형변환 함수를 사용하여 list를 형변환 하면 {1,2,3} 이와같이 출력됨
print(s1)

s2=set("hello")
print(s2) #hello문자열을 set 형변환하니 순서가 바뀌고 l은 하나만 나옴

#set데이터 타입은 중복이 허용되지 안흠
#set데이터 타입은 순서가 없는 데이터 타입이다. unordered
#중복제거 용도로 사용하기도 함. set로 형변환 했다가 다시 다른 데이터 타입으로 반환
#인덱스 사용 불가능 하다. 순서가 없기 때문에
#딕셔너리도 순서가 없다 때문에 인덱스 사용 불가 하다

s1=set([1,2,3])
l1=list(s1)
print(l1)

t1=tuple(s1)
print(t1)
print(t1[0])

#set집합 데이터를 만드는 이유
#교집합, 합집합, 차집합을 구할 수 있다. 두 데이터의 중복된것을 제거하거나 그럴 때 사용,

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합
print(s1&s2) #교집합 구하기 위해서 &이거 사용하던지
print(s1.intersection(s2)) #intersection()함수 사용하면 됨.

#합집합 => 중복은 제거 됨
print(s1|s2) # |이거 쓰면 합집합 구할 수 있음
print(s1.union(s2)) #혹은 union()함수 쓰면 합집합 구할 수 있음
print(s2.union(s1))

#차집합
print(s1-s2)
print(s2-s1)
print(s1.difference(s2))
print(s2.difference(s1))

#집합 자료형에 하나의 값 추가 => 집합 자료형은 인덱스를 쓸 수 없음 따라서 add()함수를 통해 값을 추가 해야함
s1.add(100)
print(s1)
#집합 자료형에 여러 값 추가 => update()함수 사용
s1.update([500,600,700])
print(s1)

#집합 데이터 제거
s1.remove((500))
print(s1)


#사칙연산 계산 함수
# + - / *
#함수이름
#곱하기 mul
#더하기 add
#빼기 sub
#나누기 div
#모든 함수는 두 수를 입력 받아 두수 간의 사칙연산을 수행한다.


#미완성
def add(sum,n):
    print(sum + n)
def mul(sum,n):
    print(sum*n)
def sub(sum,n):
    print(sum - n)
def div(sum,n):
    print(sum/n)

lista=["+","-","*","/","="]
n=0
sum=0
while True:
    x=input("입력하세요")
    if x.isnumeric():
        n=int(x)
    if x==lista[0]:
        sum+=n
        print(sum)

    if x == lista[1]:
        sum-=n
        print(sum)
    if x == lista[2]:
        add(sum, n)
        print(sum)

    if x == lista[3]:

        sum/=n
        print(sum)
    if x == lista[4]:
        add(sum,n)








