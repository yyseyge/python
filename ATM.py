#cash- 사용자가 지니고 있는 금액
#money- atm기기가 가지고 있는 금액


import datetime
import random

class person: #사용자 이름, 통장 , 현재소지금액
    def __init__(self,name,acc,addmoney):
        self.name=name
        self.acc=acc
        self.addmoney = addmoney

    def insert(self,who,addmoney):
        atm.add(who,addmoney)
    def sub(self,who,submoney):
        atm.sub(who,submoney)
    def send(self,sender,receiver,sendmoney):
        atm.send(sender,receiver,sendmoney)
    def balance(self,who):
        atm.bal(who)

a=person("이윤서",[],1000)
b=person("홍길순",[],1000)
c=person("홍길동",[],1000)

class account: #통장 필드는 어디은행인지, 계좌번호, 통장 소유주, 현재 잔액
    def __init__(self,bank,accNum,own,balance):
        self.bank=bank
        self.accNum=accNum
        self.own=own
        self.balance=balance
        self.own.acc.append(self)


account1=account("NH",12341234,a,50000)
account2=account("카카오뱅크",1343234,b,758000)
account3=account("kb",934940393,c,1280000)

class ATM: # ATM 필드 이용가능시간인지, 어디은행 ATM기인지
    def __init__(self,time,cat):
        self.time=True
        self.cat="NH"

    def display(self,who):
        print(who.acc[0].balance)

    def senddis(self,sender):
        print(sender.acc[0].balance)

    def time(self):
        now=datetime.datetime.now()
        if now.hour<7 or now.hour>23:
            self.time=False
        else:
            self.time=True

    def add(self,who,addmoney):
        BankSys.add(self,who,addmoney)

    def sub(self,who,submoney):
        BankSys.sub(self,who,submoney)

    def bal(self,who):
        BankSys.balance(who)

    def send(self,sender,receiver,sendmoney):
        BankSys.send(self,sender,receiver,sendmoney)

atm=ATM(True,"NH")

class BankSys:
    def __init__(self,bank,accNum,own,balance):
        self.bank = bank
        self.accNum = accNum
        self.own = own
        self.balance = balance
        self.own.acc.append(self)

    def add(self,who,addmoney):
       if who.acc[0].bank==atm.cat:
            who.acc[0].balance+=addmoney
            atm.display(who)
       else:
           addmoney-=700
           who.acc[0].balance+=addmoney
           atm.display(who)

    def sub(self,who,submoney):
        if who.acc[0]==atm.cat:
            who.acc[0].balance -= submoney
            atm.display(who)
        else:
            submoney += 700
            who.acc[0].balance-=submoney
            atm.display(who)

    def send(self,sender,receiver,sendmoney):
        sender.acc[0].balance-=sendmoney
        receiver.acc[0].balace+=sendmoney
        atm.senddis(sender)

if atm.time==True:
    b.insert(b,1000)
    b.sub(a,3000)



