#범위
#while반복문 : 상황에 따라 for문 혹은 while문을 사용 할 수 있음, for는 반복되는 객체 대상으로 돌릴 때, 그것을 하나씩 꺼내서 써야할 때 사용하고 while은 특정 횟수 특정 시간,특정 조건 도달시 등 이런 조건에서 쓰임
#break 키워드
#continue 키워드
from runpy import run_path

#range()
#range(까지) : 0부터
#range(부터,까지)
#range(부터,까지,스템)

print(range(100))
print(range(0,100))
print(range(0,100,1))

print(type(range(100))) #<class 'range'>출력됨
print(list(range(100))) #[0,1,2,3~~99]출력됨. 0부터99까지의 range를 리스트 형태로 출력함
#range()함수 안에 들어갈 수 있는 요소는 int 뿐인지???

for i in reversed(range(5)): #4,3,2,1,0출력 됨 print(range(4,-1,-1))과 같은 형태로 출력됨.
    print(i)
print()
print("==반복문으로 삼각형 만들기==")
sum=""
for i in range(1,10):
    for j in range(0,i):
        sum=sum+"*"
    sum+="\n"
print(sum)
print()
print("==반복문으로피라미드만들기==")
sum=""
for i in range(1,15):
    for j in range(14,i,-1):
        sum+=' '
    for k in range(0,2*i-1):
        sum+="*"
    sum+='\n'
print(sum)

output=''
n=int(input("몇행?")) #행을 직접 입력받음
for i in range(1,n+1): #첫번째 for문은 행이다. 몇행인지 보고 range설정하면 됨.
    for j in range(0,i-1): # 두번째for문은 공백이다. 처음엔 공백이 하나도 없고 행이 1개씩 늘어날 수록 공백이 하나씩 생김.
        output+=' '
    for k in range(2*(n-i),-1,-1):#그림 그려진 갯수의 규칙이 11,9,7,5,3,1이다, 이건 2*(행의수-들어온i)라는 규칙가짐, (10,-1,-1)이니까 10,9,8,7,6,5,4,3,2,1,0 11개 그림그려짐. 공백이 앞에서 부터 시작이니까 그림은 끝에서부터그림
        if k==0 or k==2*(n-i):#세번째 for문은 *혹은#을 채우는 건데, 만약 같은 모양으로 채워져있으면 if를 안써도 되지만 지금은 *혹은#이기 때문에 if문을 쓴다.
            output+='*'# *은 처음과 끝에 그려져있으니까 k가 0일때가
        else:
            output+="#"
    output+="\n"
print(output)





#for문은 반복가능한객체를 대상으로 사용할 수 있음, 반복가능한객체 내부 요소를 하나씩 뜯어와서 활용 할 수 있다.
#while문은 특정 횟수 반복이나 범용적으로 사용할 때 활용한다.

"""
while bool의 결과를 나타내는 식:
    실행문
"""

"""
x=10
while x>5:
    print(1234)

while 1: #1도 true로 취급해서 사용가능 0은 false로 취급해서 사용가능
    print(123)

x=[1,2,3]
while len(x)>1:
    print(123)
"""

print("==while문을 for문처럼 사용하기==")
x=0
while x<10:
    print("{}번째 while문 반복".format(x))
    x+=1 #정지하기 위한 작업이 필요하다.


"""
import datetime
x=0
while x<10:
    print("{}번째 while문 반복".format(x))
    now=datetime.datetime.now()
    if now.second==30: #특정 시간 값에 도달했을 때 정지시키는 방법
        x=20
"""


x=0
l=[1,2,3,4,5]
while len(l)!=0:
    l.pop()
    print(l)

#변수를 선언합니다
list_test=[1,2,3,4,2,1]
value=2

#list_test 내부에 value가 있다면 반복
while value in list_test:
    list_test.remove(value)
#출력합니다.
print(list_test)

import datetime
import time
print(time.time())
x=0
l=[1,2,3,4,5]
while 3 in 1:
    print(time.time())
    l.pop()










