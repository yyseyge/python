#import time
#number = 0
#x=[1,2,3,4,5,6,7,8]
#target_tick=time.time()+5
#while time.time() < target_tick:
    #number+=1
    #for i in x:
        #x.count(i)
#print("5초동안{}번 반복했습니다".format(number))
from multiprocessing.connection import reduce_pipe_connection
from runpy import run_path
from tkinter.scrolledtext import example
from traceback import print_tb

#키워드
#break
#continue
#위 2가지 키워드는 반복문의 내부에서만 사용 가능
#반복문의 내부에 들여쓰기로 들어간 자식
#break키워드는 반복문을 탈출하게 하는 기능
#continue키워드는 반복문의 처음으로 돌아가서 실행 하는 기능

i=0
while True:
    print("{}번쨰 반복문입니다".format(i))
    i = i+1
    text=input("종료하시렵니까?(Y/N): ")
    if text in ["Y","y"]:
        print("반복을 종료합니다")
        break

#내가 어떤 문제같은 거 내고 정답맞추면 종료되는 그런 프로그램 만들때 while 사용

#key_list =["name","hp","mp","level"]
#value_list=["기사",200,30,5]
#character={}
#for i in key_list:
    #print(i)
#for j in v


limit = 10000
i = 1
sum_value=0

while sum_value<limit:
    sum_value+=i
    i+=1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다".format(i-1,limit,sum_value))

print()
print("==249p4번==")
maxv=0
a=0
b=0
for i in range(1,100):
    j=100-i
    if j*i>maxv:
        maxv=j*i
        a=j
        b=i
print("최대 경우는 {}*{}={}".format(a,b,maxv))

#time => UTC 1970 1 1 기반 sec 얻을수있음
#ㅔ.244 예제처럼 반복해서 input을 요청하는 문제
#아래 UTC기반 초에서 아래 데이터 기준 971.6
#만약 문제를 틀린 경우 => 힌트 출력 1732759971까지 보여준다 (ms)소숫점은 보여주지 안흥ㅁ
#문제를 20번 안에 맞히지 못하면 '실패' 출력
#20번안에 정답 맞히면 '성공출력'
#while break type 문자열로 해서 잘라서 특정 부분만 정답체크할 수 있는 if문
#print("==내가생각한버전==")
#i=0
#while True:
        #print("{}번째 반복문입니다".format(i))
        #i+=1
        #ans = input("정답을 입력하세요(xxx.x): ")


        #if ans in str(now): #이렇게 코드를 만들어 버리면 input으로 입력할때 4만 입력해도 now안에 4가 들어가있으므로 정답이 되어버린다.
            #print("성공")
            #break
        #elif ans not in str(now):
            #print(int(now))
        #if i>20:
            #print("실패")
            #break
#print()
#print("==선생님버전==")
#count=0
#while count !=20:
    #import time
    #count+=1 #몇 바퀴인지 카운트
    #x=str(time.time()) #시간값을 문자열로 변환하여 x변수에 기억
    #x2=x[7:12] #정답형태로 xxx.x 문자열 슬라이싱
    #v=input("xxx.x초입력")#사용자 입력
    #if x2==v: #정답이 사용자 입력과 같은지
        #print("정답")
        #break
    #else:
        #print("오답", x.split(".")[0])   #x.split(".")[0]
    #if count==20:
        #print("실패")


#딕셔너리에 사용 가능한 딕셔너리 함수
#key() : 키 리스트를 얻을 수 있다.
a={"A":100,"B":200,"C":300}
print(type(a.keys())) #a.keys는 a딕셔너리의 키 묶음 객체 리턴
list(a.keys()) #키 묶음 객체는 list로 형변환 가능 => 형변환 하는 이유는 append처럼 리스트에 쓸 수 있는 함수를 적용할 수 있도록 하기 위해
print(type(list(a.keys())))#리스트로 변환 후 타입
for i in list(a.keys()): #for문같은 경우는 딕셔너리 자체로도 가능하므로 굳이 형변화 안해도됨
    print(i)
for i in a:
    print(i)
for i in a.keys():
    print(i)

#items()는 딕셔너리 내부 키:밸류 들을 얻는 함수이다.
print(a.items())

#claer()는 딕셔너리 비우는 함수
a.clear()
print(a)

#get()

print("1"in"12345")
print("1"in["1",'2'])
print('A'in a)

if 'A' in a:
    print("A키 있음")

#리스트에 적용가능한 함수 min(),max(),sum()
#최소, 최대, 합 함수
#reversed() 리스트 뒤집기
#enumerate() 열거 함수

num=[1,2,3,4,5,6]
print(min(num))
print(max(num))
print(sum(num))

reversed_num=reversed(num)
print(reversed_num)
print(list(reversed_num)) #reversed(num)을 써서 리스트를 뒤집은 값을 저장한 변수를 바로 print(reversed_num)하면 이상한 값 나옴 이때 그 변수를 리스트로 형변환해서 출력해야지 제대로 나옴

temp=reversed([1,2,3,4,5,6])
for i in temp:
    print(i,"1111")
for i in temp:
    print(i,"222222")


#두번째 for문이 출력되지 않는 이유?
#reversed()를 통해 만들어진 객체 <list_reverseiterator object>는
#한 번 for문을 통해 내부 순화가 끝나면
#객체 내부적으로 더 이상 조회가 되지 않는 객체 형태임
#for문을 통해 첫 번째 순회시 내부 데이터가 소모 됨.




for i in reversed([1,2,3,4,5,6]):
    print(i,"33333")
for i in reversed([1,2,3,4,5,6]):
    print(i,"4444")
#두 번 for문을 반복하려면 위 코드 방식으로 작성해야함,
#위 코드는 두 for문 모두 출력

import time
x=time.time()
if type is float:
    print(x)
if type is float:
    print(x)

import time
y=time.time()
if type(1) is int:
     print(y)
time.sleep(1)#강제 시간 지연
if type(1) is int:
    print(y)

if type(1) is int:
    print(time.time())
time.sleep(1)
if type(1) is int:
    print(time.time())

example_list=['요소a','요소b','요소c']
for i in example_list:
    print(example_list.index(i),i,"#")

x=0
for i in example_list:
    print(x,i,"##")

for i in range(len(example_list)):
    print(i,example_list[i],"###")

#enumerate() 열거 함수
#for i in~~~: => 이게 기본 구조인데
#enumerate() 열거함수 사용하면
#for i,j in ~~~: 이렇게 반복 변수를 두개 넣을 수 있다.

example_list=["요소A","요소B","요소C"]
print()

print("#단순출력")
print(example_list)
print()

print("#enumerate()함수 적용 출력")
print(enumerate(example_list))
print()

print("#list()함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("#반복문과 조합하기")
for i,value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))

exmple_dictionary={"키":"값A","키B":"값B","키C":"값C"}
print("#딕셔너리의 items()함수")
print("items():",exmple_dictionary.items())
print()
print("#딕셔너리의 items()함수와 반복문 조합하기")
for key,element in exmple_dictionary.items():
    print("dictionary[{}]={}".format(key,element))


#for i in 반복가능한객체:
#반복할 수 있는 것 : 이터러블
#이터레이터$이터러블
#이터러블 : 순차적인 값을 반환할 수 있는 구조 -> 리스트, 문자열, 딕셔너리


#이터레이터 : 반복을 실제 수행하는 객체
#이터레이터는 이터러블 객체에서 값을 순차적으로 하나씩 꺼내는 역할을 한다.
#이터레이터로 되는 종류는 reversed()의 반환값, iter()의 반환값, enumerate()의 반환 값 => 이터레이터는 print()해보면 at 메모리 주소 형태로 출력됨.
#next()를 통해 순차적으로 다음 값을 반환, next()함수는 이터레이터만 사용가능
#next()사용시 stopIteration 더이상 반환 할 값 없다.
#한번 순회를 마치면 다시 조회 불가
testlist=["500","600","700"] #이터러블 객체 , 반복 가능한 객체
#print(next(testlist)) testlist 이터러블 이지만 이터레이터는 아님, next불가
testiter=iter(testlist) #이터러블 객체에서 이터레이터로 변화 iter()함수를 사용함.
print(testiter)
print(next(testiter))
print(next(testiter))


lista=[1,2,3,4,1,2,3,1,4,1,2,3]
counter={}
for i in lista:
    if counter.get(i)==None:
        counter[i]=1

    else:
        counter[i]=counter[i]+1
print(counter)



x=input("염기서열을 입력해 주세요")
a=0
t=0
c=0
g=0
for i in x:
    if i=="a":
        a+=1
    elif i=="t":
        t+=1
    elif i=="g":
        g+=1
    else:
        c+=1
print("a의갯수:{},t의갯수:{},g의갯수:{},c의갯수:{}".format(a,t,g,c))


counter={}
x=input("염기서열을 입력해 주세요")
print(x)
for i in x:
    if i not in counter:
        counter[i]=0
    counter[i]+=1
print(counter)

print()

text=input("염기서열을 입력하세요") #문자열의 슬라이싱 함수는 파괴적이지 않다. 슬라이싱 해도 text는 원본 그대로 이다.
counter={}
i = 0
dna = text[i:i + 3]
while len(dna)==3:
    if counter.get(dna)==None:
        counter[dna]=1
        i += 3
        dna = text[i:i + 3]
    elif counter.get(dna)!=None:
        counter[dna]=counter[dna]+1
        i += 3
        dna = text[i:i + 3]
print(counter)
print()

print("==선생님버전==")
atgc=input("염기서열입력")
l=[atgc[i:i+3]for i in range(0,len(atgc),3) if len(atgc[i:i+3])==3]
counter={}
for i in l:
    if i not in counter:
        counter[i]=0
    counter[i]+=1
print(counter)

lista=[1,2,[3,4],5,[6,7],[8,9]]
listb=[]
for i in lista:
    if type(i)==list:
        for j in i:
            listb.append(j)
    else:
        listb.append(i)
print(listb)