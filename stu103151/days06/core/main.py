import random
import core.handle as handle
class Role(object):
    '''
    定义一个通用的Role类
    '''
    def __init__(self,name,armor,weapon,life_value=100,money=0):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
    def power(self):
        '''
        根据weapon和armor/life_value的值求出power
        :return:
        '''
        p_armor = handle.select_equipment_power('armor',self.armor)
        p_weapon = handle.select_equipment_power('weapon',self.weapon)
        power = p_armor[0] + p_weapon[0] + self.life_value
        return power
    def damage(self):
        '''
        根据weapon和armor计算出来伤害值
        :return:
        '''
        value_data = handle.select_equipment_power('weapon',self.weapon)[0] + handle.select_equipment_power('armor',self.armor)[0]
        return value_data

class Monster(Role):
    '''
    定义怪兽的类
    '''
    def __int__(self,name,armor,weapon,life_value):
        super(Role,self).__init__(name,armor,weapon,life_value,money=0)
class Human(Role):
    '''
    定义人类的类
    '''
    def __int__(self,name,armor,weapon,life_value,):
        super(Role,self).__init__(name,armor,weapon,life_value,money=0)
    def buy(self):
        '''买装备'''
    def pick(self):
        '''捡钱'''



def name():
    '''
    随机生成怪物的名字
    :return:
    '''
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
    '''
    随机产生数字,便于随机分配给怪兽属性
    :return:
    '''
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
    weapon = handle.select_equipment('weapon',random.randint(1,8))

    m1 = Monster(name(),armor,weapon,life_value=random_value(),money=random_value())


    print('%s武力值挺高的,都到了%s!'%(h1.name,h1.damage()))
    print('\n前面出现了一个%s,它的力量很强大,到了%s!\n' %(m1.name,m1.power()))
    if h1.power() >= m1.power():
        tmp1 = h1.power()
        tmp2 = m1.power()
        i = 1
        while tmp1 > 0:

            print('第%s回合!'%i)
            if tmp2 - h1.damage() <= 0:
                print('%s减去了%s的血!他倒下啦!!!\n还有%s个金币!!!!'%(m1.name,h1.damage(),m1.money))

                if handle.select_equipment_power('weapon',m1.weapon) > handle.select_equipment_power('weapon',h1.weapon):
                    h1.weapon = m1.weapon
                    print('\n%s的武器爆出来啦!\n%s捡起来看了看,感觉还不错,把武器换成了这%s!'% (m1.name,h1.name,h1.weapon[0]))

                break
            else:
                tmp2 = tmp2 - h1.damage()
                print('%s减去了%s的血!剩余%s!!!'%(m1.name,h1.damage(),(tmp2)))
                tmp1 = tmp1 - m1.damage()
                print('%s减去了%s的血!剩余%s!!!'%(h1.name,m1.damage(),tmp1))

            i += 1
        else:
            print('%s倒下啦!!!'%h1.name)
    else:
        tmp1 = h1.power()
        tmp2 = m1.power()
        i = 1
        while tmp2 > 0:

            print('第%s回合!'%i)
            if tmp1 - m1.damage() <= 0:
                print('%s减去了%s的血!他倒下啦!!!'%(h1.name,m1.damage()))
                exit()
            else:
                tmp1 = tmp1 - m1.damage()
                tmp2 = tmp2 - h1.damage()
                print('%s减去了%s的血!剩余%s!!!'%(h1.name,m1.damage(),tmp1))
                print('%s减去了%s的血!剩余%s!!!'%(m1.name,h1.damage(),(tmp2)))
            i += 1
        else:
            print('%s减去了%s的血!他倒下啦!!!\n还有%s个金币!!!!'%(m1.name,h1.damage(),m1.money))














