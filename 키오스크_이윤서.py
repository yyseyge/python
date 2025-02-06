import datetime
from unicodedata import category
#시간대별 활성화 되는 카테고리 속성값을 부여
cate={"버거":[2],"맥런치":[1],"맥모닝":[0],"해피스낵":[2],"사이드":[2],"디저트":[2],"맥카페":[2],"음료":[2],"해피밀":[2],"처음으로":[4]}
#0.가격  1. 카테고리 별 속성  3.소분류 속성(비프/치킨, 해피밀오전/오후)
menu={"버거":{"더블쿼터파운더치즈":[6000,0,0,0],"쿼터파운더치즈":[5000,0,0,0],"불고기버거":[3000,0,0,0],"더블불고기":[3500,0,0,0],"빅맥":[4500,0,0,0],"치즈버거":[3000,0,0,0],"베이컨토마토디럭스":[5000,0,0,0],"햄버거":[2500,0,0,0],"맥스파이시상하이":[5500,0,1,0],"맥치킨":[4500,0,1,0],"맥크리스피디럭스":[6000,0,1,0]},
      "맥런치":{"빅맥세트":[5500,1,2,1],"더블불고기세트":[4500,1,2,1],"베이컨토마토디럭스세트":[6000,1,2,1]},
      "맥모닝":{"애그맥머핀":[2800,2,2,2],"소시지에그맥머핀":[3000,2,2,2],"베이컨에그맥머핀":[3300,2,2,2],"치킨맥머핀":[3000,2,2,2]},
      "해피스낵":{"드립커피M":[1000,3,2,3],"제로콜라M":[1000,3,2,3],"치즈버거":[2000,3,2,3],"치즈스틱2조각":[2000,3,2,3],"후렌치후라이S":[1000,3,2,3]},
      "사이드":{"맥윙2조각":[2000,4,2,4],"맥윙4조각":[3500,4,2,4],"맥윙8조각":[6000,4,2,4],"치즈스틱2조각":[2000,4,2,4],"치즈스틱4조각":[3800,4,2,4],"후렌치후라이S":[1000,4,2,4],"후렌치후라이M":[1500,4,2,4],"후렌치후라이L":[2000,4,2,4],"맥너겟4조각":[2000,4,2,4],"맥너겟6조각":[2800,4,2,4]},
      "디저트":{"맥플러리":[3000,5,2,5],"아이스크림콘":[1000,5,2,5]},
      "맥카페":{"카페라떼":[2000,6,2,6],"아이스카페라떼":[2000,6,2,6],"아이스드립커피":[1000,6,2,6],"드립커피":[1000,6,2,6]},
      "음료":{"콜라M":[1000,7,2,7],"콜라L":[1500,7,2,7],"콜라제로M":[1000,7,2,7],"콜라제로L":[1500,7,2,7],"사이다M":[1000,7,2,7],"사이다L":[1500,7,2,7],"오렌지주스":[1000,7,2,7],"생수":[1000,7,2,7]},
      "해피밀":{"애그맥머핀":[4000,8,3,8],"소시지에그맥머핀":[4200,8,3,8],"베이컨에그맥머핀":[4500,8,3,8],"치즈버거":[4200,9,4,8],"햄버거":[3800,9,4,8],"불고기버거":[4200,9,4,8]},
      "세트사이드": {"감자튀김": [4, 10, 10,9], "치즈스틱": [4, 10, 10,9], "어니언링": [4, 10, 10,9]},
      "세트음료": {"콜라": [5, 11,11,10], "사이다": [5, 11, 11,10], "환타": [5, 11, 11,10]},
      "해피밀 사이드": {"파인애플": [2, 7, 7, 13]},
      "해피밀 음료": {"오렌지주스": [3, 7, 7, 14], "생수": [3, 7, 7, 14]},
      "이전으로":{"이전으로":[0,9,9,11]},
      "처음으로":{"처음으로":[1,8,8,12]}}
counter={} #장바구니 역할
counterb={}
counterc={}
key=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lista=[]
count=0 #자동 넘버링 시스템
s=0 #이전으로 돌아가기 위한 count변수
ss=0 #처음으로 돌아가기 위한 count변수
e = "==메뉴선택=="
t = "==1.세트 2.단품 3.처음 4.이전=="
r = "==세트고정=="
sz = "==1.기본 2.라지 3.처음 4.이전 5.취소=="
y = "숫자로 선택"
while key[0]==0: #처음으로 돌아올 수 있게
    key[9] = 0
    key[8] = 0
    key[7] = 0
    key[6] = 0
    key[5] = 0
    key[4] = 0
    key[3] = 0
    key[2] = 0
    key[1] = 0
    count=0
    print("==주문하기 1번==") #첫 주문 입력
    input(y)
    print("==식사 장소를 선택하세요(1.매장 2.포장 3.처음으로)==") #매장 or 포장 입력
    x=int(input(y))
    if x ==3:
        continue
    while key[1]==0: #메뉴 선택중 이전으로 가서 카테고리 다시 보고 싶을때 돌아오는 구간

        key[9] = 0
        key[8] = 0
        key[7] = 0
        key[6] = 0
        key[5] = 0
        key[4] = 0
        key[3] = 0
        key[2] = 0
        count = 0
        now=datetime.datetime.now()
        print("==카테고리를 선택해 주세요==")
        if 4 <= now.hour < 10:# 시간대별로 변수를 다르게 저장함
            a=1
        if 10 <= now.hour < 14:
            a=2
        if 14 <= now.hour or now.hour < 4:
            a=3
        if a == 1: #시간구간 1일 경우 보여지는 카테고리
            for i in cate:
                if cate[i][0] == 0 or cate[i][0] == 2 or cate[i][0] == 4:
                    count += 1
                    print(count, i)
        if a==2: #시간구간 2일 경우 보여지는 카테고리
            for i in cate:
                if cate[i][0] >= 1:
                    count += 1
                    print(count, i)
        if a == 3: #시간구간 3일 경우 보여지는 카테고리
            for i in cate:
                if cate[i][0] >= 2:
                    count += 1
                    print(count, i)
        if counter.get('메뉴이름') == None:  # 장바구니에 어떤 메뉴가 담겨있는지 확인해서 결제 탭 활성화 시키는 부분
            pass
        else:
            print("결제 하시겠습니까?")
            j=int(input("1.결제 2.더 담기: "))
            if j==1:
                print(counter)
                if counterb.get(counter['메뉴이름'])==None:
                    pass
                else:
                    for i in counterb:
                        if counter['메뉴이름'] in counterb[i]:
                            print(counterb[i][0])
            if j==2:
                if counterc.get(counter)==None:
                    counterc=counter
        count=0
        n=input(y) #카테고리 선택
        if n=="1": #만약 버거 카테고리 선택했으면
            print("==1.전체보기 2.비프버거 3.치킨버거 중 선택해주세요==") #버거는 소분류 있어서 나눠줘야함
            m = input(y) #버거의 소분류 선택
            if m=="1": #전체버거 다보여줌
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1]==0:
                            count += 1
                            print(count,j)
                            lista.append(j)
                            if counterb.get(j)==None:
                                counterb[j]=menu[i][j]
            if m=="2": #비프버거만 보여줌
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][2] == 0:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j)==None:
                                counterb[j]=menu[i][j]

            if m == "3": #치킨버거만 보여줌
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][2] == 1:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j)==None:
                                counterb[j]=menu[i][j]
            if m>="1": #처음으로 보여줌
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][0] == 0: #menu에 이전으로가 보여지는 코드
                            count += 1
                            s=count
                            print(count, j)
                        if menu[i][j][0] == 1:#menu에 처음으로가 보여지는 코드
                            count += 1
                            ss=count
                            print(count, j)
        count = 0
        if n=="2": #카테고리 2 선택했을 때 시간별로 나오는 메뉴
            if a == 1:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 2:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j)==None:
                                counterb[j]=menu[i][j]
            if a==2:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 1:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
            if a == 3:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 3:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
            if a>=1:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][0] == 0:
                            count += 1
                            s = count
                            print(count, j)
                        if menu[i][j][0] == 1:#menu에 처음으로가 보여지는 코드
                            count += 1
                            ss=count
                            print(count, j)
            count = 0
        if n == "3":#카테고리 3 선택했을 때 시간별로 나오는 메뉴
            if a<=2:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 3:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j)==None:
                                counterb[j]=menu[i][j]
                            if menu[i][j][0] == 0:  # 이전으로 가는 코드
                                count += 1
                                s = count
                                print(count, j)
                            if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                                count += 1
                                ss = count
                                print(count, j)
            if a==3:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 4:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
                        if menu[i][j][0] == 0:  # 이전으로 가는 코드
                            count += 1
                            s = count
                            print(count, j)
                        if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                            count += 1
                            ss = count
                            print(count, j)
            count = 0
        if n == "4": #카테고리 4선택했을 때 시간별로 나오는 메뉴
            if a <= 2:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 4:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j)==None:
                                counterb[j]=menu[i][j]
            if a == 3:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 5:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
            if a>=1:
                for i in menu:
                    for j in menu[i]:
                         if menu[i][j][0] == 0:
                            count += 1
                            s=count
                            print(count, j)
                         if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                             count += 1
                             ss = count
                             print(count, j)
            count = 0
        if n == "5": #카테고리 5선택했을 때 시간별로 나오는 메뉴
            if a <= 2:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 5:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
                        if menu[i][j][0] == 0:
                            count += 1
                            s = count
                            print(count, j)
                        if menu[i][j][0] == 1:#menu에 처음으로가 보여지는 코드
                            count += 1
                            ss=count
                            print(count, j)
            if a == 3:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 6:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
                        if menu[i][j][0] == 0:
                            count += 1
                            s = count
                            print(count, j)
                        if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                            count += 1
                            ss = count
                            print(count, j)
            count = 0
        if n == "6": #카테고리 6선택했을 때 시간별로 나오는 메뉴
            if a <= 1:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 6:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
                        if menu[i][j][0] == 0:
                            count += 1
                            s = count
                            print(count, j)
                        if menu[i][j][0] == 1:#menu에 처음으로가 보여지는 코드
                            count += 1
                            ss=count
                            print(count, j)
            if a == 3:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][1] == 7:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
            count = 0
        if n == "7": #카테고리 7선택했을 때 시간별로 나오는 메뉴
            if a <= 1:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][3] == 7:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
                        if menu[i][j][0] == 0:
                            count += 1
                            s = count
                            print(count, j)
                        if menu[i][j][0] == 1:#menu에 처음으로가 보여지는 코드
                            count += 1
                            ss=count
                            print(count, j)
            if a == 3:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][2] == 4:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
            count = 0
        if n == "8": #카테고리 8선택했을 때 시간별로 나오는 메뉴
            if a == 1:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][2] == 3:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
            if a == 2:
                for i in menu:
                    for j in menu[i]:
                        if menu[i][j][2] == 4:
                            count += 1
                            print(count, j)
                            lista.append(j)
                            if counterb.get(j) == None:
                                counterb[j] = menu[i][j]
            if a ==3:
                key[1] = 1
                break
            count = 0
        if n == "9": #카테고리 9선택하면 처음으로 돌아가기
            lista.clear()
            break
        print(e) # 메뉴 선택 메세지 출력
        h = int(input(y)) # 메뉴 선택 입력
        if h == s:
            lista.clear()
            continue # 메뉴 선택하려다가 이전으로 돌아가는 코드
        if h==ss:
            lista.clear()
            key[1]=1
            break # 메뉴 선택하려다가 처음으로 가는 코드
        print(lista[h - 1], "을/를 선택했습니다")
        if counter.get(lista[h - 1]) == None:
            counter['메뉴이름']= lista[h - 1]
            counter['수량']=1
            print(counter)  # 장바구니에 뭐 담겼는지 보여주는 코\드
        while key[2]==0:
            for i in counterb:
                if key[3] == 0:
                    if counterb[i][3]==3 or counterb[i][3]==4 or counterb[i][3]==5 or counterb[i][3]==6 or counterb[i][3]==7:
                        print("옵션 수정")
                        re = int(input(" 1.수량  2.장바구니  3.취소 4.처음으로:  "))
                        if re == 2:
                            print("장바구니에 담습니다.")
                            key[4]=1
                            key[3]=1
                            key[2]=1
                            break
                        if re ==1:
                            print("수량 선택하세요")
                            x=int(input())
                            counter['수량']=x
                            print(counter)
                            continue
                        if re == 3:
                            key[4] = 1
                            key[3] = 1
                            key[2] = 1
                            lista.clear()
                            counter.clear()
                            break
                        if re == 4:
                            key[4] = 1
                            key[3] = 1
                            key[2] = 1
                            key[1] = 1
                            lista.clear()
                            counter.clear()
                            break
            while key[4] == 0:  # 세트 단품 선택
                for i in counterb:
                    if key[5] == 0:
                        key[6]=0
                        if counterb[i][3]==0 or counterb[i][3]==2:
                            print(t)  # 세트 단품 처음 이전으로 중 선택하라는 메세지 출력
                            xx = input(y)  # 입력
                            if xx=="2":
                                print("옵션 수정")
                                re = int(input(" 1.수량  2.장바구니  3.취소 4.처음으로:  "))
                                if re == 1:
                                    print(counter)
                                    print("수량을 선택하세요")
                                    x=int(input())
                                    counter['수량'] = x
                                    print(counter)
                                    continue
                                if re == 2:
                                    print("장바구니에 담습니다.")
                                    key[5]=1
                                    key[4]=1
                                    key[3]=1
                                    key[2]=1
                                    break
                                if re == 3:
                                    key[5] = 1
                                    key[4] = 1
                                    key[3] = 1
                                    key[2] = 1
                                    lista.clear()
                                    counter.clear()
                                    break
                                if re == 4:
                                    key[5] = 1
                                    key[4] = 1
                                    key[3] = 1
                                    key[2] = 1
                                    key[1] = 1
                                    lista.clear()
                                    counter.clear()
                                    break
                            if xx == "3":  # 세트 단품 처음 이전 중 입력값이 처음으로면 처음
                                lista.clear()
                                counter.clear()
                                key[5] = 1
                                key[4] = 1
                                key[3] = 1
                                key[2] = 1
                                key[1] = 1
                                break
                            if xx == "4":  # 세트 단품 처음 이전 중 입력값이 이전이면 이전
                                lista.clear()
                                counter.clear()
                                key[5] = 1
                                key[4] = 1
                                key[3] = 1
                                key[2] = 1
                                break
                            if xx == "1":  # 입력값이 세트면
                                while key[6] == 0:
                                    key[7] = 0
                                    print(sz)  # 기본 라지 이전 처음으로 중  선택하라는 메세지 출력
                                    h = input(y)  # 사이즈 입력
                                    if h == "3":  # 사이즈 선택시 처음으로 가는 코드
                                        lista.clear()
                                        counter.clear()
                                        key[6] = 1
                                        key[5] = 1
                                        key[4] = 1
                                        key[3] = 1
                                        key[2] = 1
                                        key[1] = 1
                                        break
                                    elif h == "4":  # 사이즈 선택시 이전으로 가는 코드
                                        key[6] = 1
                                        break
                                    elif h == "5":  # 사이즈 선택하다가 취소 누르면 카테고리 보여주는 코드
                                        lista.clear()
                                        counter.clear()
                                        key[6] = 1
                                        key[5] = 1
                                        key[4] = 1
                                        key[3] = 1
                                        key[2] = 1
                                        break
                                    if h <= "2":  # 기본 혹은 라지 사이즈 선택시
                                        while key[7] == 0:
                                            key[8] = 0

                                            print("==세트메뉴 사이드와 음료를 골라주세요==")  # 세트메뉴의 사이드와 음료 선택
                                            lista.clear()
                                            for i in menu:  # 사이드 메뉴 먼저 보여줌
                                                for j in menu[i]:
                                                    if menu[i][j][1] == 10:
                                                        count += 1
                                                        print(count, j)
                                                        lista.append(j)
                                                    if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                                                        count += 1
                                                        ss = count
                                                        print(count, j)
                                                    if menu[i][j][0] == 0:  # 이전으로 가는 코드
                                                        count += 1
                                                        s = count
                                                        print(count, j)

                                            print(e)  # 세트 사이드 고르는 메세지 출력
                                            h = int(input(y))  # 세트 사이드 입력
                                            if h == ss:
                                                lista.clear()
                                                counter.clear()
                                                key[7] = 1
                                                key[6] = 1
                                                key[5] = 1
                                                key[4] = 1
                                                key[3] = 1
                                                key[2] = 1
                                                key[1] = 1
                                                break
                                            if h == s:
                                                lista.clear()
                                                counter.clear()
                                                key[7] = 1
                                                break
                                            print(lista[h - 1], "을/를 선택했습니다")
                                            if counter.get(lista[h - 1]) == None:
                                                counter['사이드'] = lista[h - 1]
                                            count = 0
                                            lista.clear()
                                            while key[8] == 0:
                                                for i in menu:  # 음료메뉴 보여줌
                                                    for j in menu[i]:
                                                        if menu[i][j][1] == 11:
                                                            count += 1
                                                            print(count, j)
                                                            lista.append(j)
                                                        if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                                                            count += 1
                                                            ss = count
                                                            print(count, j)
                                                        if menu[i][j][0] == 0:  # 이전으로 가는 코드
                                                            count += 1
                                                            s = count
                                                            print(count, j)
                                                print(e)  # 세트 음료 고르는 메세지 출력
                                                h = int(input(y))  # 세트 음료 입력
                                                if h == ss:
                                                    lista.clear()
                                                    counter.clear()
                                                    key[8] = 1
                                                    key[7] = 1
                                                    key[6] = 1
                                                    key[5] = 1
                                                    key[4] = 1
                                                    key[3] = 1
                                                    key[2] = 1
                                                    key[1] = 1
                                                    break
                                                if h == s:
                                                    lista.clear()
                                                    counter.clear()
                                                    key[8] = 1
                                                    break
                                                print(lista[h - 1], "을/를 선택했습니다")
                                                if counter.get(lista[h - 1]) == None:
                                                    counter['음료'] = lista[h - 1]
                                                while key[9] == 0:
                                                    print("==현재 입력하신 메뉴 정보 입니다.==")
                                                    print(counter)
                                                    print("옵션 수정")
                                                    re = int(input("1.사이드 2.음료 3.수량  4.장바구니  5.취소 6.처음으로:  "))
                                                    count = 0
                                                    if re == 1:
                                                        lista.clear()
                                                        for i in menu:
                                                            for j in menu[i]:
                                                                if menu[i][j][3] == 9:
                                                                    count += 1
                                                                    print(count, j)
                                                                    lista.append(j)
                                                        print(e)  # 세트 사이드 고르는 메세지 출력
                                                        h = int(input(y))  # 세트 사이드 입력
                                                        print(lista[h - 1], "을/를 선택했습니다")
                                                        if counter.get(lista[h - 1]) == None:
                                                            counter['사이드'] = lista[h - 1]
                                                        count = 0
                                                    if re == 2:
                                                        lista.clear()
                                                        for i in menu:
                                                            for j in menu[i]:
                                                                if menu[i][j][3] == 10:
                                                                    count += 1
                                                                    print(count, j)
                                                                    lista.append(j)
                                                        print(e)  # 세트 음료 고르는 메세지 출력
                                                        h = int(input(y))  # 세트 음료 입력
                                                        print(lista[h - 1], "을/를 선택했습니다")
                                                        if counter.get(lista[h - 1]) == None:
                                                            counter['음료'] = lista[h-1]
                                                    if re == 4:
                                                        key[9]=1
                                                        key[8]=1
                                                        key[7]=1
                                                        key[6]=1
                                                        key[5]=1
                                                        key[4]=1
                                                        key[3]=1
                                                        key[2]=1
                                                    if re ==5:
                                                        key[9] = 1
                                                        key[8] = 1
                                                        key[7] = 1
                                                        key[6] = 1
                                                        key[5] = 1
                                                        key[4] = 1
                                                        key[3] = 1
                                                        key[2] = 1
                                                    if re ==6:
                                                        key[9] = 1
                                                        key[8] = 1
                                                        key[7] = 1
                                                        key[6] = 1
                                                        key[5] = 1
                                                        key[4] = 1
                                                        key[3] = 1
                                                        key[2] = 1
                                                        key[1] = 1
                for i in counterb:
                    if counterb[i][3] == 1:
                        if key[5]==0:
                            while key[6] == 0:
                                key[7] = 0
                                print(sz)  # 기본 라지 이전 처음으로 중  선택하라는 메세지 출력
                                h = input(y)  # 사이즈 입력
                                if h == "3":  # 사이즈 선택시 처음으로 가는 코드
                                    lista.clear()
                                    counter.clear()
                                    key[6] = 1
                                    key[5] = 1
                                    key[4] = 1
                                    key[3] = 1
                                    key[2] = 1
                                    key[1] = 1
                                    break
                                elif h == "4":  # 사이즈 선택시 이전으로 가는 코드
                                    key[6] = 1
                                    break
                                elif h == "5":  # 사이즈 선택하다가 취소 누르면 카테고리 보여주는 코드
                                    lista.clear()
                                    counter.clear()
                                    key[6] = 1
                                    key[5] = 1
                                    key[4] = 1
                                    key[3] = 1
                                    key[2] = 1
                                    break
                                if h <= "2":  # 기본 혹은 라지 사이즈 선택시
                                    while key[7] == 0:
                                        key[8] = 0

                                        print("==세트메뉴 사이드와 음료를 골라주세요==")  # 세트메뉴의 사이드와 음료 선택
                                        lista.clear()
                                        for i in menu:  # 사이드 메뉴 먼저 보여줌
                                            for j in menu[i]:
                                                if menu[i][j][1] == 10:
                                                    count += 1
                                                    print(count, j)
                                                    lista.append(j)
                                                if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                                                    count += 1
                                                    ss = count
                                                    print(count, j)
                                                if menu[i][j][0] == 0:  # 이전으로 가는 코드
                                                    count += 1
                                                    s = count
                                                    print(count, j)

                                        print(e)  # 세트 사이드 고르는 메세지 출력
                                        h = int(input(y))  # 세트 사이드 입력
                                        if h == ss:
                                            lista.clear()
                                            counter.clear()
                                            key[7] = 1
                                            key[6] = 1
                                            key[5] = 1
                                            key[4] = 1
                                            key[3] = 1
                                            key[2] = 1
                                            key[1] = 1
                                            break
                                        if h == s:
                                            lista.clear()
                                            counter.clear()
                                            key[7] = 1
                                            break
                                        print(lista[h - 1], "을/를 선택했습니다")
                                        if counter.get(lista[h - 1]) == None:
                                            counter['사이드'] = lista[h - 1]
                                        count = 0
                                        lista.clear()
                                        while key[8] == 0:
                                            for i in menu:  # 음료메뉴 보여줌
                                                for j in menu[i]:
                                                    if menu[i][j][1] == 11:
                                                        count += 1
                                                        print(count, j)
                                                        lista.append(j)
                                                    if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                                                        count += 1
                                                        ss = count
                                                        print(count, j)
                                                    if menu[i][j][0] == 0:  # 이전으로 가는 코드
                                                        count += 1
                                                        s = count
                                                        print(count, j)
                                            print(e)  # 세트 음료 고르는 메세지 출력
                                            h = int(input(y))  # 세트 음료 입력
                                            if h == ss:
                                                lista.clear()
                                                counter.clear()
                                                key[8] = 1
                                                key[7] = 1
                                                key[6] = 1
                                                key[5] = 1
                                                key[4] = 1
                                                key[3] = 1
                                                key[2] = 1
                                                key[1] = 1
                                                break
                                            if h == s:
                                                lista.clear()
                                                counter.clear()
                                                key[8] = 1
                                                break
                                            print(lista[h - 1], "을/를 선택했습니다")
                                            if counter.get(lista[h - 1]) == None:
                                                counter['음료'] = lista[h - 1]
                                            while key[9] == 0:
                                                print("==현재 입력하신 메뉴 정보 입니다.==")
                                                print(counter)
                                                print("옵션 수정")
                                                re = int(input("1.사이드 2.음료 3.수량  4.장바구니  5.취소 6.처음으로:  "))
                                                count = 0
                                                if re == 1:
                                                    lista.clear()
                                                    for i in menu:
                                                        for j in menu[i]:
                                                            if menu[i][j][3] == 9:
                                                                count += 1
                                                                print(count, j)
                                                                lista.append(j)
                                                    print(e)  # 세트 사이드 고르는 메세지 출력
                                                    h = int(input(y))  # 세트 사이드 입력
                                                    print(lista[h - 1], "을/를 선택했습니다")
                                                    if counter.get(lista[h - 1]) == None:
                                                        counter['사이드'] = lista[h - 1]
                                                    count = 0
                                                if re == 2:
                                                    lista.clear()
                                                    for i in menu:
                                                        for j in menu[i]:
                                                            if menu[i][j][3] == 10:
                                                                count += 1
                                                                print(count, j)
                                                                lista.append(j)
                                                    print(e)  # 세트 음료 고르는 메세지 출력
                                                    h = int(input(y))  # 세트 음료 입력
                                                    print(lista[h - 1], "을/를 선택했습니다")
                                                    if counter.get(lista[h - 1]) == None:
                                                        counter['음료'] = lista[h - 1]
                                                if re == 4:
                                                    key[9] = 1
                                                    key[8] = 1
                                                    key[7] = 1
                                                    key[6] = 1
                                                    key[5] = 1
                                                    key[4] = 1
                                                    key[3] = 1
                                                    key[2] = 1
                                                if re == 5:
                                                    key[9] = 1
                                                    key[8] = 1
                                                    key[7] = 1
                                                    key[6] = 1
                                                    key[5] = 1
                                                    key[4] = 1
                                                    key[3] = 1
                                                    key[2] = 1
                                                if re == 6:
                                                    key[9] = 1
                                                    key[8] = 1
                                                    key[7] = 1
                                                    key[6] = 1
                                                    key[5] = 1
                                                    key[4] = 1
                                                    key[3] = 1
                                                    key[2] = 1
                                                    key[1] = 1
                for i in counterb:
                    if key[7] == 0:
                        key[4] = 0
                        if counterb[i][3] == 1:
                            while key[3] == 0:
                                key[4] = 0
                                print(r)  # 세트 고정 메세지 출력
                                print(sz)  # 기본 라지 이전 처음으로 중  선택하라는 메세지 출력
                                h = int(input(y))
                                if h == 3:  # 처음으로 가는 코드
                                    lista.clear()
                                    counter.clear()
                                    key[7] = 1
                                    key[3] = 1
                                    key[2] = 1
                                    key[1] = 1
                                    break
                                if h == 4:  # 이전으로 가는 코드
                                    key[7] = 1
                                    key[3] = 1
                                    key[2] = 1
                                    lista.clear()
                                    counter.clear()
                                    continue
                                if h == 5:  # 사이즈 선택하다가 취소 누르면 카테고리 보여주는 코드
                                    lista.clear()
                                    counter.clear()
                                    key[3] = 1
                                    key[2] = 1
                                    key[7] = 1
                                    break
                                if h <= 2:  # 기본 혹은 라지 사이즈 선택시
                                    while key[4] == 0:
                                        key[5] = 0
                                        print("세트메뉴 사이드와 음료를 골라주세요")  # 세트메뉴의 사이드와 음료 선택
                                        for i in menu:  # 사이드 메뉴 먼저 보여줌
                                            for j in menu[i]:
                                                if menu[i][j][3] == 9:
                                                    count += 1
                                                    print(count, j)
                                                    lista.append(j)
                                                if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                                                    count += 1
                                                    ss = count
                                                    print(count, j)
                                                if menu[i][j][0] == 0:  # 이전으로 가는 코드
                                                    count += 1
                                                    s = count
                                                    print(count, j)
                                        print(e)  # 세트 사이드 고르는 메세지 출력
                                        h = int(input(y))  # 세트 사이드 입력
                                        if h == ss:
                                            lista.clear()
                                            counter.clear()
                                            key[7] = 1
                                            key[4] = 1
                                            key[3] = 1
                                            key[2] = 1
                                            key[1] = 1
                                            break
                                        if h == s:
                                            lista.clear()
                                            counter.clear()
                                            key[4] = 1
                                            break
                                        print(lista[h - 1], "을/를 선택했습니다")
                                        if counter.get(lista[h - 1]) == None:
                                            counter['사이드'] = lista[h - 1]
                                        count = 0
                                        lista.clear()
                                        while key[5] == 0:
                                            for i in menu:  # 음료메뉴 보여줌
                                                for j in menu[i]:
                                                    if menu[i][j][3] == 10:
                                                        count += 1
                                                        print(count, j)
                                                        lista.append(j)
                                                    if menu[i][j][0] == 1:  # menu에 처음으로가 보여지는 코드
                                                        count += 1
                                                        ss = count
                                                        print(count, j)
                                                    if menu[i][j][0] == 0:  # 이전으로 가는 코드
                                                        count += 1
                                                        s = count
                                                        print(count, j)
                                            print(e)  # 세트 음료 고르는 메세지 출력
                                            h = int(input(y))  # 세트 음료 입력
                                            if h == ss:
                                                lista.clear()
                                                counter.clear()
                                                key[7] = 1
                                                key[5] = 1
                                                key[4] = 1
                                                key[3] = 1
                                                key[2] = 1
                                                key[1] = 1
                                                break
                                            if h == s:
                                                lista.clear()
                                                counter.clear()
                                                key[5] = 1
                                                break
                                            print(lista[h - 1], "을/를 선택했습니다")
                                            if counter.get(lista[h - 1]) == None:
                                                counter['음료'] = lista[h - 1]
                                            while key[6] == 0:
                                                print("==현재 입력하신 메뉴 정보 입니다.==")
                                                print(counter)
                                                print("옵션 수정")
                                                re = int(input("1.음료 2.수량  3.장바구니  4.취소 5.처음으로:  "))
                                                count = 0
                                                if re == 1:
                                                    lista.clear()
                                                    for i in menu:
                                                        for j in menu[i]:
                                                            if menu[i][j][0] == 3:
                                                                count += 1
                                                                print(count, j)
                                                                lista.append(j)
                                                    print(e)  # 세트 사이드 고르는 메세지 출력
                                                    h = int(input(y))  # 세트 사이드 입력
                                                    print(lista[h - 1], "을/를 선택했습니다")
                                                    if counter.get(lista[h - 1]) == None:
                                                        counter['음료'] = lista[h - 1]
                                                    count = 0
                                                if re == 3:
                                                    print(counter)
                                                if re == 4:
                                                    lista.clear()
                                                    counter.clear()
                                                    key[6] = 1
                                                    key[5] = 1
                                                    key[4] = 1
                                                    key[3] = 1
                                                    key[2] = 1
                                                    break