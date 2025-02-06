#302p
from cgi import print_environ_usage

from traceback import print_tb

dicta={}
def fi(n):
    if n in dicta:
        return dicta[n] #조기리턴 탈출 , return뒤에 아무것도 없이 리턴하면 결과값이
    output=fi(n-1)+fi(n-2)
    dicta[n]=output
    return output

def ttt():
    return
x=ttt()
print(x) #이때 x값은 None이 나온다 return뒤에 아무것도 없이 리턴해서 그럼

#def ttt():
    #if A:
        #return  a
    #elif B:
        #return True
    #elif:
        #return
    #else:
        #return ttt() => 리턴 뒤에는 다른 함수도 호출할 수 있다.

x=[1,2,3,[4,5,6],[7,[8,9]],10]
for i in x:
    if type(i) is list:
        for j in i:
            if type(j) is list:
                print(j)


def flatten(data):
    output=[]
    for i in data:
        if type(i)  is list:
            output+=flatten(i)
        else:
            output.append(i)
    return output

ex=[[1,2,3],[4,[5,6]],7,[8,9],10,[11,12,[13,14,[15]]]]
print("원본",ex)
print("변환",flatten(ex))

min_x=2
max_x=10
total_x=10
memo={}
def sit(total_x,min_x):
    key=str([total_x,min_x])
    if key in memo: #이미 메모가 되어있는 것을 리턴
        return memo[key] #memo[key]밸류를 리턴
    if total_x <0: #무효
        return 0
    if total_x==0: #유효
        return 1
    count=0 #카운트 변수
    for i in range(min_x,total_x,1):
        a=total_x-min_x
        print(min_x,a)
        if a>2:
            print("e")
            #def sit(a,앉힌사람수)
    memo[key]=count #메모화
    return count #최종 수 리턴
print(sit(total_x,min_x))


#316p
#콜백함수
#람다
#with구문
#튜플

#람다:def로 작성 함수를 줄여서 작성하는 방식
#함수의 매개변수로 함수 전달하기

def call_10_times(func):
    for i in range(10):
        func()
def print_hello():
    print("안녕")


x=print_hello
call_10_times(x)
#함수의 매개변수에 사용하는 함수 : 콜백함수

#filter() -> filter(함수,리스트)
#map() -> map(함수,리스트)


def power(item): #코드를 여러번 쓸거면 def쓰고 , 한번만 사용할 것 같으면 lamda쓰면됨
    return item*item
def under_3(item):
    return item<3
list_input_a=[1,2,3,4,5]
output_a=map(power,list_input_a)
print(output_a) #결과가 mapobject로 출력됨
print(list(output_a)) #결과가 [1,4,9,16,25]
output_b=filter(under_3,list_input_a)
print(list(output_b)) #결과 1,2나옴 , filter함수는return이 true인것만 값을 줌 그때 list처리해서 print하면 값이 true인 요소를 출력해줌
print(under_3(1)) #결과 True나옴 , filter함수는 return이 true이면 true로 출력
#map object at 0x0000024ECD59EF80
#위 obj형태는 제너레이터이다
#a=[1,2,3,4,5]
#a리스트의 모든 요소를 제곱해서 리스트로 만들어서 출력하세요.
out=[]
a=[1,2,3,4,5]
for i in a:
    out.append(i*i)
print(out)


#lamda
#lamda 매개변수 : 리턴값
#lamda x: x*x
power=lambda x:x*x
under_3=lambda x:x<3
list_input_a=[1,2,3,4,5]
print(list(map(power,list_input_a)))
print(list(filter(under_3,list_input_a)))

#filter map lamda를 사용하여
lista=[1,2,3,4,5,6,7,8,9,10]
# 에서 3의 배수만 뽑아서 그 수를 제곱한 리스트를 리턴받아 출력하라

print(list(map(lambda x:x*x,list(filter(lambda x:x%3==0,lista)))))

#파일처리
#파일은 크게 텍스트파일과 바이너리 파일로 나뉜다.
#open()이라는 함수로 파일을 연다
#파일을 열고 나서는 파일 읽기 쓰기가 가능하다.

#파일객체=open(문자열: 파일경로, 문자열: 읽기모드)
#open함수의 첫 매개변수는 파일경로이고 두번째 매개함수는 모드인데, 모드의 종류는
#W 쓰기모드 => 파일을 새로 생성하고 작성
#a append모드 => 기본에 있는 파일을 열고 작성
#r 읽기모드 => 읽기만한다.

#파일객체.close()
file=open("basic.txt","w")
file.write("안녕하세요")
file.close() #파일객체는 사용 완료 후 항상 닫아줘야함

with open("basic.txt","w") as file: #close를 수동으로 안해도됨
    file.write("12345")

with open("basic.txt",'r') as file:
    contents=file.read()
print(contents)

import random
han=list("가나다라마바사아")
with open("info.txt",'w',encoding='UTF-8') as file:
    for i in range(1000):
        name=random.choice(han)+random.choice(han)
        weight=random.randrange(40,100)
        height=random.randrange(140,200)
        file.write("{},{},{}\n".format(name,weight,height))
print(random.choice([1,2,3,4,5]),"rchoice") #리스트중 랜덤으로 하나 뽑음
print(random.randrange(40,100),"rrange") #40부터 100까지의 숫자중 무작위 숫자 뽑기
print(random.random(),"rrandom") #0~1까지의 난수 생성

count=0
with open("info.txt",'r') as file:
    for line in file:
        (name,weight,height)=line.strip().split(", ") #split을 했기 때문에 리스트 형태로 나옴 , split안하면 하나의 문자열로 나옴

        count+=1
        if (not name)  or (not weight) or (not height): #=> 이 if문은 결측치를 측정하는 거다.
            print(count)
            continue
        #결과를 계산합니다.
        bmi=int(weight)/((int(height)/100)**2)
        result=""
        if 25<=bmi:
            result="과"
        else:

            result="저"

        print("\n".join(["이름:{}","몸무게:{}","키:{}","결과:{}"]).format(name,weight,height,bmi,result))
        print()


import time
def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"
list_job=iter([longtime_job() for i in range(5)]) #이터레이터
print(type(list_job),"list->iter")
#이터레이터로 형변화함 #리스트내포 #함수호출
print(next(list_job)) #next한번사용
print()
list_job=(longtime_job() for i in range(5)) #제너레이터
#제너레이터표현식사용 #함수호출
print(next(list_job)) #next한번사용 -> job1 done1

#1번식 설명 : 리스트컴프리핸션
#같은 식 longtime_job() for i in range(5)을 리스트내포하면 결과 값 타입이 리스트가 된다.
#생성과 동시에 job()함수가 5번 다 호출되고, job()리턴값 5개를 가지고 리스트를 구성한다.

#2번식 설명 : 제너레이터컴프리핸션
#같은식 longtime_job() for i in range(5)
#제너레이터를 사용하여 job함수 5번실행
#한번에 하나씩 값을 생성, 계산 연산 한다.
#next() 호출되면 하나씩 실질적으로 계산한다.
#메모리 낭비 줄이기 위해
#각 함수의 실행은 필요할때 next()호출을 통해 실행
#지연 실행


def test():
    print("함수가 호출됨")
    yield "test"
print("a지점") #a지점 출력됨
test()
print("b지점") #b지점 출력됨
test()
print(test()) #제너레이트 객체 츨력

def test(): #=> 이함수는 제너레이터 함수이다 왜냐 yield가 써있으니까
    print("A지점통과")
    yield 1
    print("B지점통과")
    yield 2
    print("C지점통과")

output=test() #test() 제너레이터는 일반 호출방식 사용하면 gen obj가 나온다. 그래서 output에 담아놓고 next()를 사용해야함
print("DDDD") #cnffur
a=next(output) #1yield까지 실행
print(a)#yield에 의해 a변수에 1이 들어온다
print("EEEE")#출력

b=next(output)#2.yield까지 실행
print(b)#yield에 의해 b변수에 2가 들어옴
print("FFFF")
#c=next(output) #3번째 yield는 없고 print("C통과")만 있는 상태
#print(c) #stopIteration발생


#이터러블이란 반복가능한 데이터 타입 (리스트 딕셔너리 등)
#이터레이터는 iter()함수 사용해서 만든다. 사용할때는 for문 사용할수도 있고 next()함수 쓸수 있다. 이터레이터는 결과물인 객체를 의미 제너레이터는 함수를 의미
#제너레이터는 실질적으로 이터레이터를 생성하는 함수이다, 그래서 호출 해봤자 의미 없음(제너레이터 오브젝트만 출력됨) , 사용할때는 next()함수로 사용됨, 이터레이터요소나 제너레이터yield 갯수를 넘어가면
#stopiteration발생함. 이터레이터 제너레이터의 공통점은 한반퀴 돌면 더이상 못돈다
#---------------------------------------------------------------------------------------------------------------
#리스트내포를 통해 이터레이터를 생성
#이 리스트는 random 모듈을 사용한 0.x(소숫점1자리까지) 형태의 난수를 10개 저장한다.
#리스트 변수명은 r


r=iter([str(random.random())[:3] for i in range(10)])
for i in r:
    print(i)

books =[{"제목":"혼자공부하는 파이썬","가격":18000},{"제목":"혼자 공부하는 머신러닝 딥러닝","가격":26000},{"제목":"혼자공부하는 자바스크립트","가격":24000}]

def x(book):
    return book["가격"]
print("#가장저렴한책")
print(min(books,key=x))
print()

print("#가장 비싼책")
print(max(books,key=x))

test=lambda x,y:x+y #람다함수에 식별자 부여 , 매개변수가 2개인 람다함수
print(test(10,20))

max_value=lambda a,b:a if a>b else b #a>b이면 a리턴 else면 b리턴
print(max_value(10,20))
print(max_value(40,20))
#a>b이면 a리턴 else면 b리턴

sssum=lambda *args:sum(args) #*args는 가변 매개변수이고 튜플로 묶인다
print(sssum(1,2,3,4,4,5),"ssssum합계")
#가변매개변수는 *args 사용

m=lambda **kwargs:f"사용자의 이름은 {kwargs.get('n','guest')}나이는{kwargs.get('age','0')}" # **kwargs는 키워드매개변수이다. 얘는 딕셔너리 형태로 저장됨.
print(m(n='302호',age=50))
print(m(n='301호'))
print(m())
#**kwargs를 사용해서 키워드 매개변수 여러개 받을 수 있음 .
#람다는 간단한 사용법에서 쓴다. 이분법이나 그럴때 사용한다.


books =[{"제목":"혼자공부하는 파이썬","가격":18000},{"제목":"혼자 공부하는 머신러닝 딥러닝","가격":26000},{"제목":"혼자공부하는 자바스크립트","가격":24000}]
print("#가격 오름차순 정렬")
books.sort(key=lambda book:book['가격'])
for book in books:
    print(book)
#sort()함수의 특징은 만약 어떤 list를 sort하면 리스트 원본을 파괴한다. sort()함수는 그냥 쓰면 오름차순, a.sort(reverse)이렇게 하면 내림차순 sort(key) sort안에 key주면 그 key를 기준으로 오름차순 정리함.