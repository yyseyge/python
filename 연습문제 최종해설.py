#for if 타입체크 문자열 숫자 연산 딕셔너리 인덱싱등 배움
#딕셔너리를 만드는데 학생이라는 딕셔너리 만들거임
#학생딕셔너리에는 다섯명의 학생 정보가 있다.
#학생 정보 종류에는 이름/나이/학년/전공(전공종류는 국어 영어 수학 컴공)/성적(국영수컴에 대한) 1-100까지
#사용자 입력을 통해서 총 장학금 액수 입력한다
#사용자 입력을 통해 장학금 지급 인원 설정
#ex)
#case1)1명으로 설정하는 경우 장학금 100% 지원
#case2)2명일경우 50%50%
#case3)3명일 경우 40%40%20%
#case4)4명 25%씩
#case5)5명일 경우 20%씩
#비전공과목의 점수는 10% 가산해준다.(최대100점으로)
#장학금은 성적의 평균으로 지급한다.
#출력: 총 장학금 ~~~이여서, X명한테 지급 , ~~~학생이 ~~~를 받았다.

s1={ "name":"홍길동",
    "age":23,
    "grade":3,
    "major":"국어",
    "score":{
        "국어":80,
        "영어":72,
        "수학":50,
        "컴퓨터":52
    }}
s2={"name":"홍길순",
    "age": 24,
    "grade": 4,
    "major": "영어",
    "score": {
        "국어":40,
        "영어":90,
        "수학":40,
        "컴퓨터":70
    }}
s3={  "name":"김철수",
    "age": 20,
    "grade":1,
    "major":"컴공",
    "score": {
        "국어":50,
        "영어":12,
        "수학":88,
        "컴퓨터":90
    }}
s4={  "name":"김영희",
    "age": 21,
    "grade":2,
    "major":"영어",
    "score": {
        "국어": 20,
        "영어": 38,
        "수학": 20,
        "컴퓨터": 70
    }}
s5={  "name": "한지민",
    "age": 25,
    "grade": 4,
    "major": "수학",
    "score": {
        "국어": 50,
        "영어": 20,
        "수학": 70,
        "컴퓨터": 70
    }}
ratio=[[100],[50,50],[40,40,20],[25,25,25,25],[20,20,20,20,20]]
stu_list=[s1,s2,s3,s4,s5]
sum=0 #학생의 국영수컴 점수를 누적합산 위한 임시 변수
score=0#최대 점수를 기억하기 위한 임시변수
who=0#최대 점수의 주인을 기억하기 위한 변수
rank_list=[]# 누가 제일 점수가 높은지 1등부터 순차적으로 나열해주기 위한 리스트
A=int(input("장학금얼마?"))
B=int(input("몇명"))#B라는 변수를 사용하면 B-1하면 ratio의 원하는 비율의 인덱스를 얻을 수 잇다.

for i in stu_list: #성적 평균내는 for문,학생 정보 하나하나가 i에 담겨서 학생 수 만큼 반복함
    for j in i['score']: #학생i[성적]만 프린트하면 성적:{'국어':39,'수학':50...}이런식으로 나오는데 for문 돌려서 j에 하나씩 넣으면 국어 영어 수학 컴터 따로 과목명이 출력됨 즉 성적 딕셔너리의 어떤 과목의 value값을 원하면 i['성적'][j]하면 됨
        if i['major']!=j: # 성적 가산을 위하여 전공과 성적과목이 일치하는 지 확인해야함 i['major']은 학생의 전공 value를 뜻하고 j는 국어 영어 수학 컴터의 정보가 하나씩 4번 들어올거임
            if i['score'][j]*1.1>100: #만약 전공과 과목이 다르면 그 과목 점수에 10%를 가산해주는데 거기서 또 그 가산점이 100을 넘으면 100점으로 치고 sum에 더해줌
                sum=sum+100 # 학생 한명의 한과목의 점수가 sum에  저장됨, 그럼 다시 for문 첫번째로 가서 두번째 학생불러오고 두번쨰 학생 점수도 따로 저장해야하기 떄문에
            else:
                sum+=i['score'][j]*1.1

        else:# 전공과목은 가산없이 그냥 과목 성적을 저장함
            sum+=i['score'][j] # 학생 한명의 한과목의 점수가 sum에  저장됨

    #lista.append(int(sum/4)) # 여기서 학생 1의 성적/4 즉 평균을 lista에 저장 한 후
    i['총점']=int(sum) #i학생의 모든 과목 가산 적용 완료 후 총점을 i학생의 총점 key값의 value로 할당함. 위에 있는 학생 딕셔너리 각각에 '총점'이 키가되고 int(sum)이 value됨
    sum=0 # i를 통해 지목된 학생 한명에 대한 성적 합산이 끝나고 변수를 초기화 즉 sum을 0으로 초기화 시킨다.

for j in range(B): #등수를 나열하는 for문 #int는 for문에 들어갈 수 없어서 for i in B하면 에러남, B가 int이기 때문에,range함수를 써야지 for문에 들어갈 수 있음
    for i in stu_list: #stu_list중에서 임시로 제일 앞에 있는 학생부터 한명씩 뽑아서 i에 넣어줌
        if i['총점']>score: #들어온학생 한명 총점을 조회함, 첫바퀴때 비교 대상이 필요해서 위에 (score변수를 0으로 설정함) score변수와 비교함
            score=i['총점'] #score에 첫번째 들어온 학생의 총점을 저장하여 다음 바퀴때부터는 score는 첫번째 학생의 총점(ex370)이 됨.
            who=stu_list.index(i) #값을가지고 최고점수를 기억하는것은 위에서 score=i[총점]으로 저장하고 있는데, 누구인지 기억하기 위해 최고점수가 나오면 i학생의 stu_list 인텍스번호로 기억해서 who변수에 저장함
    rank_list.append(stu_list.pop(who))#학생 수 만큼 다돌고 who에 저장된 성적제일높은 한명을 stu_list에서 빼서 rank_list에 넣고 첫번째 for문으로 들어감 그다음부턴 4명이 들어옴
    score=0 #만들어져 있는 변수에 값을 재할당하는 코드이다.
    who=0# 그러고 다시 score, who를 초기화 한 후 for i in range(B)로 돌아가서 내가 몇명 뽑을건지에 대한 범위만큼 돌아감
for i in range(len(ratio[B-1])): # 출력용도
    print("{}등 이름{},총점{}으로 장학금{}%지급 => {}원".format(i+1,rank_list[i]['name'],rank_list[i]['총점'],ratio[B-1][i],int((ratio[B-1][i]*A)/100)))
    #i+1의 의미는 i는 예를들어 장학금 3명 받는다고 하면 i에는 0 1 2가 들어옴 즉 0이 처음들어오면  1등,


