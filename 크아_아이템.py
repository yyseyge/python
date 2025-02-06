import random as rm




class Item:
   # 아이템 종류와 효과를 정의
   ITEM_TYPES = {
       "plus_bomb": {"name": "폭탄 소지+", "effects": {"b_count": 1}},
       "plus_scope": {"name": "폭발 범위+", "effects": {"b_range": 1}},
       "skate": {"name": "스케이트", "effects": {"speed": 1}},
       "reverse": {"name": "악마", "effects": {"reverse": True}},
       "kick": {"name": "킥", "effects": {"kick": True}},
   }


   def __init__(self, x=0, y=0, item_type="nothing"):
       # 아이템 초기화
       # x: 아이템의 X 좌표
       # y: 아이템의 Y 좌표
       # item_type: 아이템의 유형 (ITEM_TYPES에 정의된 키값)
       if item_type not in self.ITEM_TYPES:
           raise ValueError(f"Invalid item_type: {item_type}")


       self.x = x
       self.y = y
       self.item_type = item_type
       self.name = self.ITEM_TYPES[item_type]["name"]
       self.effects = self.ITEM_TYPES[item_type]["effects"]


   def get_position(self):
       # 아이템의 현재 좌표를 반환
       return self.x, self.y


   def __str__(self):
       return f"Item({self.name}, 위치=({self.x}, {self.y}))"


   def apply_effect(self, character):
       for stat, value in self.effects.items():
           if hasattr(character, stat):  # 캐릭터가 해당 속성을 가지고 있을 경우
               current_value = getattr(character, stat)
               max_stat = f"max_{stat}"  # 최대값 속성 이름 동적 생성


               if hasattr(character, max_stat):  # 최대값 속성이 존재하면
                   max_value = getattr(character, max_stat)
                   new_value = min(current_value + value, max_value)  # 최대값 제한
               else:
                   new_value = current_value + value  # 최대값 없으면 그냥 증가


               setattr(character, stat, new_value)  # 캐릭터 안에 stat을 new value로 설정


               print(f"{self.name} 효과 적용됨: {stat} +{value} (현재값: {new_value})")
           else:
               print(f"캐릭터에 {stat} 속성이 없어 효과를 적용할 수 없습니다.")




class Box:
   def __init__(self, b_x, b_y):
       self.hp = 1  # 박스의 체력
       self.x = b_x  # 박스의 X 좌표
       self.y = b_y  # 박스의 Y 좌표


   def damaged_box(self):
       self.hp -= 1
       if self.hp <= 0:
           return self.drop_item()
       return None


   def drop_item(self):
       drop_chance = rm.random()  # 0.0 ~ 1.0 사이의 랜덤 값
       if drop_chance < 0.7:  # 70% 확률로 아이템 생성
           item_type = rm.choice(list(Item.ITEM_TYPES.keys()))  # ITEM_TYPES의 키에서 랜덤 선택
           return Item(self.x, self.y, item_type)  # 선택된 타입으로 아이템 객체 생성
       else:
           print("아이템이 나오지 않았습니다.")







class Character:

    def __init__(self,x,y):
        self.hp = 3
        self.speed = 1
        self.max_speed = 3
        self.b_count = 1
        self.max_b_count = 3
        self.b_range = 1
        self.max_b_range = 5
        self.damage = 1
        self.x = x
        self.y = y
        self.kick = False
        self.state = None

    def move_up(self, x):
        self.x -= x
        return self.x
    def move_down(self,x):
        self.x += x
        return self.x
    def move_left(self,y):
        self.y -= y
        return self.y
    def move_right(self,y):
        self.y += y
        return self.y

    def input(self, input):
        if input[0] == "w":
            self.move_up(len(input))
            print(f"{len(input)}칸 ")
        elif input[0] == "a":
            self.move_left(len(input))
        elif input[0] == "s":
            self.move_down(len(input))
        elif input[0] == "d":
            self.move_right(len(input))
            print(f"{len(input)}칸 오른쪽으로 이동 ")
            print(self.x, self.y)

    # def 물풍선

    def get_damage(self,damage):
        self.hp -= damage
        if self.hp == 0:
            self.state="Die"
            return
        return self.hp


    def get_state(self):
        self.hp -= 1
        return {
            "hp": self.hp,
            "speed": self.speed,
            "b_count": self.b_count,
            "b_range": self.b_range,
            "damage": self.damage,
            "x": self.x,
            "y": self.y,
            "kick": self.kick,
            "state": self.state
        }

char = Character(1,1)

char.input(input())
print(char.get_state())

bi = Item(5,5,"plus_bomb")
print(bi.apply_effect(char))


ps = Item(8,6,"plus_scope")
print(ps.apply_effect(char))

# 박스 생성
for i in range(10):
   a = rm.randrange(1, 25)
   b = rm.randrange(1, 25)
   box = Box(a, b)


   dropped_item = box.drop_item()
   if dropped_item:
       print(dropped_item)


# input"이동할 방향 골"
# w 위로 이동 ww 위로 2칸
# 맵 소통함수
# 이동
# 생성(기본값) - 이동 - 결과값- 이동 - 결과값- 이동 - 결과값