#변수
#변수에는 모든 자료형의 값을 저장할 수 있다.
#변수의 선언
#변수의 생성
#변수는 값을 담아놓기 위한 저장장소이다.
from os.path import split
from traceback import print_tb

x=10
a=20
abc=30

#복합 대입 연산자
# a+=10  -> a=a+10

a=100
print(a) #100

a=a+10 #a값이 갱신됨, 110
print(a) #110

#a값이 110에서 바꾸고 싶지 않다면 b=a로 다른 변수를 써서 담아놓는다.

#복합대입연산자 a**10 -> a=a**10

number = 100
number += 10
number += 20
number += 30
print("number :", number)


#데이터타입
# 1. 숫자 (사용가능한 연산자 +-*/ % ** //)
# 2. 문자열 (사용가능합 연산자 + *)

#문자열에 대한 복합 연산자에서는 +=이랑 *= 사용 가능함.
#문자열에 += 은 문자열 연결 후 대입
#문자열에 *= 은 문장려 반복 후 대입
Str="안녕하세요."
Str+="이윤서입니다."
Str+="잘부탁드립니다."
print("str :", Str)
#str은 변수명으로 사용하면 안됨 Str이렇게 변수명 사용해야함. 즉 함수를 변수명으로 사용하면 안됨.

#str="안녕하세요"
#str*=3
#print("str :", str)

#사용자 입력 input()
#식별자 뒤에 괄호 +> 함수
#input() #사용자로부터 입력을 받아 활용하는 방법
#name=input("이름을 입력하세요 >")
#print(name,name,name)
#input()함수로 입력받은 값은 항상 문자열이고, return값을 남긴다.
#문자열을 숫자로 변환하는 과정 필요
#input을 통해서 두 수(두번)를 입력받아서 합을 출력하는 코드 작성(캐스트 형 변환)
#int_a = int(input("입력a"))
#int_b = int(input("입력b"))
#print(int_a + int_b)
#한줄로 바꾸면 ->
#print(int(input("입력a"))+int(input("입력b")))
#int() : 문자열을 숫자(정수)로 변환
#float() : 문자열을 숫자(실수)로 변환

#Strint_a = input("입력a")
#int_a = int(Strint_a)
#이걸 한줄로 바꾸기
#int_a = int(input("입력a"))

#float_a = float(input("float변환"))
#print(float_a)
#print(float_a+100)
#정수와 실수의 + 결과는 실수형
#실수와 실수의 + 결과는 실수형
#정수와 정수의 + 결과는 정수형


print(type(str(int(input("str 함수 테스트")))))


#inch단위를 cm로 변경하기
inch = int(input("inch 단위숫자를 입력하세요"))
cm = inch * 2.54
print(inch,"inch는 cm단위로",cm,"cm입니다.")

#사용자 입력으로 키와 체중(kg)을 입력 받아서 BMI결과 출력 코드
#BMI = 체중(kg) / 신장(m)의 제곱
#a=float(input("키"))
#b=float(input("체중"))
#BMI = b/a**2
#print("BMI : ", BMI)

#원의 반지름을 입력받아 원의 둘레와 넓이 구하는 코드
#둘레 : 2*원주율*반지름
#넓이 : 원주율 *반지름*반지름
r = int(input("원의 반지름을 입력하세요"))
s = 3.14*r*r
l = 2*3.14*r
print("원의 둘레는 ",l,"입니다")
print("원의 넓이는",s,"입니다")

a = input("문자열입력")
b = input("문자열 입력")
print(a,b)
#a=안녕하세요
#b=아침입니다
c=a
a=b
b=c
print(a,b)
#--------------------------------
#"안녕하세요".find() #문자열 전용 함수
#print() #문자열 숫자 뭐든 쓸 수 있는 함수
#input() # 아무거나 쓸 수 있는 함수
# . 찍고 사용하는 함수는 . 앞 데이터 형태 전용 함수라고 생각

#문자열 format()함수
#변수를 대상으로 format함수를 많이 쓴다.
xx="{}".format(10)
print(xx)  #format함수는 format안에 들어있는것을 문자로 바꿔서 {}안에 넣어주는 함수
x= "{}{}".format(20,30)
print(x) # 중괄호 갯수와 format함수안의 갯수는 같아야함

age = int(input("나이를 입력하세요"))
x = "당신의 나이는{}입니다.".format(age)
print(x)

#format 함수로 숫자를 문자열로 변환하기
a="{}만원".format(5000)
b="파이썬 열공해서 연봉{}만원 만들기".format(5000)
c="{}{}{}".format(3500,4500,5000)
d="{}{}{}".format(1,"문자열",True)

print(a)
print(b)
print(c)
print(d)

#BMI 계산에 format함수 활용
#사용자 입력한 이름/키/체중 "XX님의 BMI는 ~~입니다"
#BMI = 체중(kg) / 신
#
# 장(m)의 제곱

name=input("이름을 입력하세요")
a=float(input("키를 입력하세요"))
b=float(input("체중을 입력하세요"))
bmi = b/a**2

c="{}님의 BMI는{}입니다".format(name,bmi)
print(c)
#indexError -> 문자열의 format사용시 {}의 칸 수와 format함수의 재료 수 맞출 것
print()

a="{:d}".format(52)
b="{:5d}".format(52)
c="{:10d}".format(52)
d="{:05d}".format(52)
e="{:05d}".format(-52)
print(a)
print(b)
print(c)
print(d)
print(e)

print("조합하기")
f="{:+5d}".format(52)
g="{:+5d}".format(-52)
h="{:=+5d}".format(52)
i="{:=+5d}".format(-52)
j="{:+05d}".format(52)
k="{:+05d}".format(-52)

print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

print("hello".upper())#문자열의 알파벳을 대문자로
print("HELLO".lower())#문자열의 알파벳을 소문자로

#파괴적함수와 비파괴적함수
#upper lower은 비파괴적 함수이다. 원본을 건들지 않음
test = "test"
res = test.upper()
print(res)
print(test)
#함수 구분 여부는 다양하다 1.재료가 필요하나안필요하나 2.파괴적이냐 비파괴적이냐 3.내장형이냐 사용자생성형이냐


#strip 함수는 공백제거 역할함.
a="""    안녕하세요
     문자열의 함수를 알아봅시다.
     """
print(a)
print(a.strip())

#문자열 구성 파악
#isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어 있는지 파악
print("abc151".isalnum()) #true
print("안냥".isalnum()) #true 그 이유는 한글도 알파벳으로 인식함
print("@#4".isalnum()) #False

#isdigit()은 만약에 사용자가 번호입력중에 010998.54 실수로 공백과 특수문자 쓰면 오류남 그때 isdigit()함수 써야함
#v=int(input("번호를 입력하세요"))
#print(v)
print("10".isdigit()) # True

#문자열 찾기 find
#문자열 내부에 특정 문자가 어디에 위치하는지 확인 하는 용도
a = "안녕안녕하세요".find("안녕")
print(a)
b="안녕안녕하세요".rfind("안녕")
print(b)

#문자열과 in 연산자 -> 단순히 포함 되는지 안되는지만 알 수 있음 , find는 위치알려줌
print("안녕"in"안녕하세요") #True

#문자열 자르기 split()
a="10 20 30 40 50".split(" ")
print(a)
print(type(a)) # list타입이다.

b="안녕하세요반가워요잘지내요안녕이요".split("요")
print(b) #['안녕하세','반가워','잘지내','안녕이']라고 출력됨

#f-문자열
print("3+4=" + str(3+4))
print("3+4={}".format(3+4))

#숫자를 문자열로 바꾸는 방법 3가지
#1.print("3+4=" + str(3+4))
#2.print("3+4=print(f'3+4={3+4}'))
#3.print(f'3+4={3+4}')

print(f'{10}')
print("{}".format(10))
print(f'3+4={3+4}')

#구의 부피와 겉넓이
r=int(input("구의 반지름을 입력해주세요"))
pi = 3.141592
v=(4/3)*pi*r**3
s=4*pi*r**2

print("구의 부피는 v입니다.",v)
print("구의 넓이는 s입니다.",s)

#피타고라스의 정리
u=float(input("밑변의 길이를 입력하세요"))
h=float(input("높이의 길이를 입력하세요"))
c=(u**2 + h**2)**(1/2)
print("빗변의 길이는 c입니다", c)
#----------------------------------------------혹은
c=(float(input("밑변의 길이를 입력하세요"))**2 + float(input("높이의 길이를 입력하세요"))**2)**(1/2)
print("빗변의 길이는 c입니다", c)

a=int(input("첫번째 숫자: "))
b=int(input("두번째 숫자: "))
c=a+b
print("{}+{}={}".format(a,b,c))

print("==조건문시작==")
#연산자(+*-/)
#대입연산자(=)
#복합대입연산자(=+,-=,*=,/=)
#비교연산자(== != < > <= >=) -> 비교 연산자가 사용된 식은 항상 true false값을 뱉는다
#논리연산자 (not,and,or)

#비교연산자(조건식)
print(10==100) #false
print(10<100) #true
print(100<=100) #true
print("가방"=="가방") #true
print("가방"<"하마") #true 그이유는 사전에 먼저 나오는 단어가 작다
x=25
print(10<x<30) #true

#논리연산자
#and -> A and B 는 A와 B 모두 참이어야 결과적으로 참
#or -> A or B 는 A B 둘중 하나만 참이면 참
#not -> not A는 A의 결과를 반대로 나타냄

#not 연산자 조합하기
x=10
under_20=x<20 #비교 연산자가 사용된 식은 항상 true, false값을 뱉는다.

print("under_20:",under_20)
print("not under_20:",not under_20)

print("==if문 사용==")
if True: # if 뒤에는 꼭 True/false가 나오는 식을 넣는다.
    print("참입니다") #이 print는 if가 참일때 실행되는 실행문이다.
if 100==100:
    print("위 if문에 소속")
    print("if 조건식이 참이면 실행됨")
    print("프린트들 = if 내부 실행문")
    print("위 if문 조건식 결과가 false라면 진입 자체 X")
    if 100==100: #레이어1은 레이어0의 자식
        print("123") #레이어2는 레이어1의 자식

#사용자 입력을 받는다
#입력받은 값이 숫자로만 구성되어 있다면
#"숫자입니다"라는 텍스트와
#실제 숫자 타입으로 변환해서 입력받은 값에 30을 더한 값을 한줄에 동시에 출력합니다


#num = (input("숫자를 입력해 주세요"))
#if num.isnumeric():
    #print("{}{}".format("숫자입니다",int(num)+30))
#if num.isalpha():
    #print("숫자로 다시 입력하세요")

num = (input("숫자를 입력해 주세요"))
if num.isdigit():
    print("{}{}".format("숫자입니다",int(num)+30))
if num.isalpha():
    print("숫자로 다시 입력하세요")
if num.isalnum():
    print("문자가 섞여있습니다")

#짝수 홀수 구분법
x=int(input("입력"))
if x%2==1:
    print("홀수입니다")
if x%2==0:
    print("짝수입니다")

print("int형변환의 특징:소숫점을 날린다")
x=int(input("입력"))
y=x/2
if y==int(y):
    print("짝수")


x=input("입력")
if x[-1] in "02468":
    print("짝수")

#숫자가 1000보다 크고 짝수인데 0으로 끝나는 짝수이면 출력
x=input("입력")
if x[len(x)-1]==0 and len(x)>=4:
    print("0으로 끝나는 짝수")


x=input("입력")
if x[-1] in "02468" and len(x)>=4:
    print("짝수이자 1000보다 큰 짝수")