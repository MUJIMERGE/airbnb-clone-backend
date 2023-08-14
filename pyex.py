from typing import Any


class Human:
    def __init__(self, name):
        # 생성자
        # self는 Java의 this 와 같음
        self.name = name
        
    def say_hello(self):
        print(f"hello my name is {self.name}")

# 상속
class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp
    
# 상속
class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team
        
muji_player = Player("MUJI", 1000)
muji_player.say_hello()
muji_fan = Fan("muji_fan", "dontknow")
muji_fan.say_hello()

# class Dog:
#     def woof(self):
#         print("woof woof")
        
# class Beagle(Dog):
#     def woof(self):
#         super().woof()
#         print("super woof")
        
# beagle = Beagle()
# beagle.woof()

class Dog:
    def __init__(self, name):
        self.name = name
        
    # 언더스코어 메소드
    def __str__(self):
        print(super().__str__())
        return f"Dog: {self.name}"
    
    # def __getattribute__(self, name):
    #     print(f"they want to get {name}")
    #     return "wwww"
        
jia = Dog("jia")
print(dir(jia)) # 클래스의 속성과 메소드 보여줌
# paul = Dog("paul")
# print(paul.name) # getattribute 호출 
