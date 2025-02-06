from runpy import run_path

print("==214p3번==")
n = [273,103,5,32,65,9,72,800,99]
for i in n:
    if i%2==0:
        print(i,"는 짝수입니다")
    else:
        print(i,"는 홀수입니다")
for i in n:
    print("{}는{}자릿수입니다".format(i,len(str(i)))) #리스트는 len가능한데 int형식은 len()함수 쓰려면 str형태로 바꿔줘야함
print()
print("==215p 4번==")
number=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]

for number in number:
    output[(number%3)-1].append(number)
print(output)


print()

print("==215p 5번==")
numbers=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(numbers)//2): #리스트는 len()함수 쓸 수 있음
    j=(i*2)+1
    print(f"i={i},j={j}")
    numbers[j]=numbers[j]**2
print(numbers)
print()

#숫자 문자열 bool 리스트
#정수와 실수
#8진수 #8진수 표기법 : 숫자0+알파벳o+8진수 숫자
#16진수 #16진수 표기법 : 0X16진수 숫자
a=0o100
print(a)#print에 8진수 넣으면 10진수로 나온다
b=0xff
print(b) #16진수
c=0x00
print(c)#16진수

#문자열 자료형
#함수들
#1.dount
a="hello"
print(a.count('l')) #count함수는 문자열에 찾는 문자가 몇개인지 알려줌
#2.find
print(a.find('h')) #find는 문자를 찾고 인덱스 번호를 리턴, 만약 찾고자 하는 문자가 해당 문자열에 없으면 -1을 리턴함
#3.index
print(a.index('h')) #index또한 문자를 찾고 인덱스 번호를 리턴함, find와 똑같은 기능이지만 다른점은 찾고자 하는 문자가 해당 문자열에 없으면 에러남.
print()
#join()함수 -> 문자열 중간에 삽입 해주는 함수, join()뒤에 있는 문자열 사이사이에 join앞에있는 문자를 껴놓는다.
s="hello"
print("_".join('abcdef'))#문자열데이터.join
print(s.join("12345"))#문자열이담긴변수.join
print()

#문자열과 리스트의 유사한점
#1.len()사용가능
#2.slice, index,연산(+,*)가능,for문의 대상으로 사용가능
#문자열과 리스트의 차이점
#1.문자열은 문자로만 구성, 리스트는 어떤 데이터 타입도 담을 수 있다.
#2.리스트는 특정 인덱스 위치의 값을 바꿀 수 있지만 문자열은 인덱스를 통해 값을 바꿀 수 없다.
#3.문자열은 인덱스를 통해 값을 바꿀 순 없지만 값을 볼 순 있다.

#문자열의 일부 문자를 수정하는 방법은 인덱스가 아닌 함수를 통해 가능하다.-
#replace()사용
aa="abcdefg"
print(aa.replace('a','f'))
print(aa) #replace()함수는 비파괴적함수이다.

#split()분리
aaa="aaa bbb ccc"
print(aaa.split()) #split()함수안에 아무것도 안들어있으면

# 공백을 기준으로 문자열을 분리해서, 리스트 형태로 반환한다.
print(aaa) #split()함수는 비파괴적함수이다. 원본을 건들지 않는다.
print()
bbb="aaaXaaaXaaa"
print(bbb.split("X")) #split()함수안에 어떤 문자가 들어가있으면 그 문자 기준으로 분리 한 후 리스트 형태로 반환하다.
print(bbb)

#딕셔너리
#딕셔너리/키/밸류

#리스트 : 인덱스 번호 기반으로 자료를 정리하고 저장한다.
#딕셔너리 : 키 값을 기반으로 특정 값을 저장한다.

x={
    "키1":10,
    "키2":20,
    "키3":30,
    1:40,
    False:50

}

dict_a={"name":123,"value":100,"yes":[1,2,3,[4,5]]}

print(dict_a["name"]) #리스트에서 인덱싱과 같은 방법으로, 인덱스 번호 아닌 Key이름을 입력

#리스트 : 순서에 의존한다, 그냥 어떤 값을 나열하는것(출석부처럼)
#딕셔너리 : 구성에 의존한다. 무엇이 어떻게 구성되어있는지 나타낼 때 사용하기 좋음.


print("==딕셔너리를 선언합니다==")
dictionary={
    "name":"건조망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}
print("name",dictionary["name"])
print("type",dictionary["type"])
print("ingredient",dictionary["ingredient"])
print("origin",dictionary["origin"])
print()
print("==값을 변경합니다==")
dictionary["name"] = "8D건조망고"
print("name",dictionary["name"])
print()

print("==딕셔너리에 요소 추가하기==")
dictionary={}
print("요소 추가 이전",dictionary)
dictionary["name"]="새로운이름"
dictionary["head"]="새로운정신"
dictionary["body"]="새로운몸"
print("요소 추가 이후",dictionary)



#딕셔너리에 요소 추가 할때는 key:value를 []를 통해 추가함.
#딕셔너리 삭제할때는 del 키워드 사용
del dictionary["name"]
print(dictionary)
#딕셔너리에 없는 키를 dict_a[key]형태로 사용하면 키에러 발생

#딕셔너리 in 키워드
if "a" in dict_a:
    print("존재한다")


#dictionary의 키 검색 방법 : get()함수
#dict_a["a"]
#=> 키가 없다면 에러발생 , 키가 있다면 값이 조회됨.
#get(키)에서 키가 존재하지 않으면 None이 리턴되고 정상 종료됨(에러X)

print()
print("==키가 존재하는지 확인하고 값에 접근하기==")
#딕셔너리를 선언합니다

dictionary={
    "name":"건조망고",
    "type":"당절임",
    "ingredient":["망고","설탕","치자황색소"],
    "origin":"필리핀"
}
#존재하지 않는 키에 접근합니다
value = dictionary.get("존재하지 않는 키")
print("값",value)
#none확인 방법
if value==None:
    print("존재하지 않는 키에 접근했습니다")


for i in dict_a:
    print(i)

#for 반복문으로 딕셔너리를 대상으로 돌리면 => 딕셔너리의 키들을 얻을 수 있다.

print()
print("==228p3번==")
numbers=[1,2,6,8,4,3,6,5,7,9,8,8,4,7,3,3]
counter={} #딕셔너리 내부 키 검사 방법? get()None
for number in numbers:
    if counter.get(number)==None:
        counter[number]=1 #딕셔너리에 새로운 요소 추가 하는 방법
    else:
        counter[number]=counter[number]+1
print(counter) #{1: 1, 2: 1, 6: 2, 8: 3, 4: 2, 3: 3, 5: 1, 7: 2, 9: 1}출력됨
print()
print("==229p4번==")
character={
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게베기","아주세게베기"]
}

for key in character:
        if type(character[key]) is list:
            for i in character[key]:
                print("{},{}".format(key,i))
        elif type(character[key]) is dict:
            for i in character[key]:
                print("{},{}".format(i,character[key][i]))
        else:
            print("{},{}".format(key,character[key]))

