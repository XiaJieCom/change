import random
import core.handle as handle
class Role(object):
    def __init__(self,name,armor,weapon,life_value=100,money=0):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
    def power(self):
        p_armor = handle.select_equipment_power('armor',self.armor)
        p_weapon = handle.select_equipment_power('weapon',self.weapon)
        power = p_armor[0] + p_weapon[0] + self.life_value
        return power
    def damage(self):
        value_data = handle.select_equipment_power('weapon',self.weapon)[0] + handle.select_equipment_power('armor',self.armor)[0]
        return value_data
    def win(self,role1,role2,power1,power2):
        if power1 > power2:
            role1.money = role1.money + role2.money

        pass


class Monster(Role):
    def __int__(self,name,armor,weapon,life_value):
        super(Role,self).__init__(name,armor,weapon,life_value,money=0)
class Human(Role):
    def __int__(self,name,armor,weapon,life_value,):
        super(Role,self).__init__(name,armor,weapon,life_value,money=0)

    def update_armor(self):
        '''买装备'''
    def update_weapon(self):
        '''换武器'''



def name():
    f_name = {
        1:'优雅的',
        2:'蠢蠢的',
        3:'大耳朵',
        4:'小鼻子',
        5:'一只眼睛的',
        6:'凶恶的',
        7:'善良的',
        8:'可爱的',
        9:'萌萌的',
        10:'肥肥的',
    }
    l_name = {
        1:'兔子',
        2:'狐狸',
        3:'鼻涕虫',
        4:'骷髅战士',
        5:'亡灵骑士',
        6:'亡灵法师',
        7:'亡灵猎人',
        8:'亡灵召唤师',
        9:'强盗',
        10:'恶人',
    }

    f = random.randint(1,10)
    l = random.randint(1,10)
    name = f_name[f]+l_name[l]
    return name
def random_value():
    func = random.randint(1,100)
    return func
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    print('这是一片平静的小山村...\n走出来的是一位少年正要去冒险.\n只见他来到铁匠铺门前和铁匠打着招呼.\n这是所有的铠甲,你想要什么呢?大胡子矮人问他.    ')
    handle.select_all('armor')
    raw = input('少年一眼就看上了这个:    ').strip()
    armor = handle.select_equipment('armor',raw)
    print('这是你的%s,少年!\n这是所有的武器,你想要什么呢?大胡子矮人问他:   '% armor)
    handle.select_all('weapon')
    raw = input('这就是传说中的:    ').strip()
    weapon = handle.select_equipment('weapon',raw)
    h1 = Human('哈哈',armor,weapon,life_value=100,money=100)
    print('这是你的%s,少年!\n'% weapon)
    print('少年赶紧换上了新买的%s,拿着心爱的%s走向地狱边缘...'%(armor[0],weapon[0]))
    print(h1.power())

    #初始化一个怪兽
    armor = handle.select_equipment('armor',random.randint(1,7))
    weapon = handle.select_equipment('weapon',random.randint(1,6))

    m1 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m2 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m3 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m4 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m5 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m6 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m8 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m9 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())
    m10 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())

    print('%s武力值挺高的,都到了%s!'%(h1.name,h1.damage()))
    print(m1.power())

    while True:
        a = h1.damage()
        b = m1.damage()
        ap = h1.power()
        bp = m1.power()
        if h1.power() > m1.power():
            h1.money = h1.money + m1.money
            print('只见%s一招下去,%s倒下了...\n哇哦!还有%s个金币!!!现在我有%s个金币,可以买个大包子啦!!!'%(h1.name,m1.name,m1.money,h1.money))
            if h1.weapon < m1.weapon:
                h1.weapon = m1.weapon
                print('%s,你的%s不错,我就拿走了...'%(m1.name,m1.weapon[0]))
            else:
                print('%s,你的%s不好,我不要了...'%(m1.name,m1.weapon[0]))
            exit()
        elif h1.power() == m1.power():
            print('只见%s一招下去,和%s都倒退了两步...'%(h1.name,m1.name))
            exit()
        else:
            print('只见%s一招下去,%s倒下了...'%(m1.name,h1.name))
            exit()




