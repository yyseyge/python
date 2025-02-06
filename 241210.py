#재귀 함수
#메모화
#조기리턴

#팩토리얼 연산을 코드로 만들기
#해결 1.반복문 활용 2.재귀함수 활용
#반복문 활용법
def fac(n):
    output=1
    for i in range(1,n+1):
        output*=i
    return output
print(fac(3))

#재귀함수 활용방법 -> 재귀함수는 함수 본인이 본인을 호출하는 형태이다
#재귀함수 사용하는 상황은
# 얼마나 같은 작업을 반복해야 끝이 날지 모르는 문제를 해결할 때 사용한다
def fac2(n):
    if n==0:
        return 1
    else:
        return n*fac2(n-1)
print(fac2(3))

def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
#파이썬 함수 내부에서 함수 외부에 있는 변수를 참조하지 못함..
#외부에 있는 변수 사용하려면 함수내에 => global 변수 명 선언을 해야 함.
counter=0
def fi(n):
    print("fibo({})를 구한다".format(n))
    global counter #함수 밖 counter 변수를 참조 하겠다는 의미
    counter+=1
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fi(n-1)+fi(n-2)
fi(10)
print("===")
print("fi(10)계산에 덤셈횟수는 {}번".format(counter))


dict1={1:1,2:1}
def f(n):
    if n in dict1:
        return dict1[n]
    else:
        output=f(n-1)+f(n-2)
        dict1[n]=output
        return output
print(f(35))


#second가 55일때 까지 도는 재귀 함수, 찾으면 탈출 못찾으면 재귀
import datetime
import sys #setrecursionlimit 사용하기 위해 import
import time #time.sleep사용하기 위해 time import
sys.setrecursionlimit(10000)#재귀함수 깊이 제한 해제
now=(datetime.datetime.now()) #datatime now()s는 호출되는 시점의 시간을 가져온다.
count=0
def finds(x): #재귀 함수는 종료할 수 있는 조건과 재귀를 할 수 있는 조건이 필요하다.
    global count #함수 밖 변수 count를 사용하겠다.
    count+=1 #함수 밖 변수 count를 의미함
    time.sleep(1) #프로세스 진행 중 1초간 정지했다가 다음 코드로 이동됨
    n = datetime.datetime.now() #함수에 들어올 때마다 새롭게 갱신되는 시간 객체 n
    if x==55: #재귀종료되는 조건 : 55초라는 시간값을 발견하면 종료됨
        return count
    else: #재귀 호출하는 조건
        return finds(n.second) #n.second는 함수 내에서 새롭게 얻어낸 최근 시간의 초.
print(finds(now.second))