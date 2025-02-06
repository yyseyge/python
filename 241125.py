#if 조건문 분기문
#파이썬 언어
#print() int() input() str() float() 내장


import datetime
#import는 라이브러리, 패키지, 모듈을 불러오는 역할을 함.
#import는 기본 내장이 아닌 외부 기능 모음
#import datetime의 기능은 날짜 시간 관련 기능 모음을 불러옴
#기본내장이 아님, 불러오고 사용 할 수 있다.

now = datetime.datetime.now() #now는 변수를 생성해준것이고 첫번째 datetime은 모듈이고 두번째datetime은 class이다. now는 함수이다. now는 결과물을 뱉어내는 함수이다.즉 값이 있다
#"문자열".format() , datetime.now
print(type(now)) #now 변수에 담긴 것은 datetime.datetime 객체이다.
print(now.year,"년") #now(객체).year(속성)이다. 속성은 그냥 값을 조회한다 라고 생각하면 된다.
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
#날짜 시간과 관련된 기능을 가져옵니다
import datetime
#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()
#출력합니다.
print("{}년{}월{}일{}시{}분{}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

#날짜/시간과 관련된 기능을 가져옵니다.
import datetime
#현재 날짜/시간을 구합니다.
now=datetime.datetime.now()
#오전 구분
if now.hour<12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour))
if now.hour>= 12:
    print("현재 시간은 {}시로 오후입니다".format(now.hour))

if now.month==11 and now.hour<12 and now.weekday()==0: #weekday는 인덱스 번호로 요일을 알려준다
    print("11월 월요일 오전")

last_num=1
# Last_num이 "abc",0,이든조건식이다참이나옴
if last_num==0 or 2:
    print("참")

a = 2
if a == 2 or "":  #a==2는 true이고 true or ""는 ""이건 false로 인식하는데 true or flase이므로 true가 나옴
    print("참")

zero=0
false=False
none=None
print(zero==false) #true
print(false==none) #false
print(zero==none) #false

# if에서는 숫자0은 F, 1~는 True, false는 False이고 "",[] 이런게 다 비어있으면 false로 본다
#false로 변환되는 값(none,0.0,빈객체("",[])
print("if 조건문에 0넣기")
if 0:
    print("0은 true로 변환됩니다")
else:
    print("0은 false로 변환됩니다")
print("if조건문에 빈 문자열 넣기")
if"":
    print("빈 문자열은 true로 변환됩니다")
else:
    print("빈 문자열은 false로 변환됩니다")

#else 조건문 활용
#else문은 if 조건문 뒤에 사용함
#if조건이 거짓(false)일 때 실행된다.
#if조건문은 else 혹은 elif와 조합가능
n = int(input("정수 입력"))
if n%2==0:
    print("짝수입니다")
else:
    print("홀수입니다.")

#elif 구문
#두 가지로 구분되지 않는 조건문 작성에 사용
#elif로 조건을 추가
#if와 else 사이에 위치해야함
#elif는 여러개 가능

#날짜/시간 관련된 기능을 가져옵니다.
import datetime
#현재 날짜/시간을 구하고 쉽게 사용할 수 있게 월을 변수에 저장합니다.
now=datetime.datetime.now()
month=now.month
#조건문으로 계절을 확인합니다.
if 3<=month<=5:
    print("봄입니다.")
elif 6<=month<=8:
    print("여름입니다.")
elif 9<=month<=11:
    print("가을입니다")
else:
    print("겨울입니다.")

#누적예제
score=float(input("학점을 입력하세요"))
if score==4.5:
    print("")
elif 4.2<=score:
    print("교수님의 사랑")
elif 3.5<=score:
    print("현 채제의 수호자")
elif 2.8<=score:
    print("일반인")
elif 2.3<=score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75<=score:
    print("")
elif 1.0<=score:
    print("")
elif 0.5<=score:
    print("")
elif 0<score:
    print("")
else:
    print("시대를 앞서가는 혁명의 씨앗")

#함수안에 쓰이는 변수를 매개변수라고 한다

pass #조건문 내 실행문 없는 경우에 실행 오류가 나지 않도록 처리
# 조건문 내에 문법 오류가 없는지 보거나 임시처리 느낌으로 사용
#if문은 내부 실행문 없으면 문법적 오류가 발생하기 때문에 pass사용

#간단한 대화 프로그램
import datetime
now=datetime.datetime.now()
c=input("대화를 입력하세요")
if "안녕" in c:
    print("안녕하세요")
    if "지금" in c or "몇시" in c:
        print("지금은{}시 입니다".format(now.hour))
if "지금" in c or "몇 시" in c:
    print("지금은{}시 입니다".format(now.hour))
else:
    print(c)

#나누어 떨어지는 숫자
n=int(input("정수를 입력하세요"))
if n%2==0:
    print("2로 나누어 떨어지는 숫자입니다.")
elif n%2!=0:
    print("2로 나누어 떨어지는 숫자가 아닙니다")
if n%3==0:
    print("3으로 나누어 떨어지는 숫자입니다")
elif n%3!=0:
    print("3으로 나누어 떨어지는 숫자가 아닙니다")
if n%4==0:
    print("4로 나누어 떨어지는 숫자입니다.")
elif n%4!=0:
    print("4으로 나누어 떨어지는 숫자가 아닙니다")
if n%5==0:
    print("5로 나누어 떨어지는 숫자입니다")
elif n%5!=0:
    print("5로 나누어 떨어지는 숫자가 아닙니다")


#리스트 : 숫자, 문자열, 불처럼 데이터 타입 중 하나
#요소 : 리스트 데이터 타입 내부에 단일 데이터를 뜻함
#인덱스 : 0번부터 시작하는 요소의 번호
#for반복문 : 특정 실행문을 반복하여 수행하기 위한 문법

#리스트 : 리스트는 [] 대괄호로 표현한다
#listA=[1,2,3,4,5] -> 리스트 내부 요소는 쉼표로 구분
#리스트 중 빈 리스트는 [] 빈 괄호로 표현
#리스트는 여러가지 자료를 저장할 수 있는 자료 타입니다
#문자,숫자,boolean은 단일데이터이다.

array=[273,32,103,"문자열",True,False] #array와 list는 다르게 작동한다. 이건 array라는 변수로 만든 list임
print(array)
print(type(array))
#인덱스 번호를 통해 리스트 내부 요소에 접근 가능
print("안녕하세요"[0])

#리스트는 문자열과 동일하게 인덱스, 슬라이스 사용 가능
#리스트는 내부 요소를 인덱싱을 통해 접근한다(조회)
#리스트는 내부 요소를 인덱싱을 통해 접근해서 수정가능
print(array[-3])
array=[273,32,103,"문자열",True,False]
#2중 인덱스
print(array[-3][0]) #[-3]한 결과가 문자열임 -> 문자열은 인덱스 가능
listaa=[[1,2,3,[44,55],66],[4,5,6],7,8,9,'열번째']
print(listaa[0][3][0])
#list 연산
# +
# *
#list()
lista=[1,2,3]
print(lista*10) #숫자를 연산해서 반복되는 리스트 생성
print(len(lista)) # 리스트의 len 은 요소의 수
lista[0]=100
print(lista)

str_x="안녕하세요"

#리스트 관련 함수
#1. append() -> 리스트에 요소를 추가하는 함수
#리스트명.append(추가요소)
lista.append(4) #lista에 4를 추가 함 (가장 뒤에 붙는다)
print(lista)

#2. insert() -> 특정 위치에 요소 추가
#리스트명.insert(위치,요소)

#3. extend() -> + 연산자와 같은 기능 함
listb=[6,7,8]
lista.extend(listb)
print(lista)

# 리스트 연결 연산자(+)와 extend()의 차이점
lista=[1,2,3]
listb=[4,5,6]
print(lista+listb) # +로 연산하면 원본 영향 없음
print(lista,'a')
print(listb,'b')

listc=[1,2,3]
listd=[4,5,6]
listc.extend(listd) #extend()로 적용하면 원본이 변형됨
print(listc,"c")
print(listd,"d")

#리스트 요소 제거
#1.인덱스를 통한 접근 후 제거 방법과
#2.값으로 제거 방법이 있다.

# 인덱스를 통한 제거 방법 1 -> del키워드로 제거
#print() 함수 안에 들어갈 수 있는거는 변수로 감쌀수 있는것이다, 즉 어떤 결론이 있는것이 들어갈 수 있다.
# 어떤 값이나 수식이나 변수가 들어갈 수 있는데 del listx[0] 이런거는 명령문이다. 그저 지워라 라는 액션만 취할 수 있고 리턴값이 없으므로 print()로 감쌀 수 없다.
#del은 원본에 영향을 끼친다.

listx=[1,2,3,4,5,6]
del listx[0]
print(listx)
#인덱스를 통한 제거 방법 2 -> pop()함수를 통한 제거 방법이 있다 이 방법도 두가지가 있는데 pop(), pop(인덱스)
#pop() : 매개변수 설정 안하면 -1인덱스 위치의 요소를 제거한다.
listx.pop()
print(listx)
#pop(인덱스) : 지정한 인덱스 위치의 요소를 제거한다.
listx.pop(0)
print(listx)


#값으로 제거 하는 방법 -> remove()로 제거
#리스트타입.remove(값)
listc=[1,2,1,2]
listc.remove(2) #2값을 찾아 제거해라
print(listc)
#remove 함수로 지정한 값이 리스트 내부에 여러개 있으면 가장 먼저 발견되는 것(좌측부터)을 제거하고 종료함

#리스트 요소 전부 제거하는 방법 -> clear()


list2=[2,3,4,5,6]
list2.clear()
print(list2) #clear() 호출 후 리스트는 빈 리스트

listslice=[1,2,3,4,5,6,7,8]
print(listslice[::2],'res') # 1,3,5,7 출력 됨
print(listslice[::-1],'res') #8,7,6,5,4,3,2,1, 출력됨
print(listslice[::-3]) # 8,5,2 출력됨


#리스트의 정렬 방법
#sort()
#기본 오름차순 정렬
#리스트.sort()
liste=[52,273,130,32,275,1,7]
liste.sort() #오름차순
print(liste) #sort()함수는 원본에 영향을 주는 파괴적 함수이다
liste.sort(reverse=True)
print(liste)

list_text=["a","c","b"] #문자열도 sort사용하면 사전에 나오는 순서대로 정렬된다.
list_text.sort()
print(list_text)

#리스트 내부 검사
#in
#not in
#값 in list
#값 on not in list
list_a=[222,33,103,55,52]
print(222 in list_a)
print(34 in list_a)
print(34 not in list_a)
print(not(34 in list_a))

#반복문(for문)
"""
for 반복자 in 반
복 가능한 객체(반복가능한 객체 종류는 문자열, 리스트, 딕셔너리, range등이 있다):
    실행문
"""
for i in range(100): #0~99까지의 반복가능한 숫자 객체이다.
    print("출력") # range라는 함수를 통하여 출력이라는 단어를 100번 나오게 함
    print("안녕")#출력 안녕 이 100번 나옴
    print("출력",i) #i는 0부터 99까지 순차적으로 대입

print(range(100))
# range 함수는 특정 숫자 범위를 쉽게 만들어 준다
#0부터 100까지 숫자 리스트를 만들어줌 , 리스트랑 비슷함

#for문의 반복 가능한 개체는 문자열, 리스트, 딕셔너리 , range 등이 있다.
for i in "안녕하세요":
    print("하이",i) #하이,안 /하이,녕/하이,하/하이,세/하이,요

lol=[[1,2,3],[4,5,6,7],[8,9]] #2차원 리스트
for i in lol:
    print(i) #[1,2,3] / [4,5,6,7]/[8,9]로 출력됨

for i in lol[0]:
    print(i)
for i in lol[1]:
    print(i)
for i in lol[2]:
    print(i)

for i in lol:
    for j in i:
      print(j)


listX=[1,2,3,4]
print(*listX)
print(listX[0],listX[1],listX[2],listX[3]) #print(*listX)랑 이거랑 똑같음.

n = [273,103,5,32,65,9,72,800,99]
for i in n:
    if i%2==0:
        print(i,"는 짝수입니다")
    else:
        print(i,"는 홀수입니다")
for i in n:
    if len(str(i))==3:
        print(i,"는 세자릿수 입니다")
    elif len(str(i))==2:
        print(i,"는 두자릿수 입니다")
    elif len(str(i))==1:
        print(i,"는 한자릿수 입니다.")



number=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]

for number in number:
    output[(number%3)-1].append(number)
print(output)
