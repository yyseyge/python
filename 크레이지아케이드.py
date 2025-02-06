from typing import ItemsView

from fontTools.misc.cython import returns


class character:
    tic_count=0
    stats={
        "up_count" : 0,
        "down_count" : 0,
        "left_count" : 0,
        "right_count" : 0,
        "reverse_count" : 0,
        "bomb_count" : 0,
        "item_count" : 0,
        "damage_count" :0
    }
    result={}

    def __init__(self,x,y,name):
        self.__x=x #캐릭터의 x좌표
        self.__y=y #캐릭터의 y좌표
        self.__speed=1 #캐릭터의 스피드 초기값
        self.__max_speed=3 #캐릭터의 최대 스피드
        self.__hp=3 #캐릭터 체력
        self.__state=True #캐릭터의 사망 여부
        self.__b_count=1 #캐릭터 물풍선 개수
        self.__max_b_count = 3 #캐릭터 최대 물풍선 개수
        self.__b_range=1 #캐릭터 물풍선 범위 초기값
        self.__max_b_range=5 #캐릭터 물풍선 최대 범위
        self.__kick=False #아이템 kick여부
        self.__reverse=0 #아이템 악마 여부
        self.__max_reverse=5 #아이템 악마 스탯 최대값
        self.__name=name

    instance=None
    @classmethod
    def init(cls, x,y):


        return cls(x,y)


    @classmethod
    def tick(cls, **kwargs): #kwargs={m:map}
        if kwargs.get("m")["bomb_hit"] ==True:

          .instance,1)

        for i, j in zip(kwargs.get("m")["movement"], kwargs.get("map")["movecheck"]):
            if i == "w" and j == True:
                cls.set_move_y(cls.instance,1)
            if i == "s" and j == True:
                cls.set_move_y(cls.instance,-1)
            if i == "d" and j == True:
                cls.set_move_x(cls.instance,-1)
            if i == "a" and j == True:
                cls.set_move_x(cls.instance,1)

        if kwargs.get("m")["hit_count"] > 0:
            cls.set_hp(cls.instance,kwargs.get("m")["hit_count"])

        if kwargs.get("m")["bomb"] == True:
            cls.bomb()

        if len(kwargs.get("m")["item"]) != 0:
            cls.item_question(cls.instance,kwargs.get("m")["item"])

        send_info = {["hp"]: cls.__hp, ["speed"]: cls.__speed, ["x"]: cls.__x, ["y"]: cls.__y,["state"]: cls.__state}
        return send_info


    def set_move_x(self,a):
        self.__x-=a
        if self.__reverse >0:
            self.__x+=a
            self.__reverse-=1

    def set_move_y(self,a):
        self.__y+=a


    def itme_question(self,item):
        lista=Item.return_effect(item)
        for i in lista:
            for key,value in lista.items():
                if hasattr(character,key):
                    current_value=getattr(character,key) # current_value라는 변수에 1을 넣어줌

                    if isinstance(value,bool):











    def set_hp(self,damage):
        #데미지를 받았다는 정보를 받으면 실행되는 함수
        self.__hp-=damage
        if self.__hp==0:
            self.__state=False
    def speed(self):
        return self.__speed
    def set_speed(self):
        #아이템을 먹은 상태라는 것이 파악되면
        self.__speed+=1

    def bomb(self):
        print("폭탄")
    #def bomb(self):
    #item.effects(map["item"])

class Item:
    item_list={"스케이트":"speed 1+","bomb+":"b_range 1+"}

    def __init__(self):
        pass
    @classmethod
    def return_effect(self,item):
        for i in item:
            if i =="스케이트":
                pass










aa=character(0,0)
aa.receive(info)

import random
from typing import Any

from bomb import Bomb
from box import Box
from character import Character
from item import Item
from mob import Monster as Mob
from pos import Pos


# 플레ㅣ어별 통계
# 이름, 이동횟수, 틱수, 승률, ...
# 랭킹
class Map:
    def __init__(self):
        self.map_size = [13, 13]  # x y
        self.map_info = []
        self.max_tick = 1000
        self.current_tick = 0

        self.box_dict = {}  # {pos: {hp: int, hit: bool}}
        self.item_dict = {}  # {pos: key}
        self.bomb_dict = {}  # {pos: {owner: str, power: int}}}

        self.char_stat = {}  #
        self.mob_dict = {}  # {boss: [{pos: Pos, hp: int, hit: bool}], minion: [{pos: Pos, hp: int, hit: bool}]}
        self.char_dict = {}

        self.initialize()

    def set_info(self, p: Pos, v):
        self.map_info[p.y][p.x] = v

    def set_box(self, p: Pos, box_id):
        self.map_info[p.y][p.x] = box_id << 2

    def set_item(self, p: Pos, item_id):
        self.map_info[p.y][p.x] = item_id << 5

    def get_info(self, p: Pos) -> Any:
        return self.map_info[p.y][p.x]

    def is_inside(self, p: Pos):
        try:
            self.get_info(p)
            return True
        except IndexError:
            return False

    def all_pos(self):
        return [Pos(x, y) for y in range(self.map_size[0]) for x in range(self.map_size[1])]

    def is_item(self, p: Pos):
        return self.get_info(p) >= 32

    def is_box(self, p: Pos):
        return 32 > self.get_info(p) >= 4

    def is_bomb(self, p: Pos):
        return self.get_info(p) == 2

    def is_water(self, p: Pos):
        return self.get_info(p) == 1

    def is_empty(self, p: Pos):
        return self.get_info(p) == 0

    def item_id(self, p: Pos):
        return self.get_info(p) >> 5

    def box_id(self, p: Pos):
        return (self.get_info(p) >> 2) & 7

    def get_item_id(self, s: str):
        return list(Item.ITEM_TYPES.keys()).index(s)

    def get_item_name(self, p: Pos):
        if self.is_item(p):
            return list(Item.ITEM_TYPES.keys())[self.item_id(p)]
        return None

    def add_bomb(self, name, pos, power):
        self.bomb_dict[pos] = {"owner": name, "power": power}

    def bomb_count(self, name):
        return sum(1 for i in self.bomb_dict if name == self.bomb_dict[i]["owner"])

    ###########################################################################

    def initialize(self):
        self.map_info = [[0 for i in range(self.map_size[0])] for j in range(self.map_size[1])]  # 맵 사이즈

        # 박스&빈 공간
        for i in range(self.map_size[1]):  # y
            for j in range(self.map_size[0]):  # x
                point_num = random.uniform(0, 1)  # 확률
                if point_num > 0.3:  # 70% 박스
                    if point_num <= 0.37:
                        self.map_info[i][j] = 28  # 부서지지 않는 박스 -1
                    elif 0.37 < point_num <= 0.5:
                        self.map_info[i][j] = 12  # 박스 체력 3
                    elif 0.5 < point_num <= 0.7:
                        self.map_info[i][j] = 8  # 박스 체력 2
                    else:
                        self.map_info[i][j] = 4  # 박스 체력 1
                else:  # 아니면 빈 공간
                    self.map_info[i][j] = 0

        # 구역 9개
        for i in range(3):
            for j in range(3):
                self.map_info[(self.map_size[1] // 2) - 1 + j][
                    (self.map_size[0] // 2) - 1 + i] = 0  # 중앙 고정 값(보스) [13][13]
                self.map_info[(self.map_size[1] - 4) + j][(self.map_size[1] - 4) + i] = 0  # 오른쪽 모서리 아래 [23][23]
                self.map_info[(self.map_size[1] - 4) + j][i + 1] = 0  # 왼쪽 모서리 아래 # [23][3]
                self.map_info[j + 1][(self.map_size[1] - 4) + i] = 0  # 오른쪽 모서리 위 [3][23]
                self.map_info[j + 1][i + 1] = 0  # 왼쪽 위 모서리 # [3][3]
                self.map_info[(self.map_size[1] - 4) + j][(self.map_size[0] // 2) - 1 + i] = 0  # 아래 중앙 # [23][13]
                self.map_info[j + 1][(self.map_size[0] // 2) - 1 + i] = 0  # 위 중앙 # [3][13]
                self.map_info[(self.map_size[0] // 2) - 1 + j][i + 1] = 0  # 왼쪽 중앙 # [13][3]
                self.map_info[(self.map_size[0] // 2) - 1 + j][(self.map_size[1] - 4) + i] = 0  # 오른쪽 중앙 # [13][23]

        # 맵 외곽은 부서지지 않는 박스
        for i in range(self.map_size[0]):
            for j in range(self.map_size[0]):
                self.map_info[0][i] = 28  # 윗줄
                self.map_info[-1][i] = 28  # 아랫줄
                self.map_info[j][0] = 28  # 왼쪽줄
                self.map_info[j][-1] = 28  # 오른쪽줄

        # map size 13 13
        # print(i, j)
        # 12 12

        # 각 구역 중앙 값
        A_point = Pos(self.map_size[0] // 2, self.map_size[1] // 2)  # 중앙 보스 [12][12]
        B_point = Pos(self.map_size[0] - 3, 2)  # 오른쪽 모서리 위 [24][0]
        C_point = Pos(self.map_size[0] // 2, 2)  # 위 중앙 [24][12]
        D_point = Pos(2, 2)  # 왼쪽 위 모서리 # [24][24]
        E_point = Pos(2, self.map_size[1] // 2)  # 왼쪽 중앙 [12][24]
        F_point = Pos(self.map_size[0] - 3, self.map_size[1] // 2)  # 오른쪽 중앙 [12][0]
        G_point = Pos(2, self.map_size[1] - 3)  # 왼쪽 모서리 아래 # [0][24]
        H_point = Pos(self.map_size[0] // 2, self.map_size[1] - 3)  # 아래 중앙 [0][12]
        I_point = Pos(self.map_size[0] - 3, self.map_size[1] - 3)  # 오른쪽 모서리 아래 [0][0]

        # point_list = [A_point, B_point, ...]

        ###########################################################################
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                p = Pos(j, i)
                if self.is_box(p):
                    self.box_dict[p] = {"hp": self.box_id(p), "hit": False}
                # print(self.map_info[i][j], end="\t")

        # 박스 id(1~7), 아이템(1~7), 0(없음), 1(물줄기), 2(물풍선)
        # 000 000 00 / 32 4 1
        Box.init([value["hp"] for _, value in self.box_dict.items()])

        # for i in range(self.map_size[0]):
        #     for j in range(self.map_size[1]):
        #         print(self.map_info[i][j], end="\t")
        #     print()

        # 캐릭터
        # 이름 입력받고
        self.char_stat = Character.init(x=G_point.x, y=G_point.y, name="이름")
        print(self.char_stat)

        # 보스 초기화
        # Mob.init(boss_count=1, minion_count=5)
        self.mob_dict = {"boss": [{"pos": A_point, "hp": -1, "hit": False}],
                         "minion": [{"pos": B_point, "hp": -1, "hit": False},
                                    {"pos": C_point, "hp": -1, "hit": False},
                                    {"pos": D_point, "hp": -1, "hit": False},
                                    {"pos": E_point, "hp": -1, "hit": False},
                                    {"pos": F_point, "hp": -1, "hit": False},
                                    ]}
        # mob_a, mob_b = Mob.init(boss_coords=[i["pos"].to_list() for i in self.mob_dict["boss"]], minion_coords=[i["pos"].to_list() for i in self.mob_dict["minion"]])
        Mob.init(boss_coords=[i["pos"].to_list() for i in self.mob_dict["boss"]],
                 minion_coords=[i["pos"].to_list() for i in self.mob_dict["minion"]])
        # for i in range(len(mob_a)):
        for i in range(1):
            self.mob_dict["boss"][i]["hp"] = 11
        # for i in range(len(mob_b)):
        for i in range(5):
            self.mob_dict["minion"][i]["hp"] = 1

        # Mob.init(boss_coords=[[0, 0]], minion_coords=[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])
        pass

    ###########################################################################

    def play(self):
        self.display()
        last_tick = False
        mob_b = [{"move": [0, 0]} for _ in self.mob_dict["minion"]]
        while not last_tick:
            self.current_tick += 1

            self.char_dict = {
                "movement": [],
                "movecheck": [],
                "dropped_item": [],
                "hit_count": 0,
                "bomb": False,

                "bomb_hit": False,
                "clear": False,
                "nowtick": self.current_tick,
            }
            # i = input("test: ")

            # inp = self.inp_user_act()
            aaa = {}
            self.is_movable(self.inp_user_act())
            # print(inp)

            # 이동만
            # 물풍선놓기+이동

            # 직전 틱의 물줄기는 빈칸으로 초기화
            for p in self.all_pos():
                if self.is_water(p):
                    self.set_info(p, 0)

            # 박스 맞음 상태 false로 초기화
            for key in self.box_dict:
                self.box_dict[key]["hit"] = False
            # 몹 맞음 상태 false로 초기화
            for b in self.mob_dict["boss"]:
                b["hit"] = False
            for m in self.mob_dict["minion"]:
                m["hit"] = False

            # 적 실제 이동
            for i in range(len(self.mob_dict["minion"])):
                p = self.mob_dict["minion"][i]["pos"] + Pos.from_list(mob_b[i]["move"])
                if self.is_inside(p) and not (self.is_box(p) or self.is_bomb(p)):
                    self.mob_dict["minion"][i]["pos"] = p

            # 테스트로 물풍선 놓기
            # 캐릭터 물풍선 추가
            if self.current_tick == 1:
                self.add_bomb("player", Pos(6, 6), 3)
                self.add_bomb("player", Pos(3, 3), 1)
            elif self.current_tick == 2:
                self.add_bomb("player", Pos(2, 3), 1)
                pass

            # 캐릭터 실제 이동

            # bomb tick
            bomb_a, bomb_b = Bomb.tick(self.bomb_dict)
            self.bomb_dict = bomb_b

            # 맵에 물풍선 놓기
            for p in self.bomb_dict:
                self.set_info(p, 2)

            # 터짐
            for p in bomb_a:
                for q in self.bomb(p, bomb_a[p]["power"]):
                    if self.is_box(q):
                        self.box_dict[q]["hit"] = True
                    elif q in self.item_dict:  # 아이템이 맞았는지
                        del self.item_dict[q]
                        self.set_info(q, 1)
                    else:
                        self.set_info(q, 1)
                    # 적이 맞았는지
                    for b in self.mob_dict["boss"]:
                        if q == b["pos"]:
                            b["hit"] = True

                    for m in self.mob_dict["minion"]:
                        if q == m["pos"]:
                            m["hit"] = True
                            print("미니언 맞음")
                    # 플레이어가 맞았는지
                    if q == Pos(self.char_stat["x"], self.char_stat["y"]):
                        self.char_dict["bomb_hit"] = True

            # 캐릭터 실제 이동
            ch = Pos(self.char_stat["x"], self.char_stat["y"])
            # if self.is_water(ch):
            #     self.char_dict["bomb_hit"] = True
            # 캐릭터랑 물줄기랑 맞았는지
            # 적이랑 맞았느지 체크

            # last tick 체크
            # last_tick = self.game_state() != 1
            self.char_dict["clear"] = False

            # character tick
            self.char_stat = Character.tick(self.char_dict)
            print(self.char_stat)

            # box tick
            box_a = Box.box_tick(damage_flags=[value["hit"] for _, value in self.box_dict.items()])
            for i, p in enumerate(self.box_dict):
                self.box_dict[p]["hp"] = box_a[i]["remaining_hp"]
                if self.box_dict[p]["hp"] <= 0:
                    if box_a[i]["item"] is not None:
                        self.set_item(p, self.get_item_id(box_a[i]["item"]))
                        self.item_dict[p] = box_a[i]["item"]
                    else:
                        self.set_info(p, 0)

            # mob tick
            # mob_a = Mob.tick(**{"boss_list": [True], "minion_list": [True, False, False]})
            # mob_a = Mob.monster_tick(**{"boss": [True], "minion": [True, False, False]})
            # tick: str
            mob_a, mob_b = Mob.monster_tick(tick=self.current_tick,
                                            damage_info={"boss": [{"pos": i["pos"].to_list(), "hit": i["hit"]} for i in
                                                                  self.mob_dict["boss"]],
                                                         "minion": [{"pos": i["pos"].to_list(), "hit": i["hit"]} for i
                                                                    in self.mob_dict["minion"]]})
            # print([{"pos": i["pos"].to_list(), "hit": i["hit"]} for i in self.mob_dict["minion"]])
            print("vv", mob_b)
            # 체력 설정
            for i in range(len(mob_a)):
                self.mob_dict["boss"][i]["hp"] = mob_a[i]["hp"]
            for i in range(len(mob_b)):
                self.mob_dict["minion"][i]["hp"] = mob_b[i]["hp"]

            # 몹 이동

            # 보스 패턴 설치

            self.display()

        pass

    def display(self):
        ch_box = {1: "▦", 2: "▥", 3: "▤", 7: "▣"}
        ch_item = {1: "＠", 2: "△", 3: "▶", 4: "♤", 5: "☞", }
        tmp = [["" for _ in range(self.map_size[0])] for _ in range(self.map_size[1])]

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                p = Pos(j, i)
                if self.is_empty(p):
                    tmp[i][j] = "　"
                elif self.is_box(p) and self.box_dict[p]["hp"] > 0:
                    tmp[i][j] = ch_box[self.box_id(p)]
                elif self.is_bomb(p):
                    tmp[i][j] = "B"
                elif self.is_item(p):
                    tmp[i][j] = ch_item[self.item_id(p)]
                else:
                    tmp[i][j] = self.get_info(p)
        tmp[self.char_stat["y"]][self.char_stat["x"]] = "☆"
        for b in self.mob_dict["boss"]:
            p = Pos(b["pos"].x, b["pos"].y)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    q = p + Pos(i, j)
                    tmp[q.y][q.x] = "●"

        for m in self.mob_dict["minion"]:
            print(m["pos"])
            if m["hp"] > 0:
                tmp[m["pos"].y][m["pos"].x] = "○"

        for i in range(self.map_size[1]):
            for j in range(self.map_size[0]):
                print(tmp[i][j], end="\t")
            print()

        print("──────────")
        # for X in range(self.map_size[0]):
        #     show = ""
        #     for Y in range(self.map_size[1]):
        #         if [Y, X] == [self.char_stat["y"], self.char_stat["x"]]:  # 플레이어 좌표 받아오기
        #             show += "\t\033[38;2;190;0;0mP\033[0m"  # 빨간색 "P"
        #         elif [Y, X] ==:  # 플레이어랑 물줄기 겹쳤을경우
        #             show += "\t\033[38;2;178;255;0mP\033[0m"  # 하늘색"P"
        #         elif [X, Y] ==:  # 플레이어랑 쫄이랑 겹쳤을경우
        #             show += "\t\033[38;2;230;50;50mP\033[0m"  # 연한 빨간색"P"
        #
        #
        #         # elif [Y, X] == [, ]:
        #         #     show += "\033[95m\t쫄\033[0m"  # 쫄 보라색
        #         # elif [X, Y] ==:  # 쫄몹이랑 아이템이랑 겹쳤을때
        #         #     show += "\t\033[38;2;102;0;88m쫄\033[0m"  # 연보라색 쫄
        #         # elif [X, Y] ==:  # 쫄몹이랑 물줄기랑 겹쳤을때
        #         #     show += "\t\033[38;2;178;255;0m쫄\033[0m"  # 하늘색 쫄
        #         #
        #         #
        #         # elif [Y, X] == [, ]:
        #         #     show += "\t\033[95mB\033[0m"  # 보스 보라색
        #         elif self.is_bomb(Pos(Y, X)) == 0:
        #             show += "\t\033[96m○\033[0m"  # 물풍선 하늘색
        #         elif self.is_water(Pos(Y, X)) == 1:
        #             show += "\t\033[96m●\033[0m"  # 물줄기 하늘색
        #
        #
        #         elif self.box_id(Pos(Y, X)) == 0:
        #             show += "\t\033[38;2;93;93;93m\033[0m"
        #         elif self.box_id(Pos(Y, X)) == 1:
        #             show += "\t\033[38;2;255;180;180m■\033[0m"
        #         elif self.box_id(Pos(Y, X)) == 2:
        #             show += "\t\033[38;2;175;72;72m■\033[0m"
        #         elif self.box_id(Pos(Y, X)) == 3:
        #             show += "\t\033[38;2;49;0;0m■\033[0m"  #
        #         elif self.item_id(Pos(Y, X)) == 0:
        #             show += "\t\033[33mI\033[0m"  # 아이템 노란색
        #         else:
        #             show += "\t■"
        #
        #     if X == 0:
        #         show += f"\t\t현재맵정보 몇틱?: {0} / 남은틱:{10}"  # 현재 진행틱 상황
        #
        #
        #     elif X == 2:
        #         show += f"\t\tPlayer Health: {1}"  # 플레이어 체력
        #
        #
        #     elif X == 3:
        #         show += f"\t\tBoss Health: {2}"  # 보스체력
        #
        #
        #     elif X == 6:
        #         show += f"\t\tItme List : [{"1"}],[{"2"}],[{"3"}],[{"4"}]"  # 아이템 리스트
        #
        #     print(show)  # 화면 출력

    def game_state(self):
        if False:  # 보스가 죽었으면
            return 0  # 클리어
        elif self.char_stat["hp"] <= 0 or self.current_tick > self.max_tick:
            return 1  # 게임오버
        return 2

    def bomb(self, p: Pos, power, s=None, pl=None):
        if s is None:
            s = set()
        if pl is None:
            pl = []
        ls = [i for i in range(1, power + 1)]
        dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.bomb_dict.pop(p, None)
        s.add(p)
        for d in dr:
            for l in ls:
                q = Pos(p.x + d[0] * l, p.y + d[1] * l)
                if not self.is_inside(q):
                    break
                s.add(q)
                if self.is_box(q):
                    break
                if self.is_bomb(q) and q not in pl:
                    pl.append(q)
                    if q in self.bomb_dict:
                        s |= self.bomb(q, self.bomb_dict[q]["power"], s, pl)
                    break
        return s

    ###########################################################################
    # 유저 행동 선택 입력받기
    def inp_user_act(self):
        tmp_tick = 0
        bomb_count = 0
        directions = []
        install_bomb = False

        while (tmp_tick != 1):
            _inp = input("입력>>")
            # 이동 # 시작이 wasd 중 하나 여야하고, 총 입력 길이가 0보다 크고 케릭터의 이동 가능한 크기보다 같거나 작아야함
            if _inp:
                if _inp[0] in "wasd" and 0 < len(_inp) <= self.char_stat["speed"]:
                    # 입력 값의 모든 요소 확인
                    for ele in _inp:
                        if ele == "w":
                            directions.append(ele)
                        elif ele == "a":
                            directions.append(ele)
                        elif ele == "s":
                            directions.append(ele)
                        elif ele == "d":
                            directions.append(ele)
                        else:
                            # print("오류메시지~~~")
                            directions.clear()  # 초기화
                            break  # 다시 입력받으러 감


                # 물풍선 설치
                elif _inp[0] == "q":
                    if bomb_count <= self.char_stat["b_count"] and install_bomb != True:
                        install_bomb = True

                        tmp_tick = 0
                        bomb_count += 1
                        continue


                    else:
                        continue


                # 이동 안함
                elif _inp[0] == "e":
                    tmp_tick = 1


                else:
                    # print("오류메시지~~~")
                    tmp_tick = 0
                    directions.clear()
                    install_bomb = False
                    continue

                tmp_tick = 1


            else:
                continue

        self.char_dict['bomb'] = install_bomb
        self.char_dict['movement'] = directions
        return directions

        # 이동가능여부

    def is_movable(self, direction):  # is_moveable(inp_user_act()[0])
        # 반환 값 저장 리스트
        result = []

        # 케릭터 정보 불러오기
        x = self.char_stat["x"]
        y = self.char_stat["y"]

        # 이동가능 칸 데이터
        # items = [32, 64, 96, 128, 160, 192, 224] 아이템 이동 가능
        # bombs = [1, 2] 1 물줄기 2 물풍선
        movable_list = [0, 32, 64, 96, 128, 160, 192, 224, 1]

        # 악마상태일 경우
        if self.char_stat["reverse"]:
            for act in direction:
                # 방향 값 일 경우 해당 방향 진행가능 여부 체크 후 T/F 값 반환
                if act == "w" and self.map_info[y + 1][x] in movable_list:
                    result.append(True)


                # 왼쪽으로 이동
                elif act == "a" and self.map_info[y][x + 1] in movable_list:
                    result.append(True)


                # 아래로 이동
                elif act == "s" and self.map_info[y - 1][x] in movable_list:
                    result.append(True)


                # 오른쪽로 이동
                elif act == "d" and self.map_info[y][x - 1] in movable_list:
                    result.append(True)


                # 이동 불가
                else:
                    result.append(False)


        # 악마상태가 아닐경우
        else:
            for act in direction:
                # 방향 값 일 경우 해당 방향 진행가능 여부 체크 후 T/F 값 반환
                # 위로 이동
                if act == "w" and self.map_info[y - 1][x] in movable_list:
                    result.append(True)


                # 왼쪽으로 이동
                elif act == "a" and self.map_info[y][x - 1] in movable_list:
                    result.append(True)


                # 아래로 이동
                elif act == "s" and self.map_info[y + 1][x] in movable_list:
                    result.append(True)


                # 오른쪽로 이동
                elif act == "d" and self.map_info[y][x + 1] in movable_list:
                    result.append(True)


                # 이동 불가
                else:
                    result.append(False)

        self.char_dict["movecheck"] = result

        # 아이템과 충돌

    def crushed_items(self):
        p = Pos(self.char_stat["x"], self.char_stat["y"])
        if self.is_item(p):
            self.char_dict["dropped_item"] = self.get_item_name(p)
            return True
        return False

    # 물줄기와 충돌
    def crushed_bombs(self):
        return self.is_water(Pos(self.char_stat["x"], self.char_stat["y"]))

    # 몬스터와 충돌
    def crushed_monster(self):
        char_pos = Pos(self.char_stat["x"], self.char_stat["y"])

        for b in self.mob_dict["boss"]:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if char_pos == b["pos"] + Pos(x, y):
                        self.char_dict["hit_count"] += 1
                        return True
        for b in self.mob_dict["minion"]:
            if char_pos == b["pos"]:
                self.char_dict["hit_count"] += 1
                return True


if __name__ == "__main__":
    map_ = Map()
    map_.play()