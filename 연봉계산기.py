#람다에 키워드 만든것 사용
#책가격 저럼한거 비싼거 정렬한것 처럼 연봉이 제일 높은사람 부터 낮은사람까지 정렬하기
#이상치 찾을때 해당 라인과 같은셀에 있는거랑 비교하면서
#lista=[]
#def x(**kwargs): #_> 만약 이게 사람만드는 함수라면 딕셔너리 사용할거임
    #return kwargs
#a=x(name='이윤서',age='27',permonth='5555555')
#print(a)
#lista.append(a)



from idlelib.replace import replace
from itertools import count

f=open("근로소득세_문제.txt",'r',encoding='UTF-8')#프로젝트 폴더에 txt파일을 옮겨 놓는다,#open()에서 encoding='UTF-8'로 지정한다.
lista=[]
listb=[]
doc=[]
all=f.readlines()
#이차원으로 표현하고 싶으면 (좌표계처럼[0,0]) 이중리스트로 쓰면 됨

for i in all:
     if i[0]=="#":
          continue #-> #으로 시작하는 필요없는 문장 빼려고 clear썻는데 , clear는 그냥 리스트를 비우는 것
     else:
          lista=i.replace('-','0').replace('\n','').replace(',','').split('\t') #-> split쓰면 '이거'기준으로 ''이렇게 나눠져서 리스트 형태로 나옴
     #lista = i.strip().split('\t')
     #b=a.replace('-','0') #-> 이렇게 하면 a가 리스트 형태여서 replace안됨
     #print(b)
     listb = map(lambda x: int(x), lista)  # 숫자로 변경, line_c 한 번 쓰면 날아감
     lista= list(listb)  # line에 다시 넣음
     doc.append(lista)
print(doc)  # -> doc이라는 리스트 []안에 lista를 append하면 [['770','775','0','0'--],['775'--]]이런식으로 나옴
count=0
for i in doc:
     if count<len(doc):
          for j in range(0,12):
               if (doc[count][j]+(doc[count+2][j])/2)*0.03<doc[count+1][j] or (((doc[count][j])+(doc[count][j]))/2)*0.03>doc[count+1][j]:
                    print(doc[count + 1][j])
                    doc[count + 1][j] = (doc[count][j] + doc[count + 2][j]) / 2
                    print("고친거", doc[count + 1][j])


     count += 2
print(doc)


#import random
#han=list("가나다라마바사아")
#with open("info연봉.txt",'w',encoding='UTF-8') as file:


     #for i in range(10):
        #name=random.choice(han)+random.choice(han)
        #age=random.randrange(20,60)
        #family=random.randrange(0,10)
        #money=random.randrange(770,9900)
        #file.write("{},{},{},{}\n".format(name,age,family,money))


#for line in ff:
     #(name,age,family,money)=line.strip().split(", ") #split을 했기 때문에 리스트 형태로 나옴 , split안하면 하나의 문자열로 나옴
     #print("\n".join(["이름:{}", "나이:{}", "부양가족수:{}", "연봉:{}"]).format(name, age, family, money))
     #print()































