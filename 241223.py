#Module

import math #수학관련함수, 필드 제공
import datetime #날짜 시간 관련 함수 필드 제공
import math #난수 생성 관련 함수 필드 제공
#얘네는 내장 모듈이다

print(math.pi) #3.141592~~원주율 값 나옴
math.pi=123
print(math.pi) #123나옴 , 즉 math는 읽기 쓰기 모두 가능하다.
print(math.floor(2.5)) #2나옴, 내림값 구하는 식
print(math.ceil(2.4)) #3나옴, 올림값 구하는 식
print(round(1.5))#2나옴, 반올림구하는 함수
print(round(1.4))#1나옴

#from 모듈이름 import 가져오고싶은 변수 혹은 함수
from math import sin,cos,tan #math에서 sin cos tan만 가져오겠다는 뜻
from math import * #math에서 모두 가져오겠다는 뜻


#절대경로
import os #를 써서
path2="c:/"
print(os.listdir(path2))
fileName="q.txt"#근로소특표 파일명이다.
filePath=os.getcwd().replace("\\","\\\\")+"\\\\"+fileName #getcwd는 현재 디렉터리 위치이다.
print("cwdPath",os.getcwd())
print("filePath",filePath)
#get current working dir 통한 절대 경로
with open(filePath,'r',encoding='UTF=8') as f:
    print(f.readline())

#상대경로 : 현재 디렉터리 (241223.py가 포함된 경로) 기준의 경로
with open("q.txt",'r',encoding='UTF-8') as f:
    print(f.readline()) #현재 디렉터리에 있는 q.txt오픈
with open("../qq.txt",'r',encoding='UTF-8') as f: #../ 상위폴더의미
    print(f.readline()) #현재 디렉터리의 상위폴더에 있는 qq.txt오픈

#os모듈을 이용해서 현재 디렉터리에 하위 폴더를 하나 만들고 근로소득표txt를 코드를 통해 하위폴더 내에 복사붙여넣기 후 첫줄을 출력한다.
#코드를 통해 하위폴더 내에 복사붙여넣기 후 첫 줄을 출력한다
import shutil
#mkdir : 폴더생성방법
#shuyil.copy(원본파일, 어디에 복사할지 경로) : 파일 복사 방법
#listdir : 현재 디렉터리의 내부 모든 파일 보는 방법
newName="new"
newDir=os.getcwd().replace("\\","\\\\")+"\\\\"+newName
if os.path.exists(newDir): #이폴더가 존재하는지 체크
    pass #폴더가 이미 있으면 패스
else: #폴더가 없으면
    os.mkdir(newDir) #폴더 생성
print(os.listdir()) #잘 생성 되었는지 출력해서 확인
shutil.copy(filePath,newDir) #새 폴더에 q.txt파일 복사

