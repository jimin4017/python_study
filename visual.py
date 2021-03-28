name ="마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
hp = 40
damage = 5
location = 1dddd

def attack (name,location,damage) :
    print("{0}:{1} 방향으로 적군을 공격 : damage = {2}".format(name,location,damage))



class unit :
    def __init__(self,name,hp,damage) :
        self.name =name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0} , 공격력 {1}".format(self.hp, self.damage))

marine1 = unit("마린",40,5)
marine2 = unit("마린",40,5)
tank = unit("탱크",150,35)

wraith1 = unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))


class AttackUnit :
    def __init__(self,name,hp,damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
    

    def attack(self,location) :
        print("{0} :{1} 현재 체력은 {2}입니다.".format(self.name,location,self.damage))


    def damaged(self,damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))



firebat1 = AttackUnit("파이어뱃",50,16)
firebat1
firebat1.attack("5시")
firebat1.damaged(25)

