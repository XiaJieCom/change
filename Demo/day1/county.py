
#__author__ = 'jack'

message_dict = {

    'SD':{
        'JN':[

            'lixia','huaiyin'
        ],
        'HZ':[
            'juancheng','yuncheng'
        ]

    },
    'BJ':{
        "HD":[
            'huangzhuang','zhonguancun'
        ],
        'CY':[
            'dayuecheng','xidan'
        ]

    },
    'HB':{
        'SJZ':[
            'zheli','nali'
        ],
        'CD':[
            'bishu','guodong'
        ]
    }

}
'''
p_list = []
print("这里显示的是省：")
print("*******************************")
for p in message_dict.keys():
    p_list.append(p)
for p in p_list:
    print(p_list.index(p),p)
p_choice = input("输入你要查询的省：")
print(p_list.index(p_choice))

#for c in message_dict:
#    print(p_list.index(c)[p_choice])
'''
for p in message_dict:
    print(p)
p_choice = input("输入你要查询的省：")
print("*******************************")
for c in message_dict[p_choice]:
    print(c)
c_choice = input("输入你要查询的市：")
print("*******************************")
for v in message_dict[p_choice][c_choice]:
    print(v)










'''
message_list = [
    ('SD',('JN',('lixia','huaiyin'),('HZ',('juancheng','yuncheng')))),
    ('BJ',('HD',('huangzhuang','zhongguancun'),('CY',('dayuecheng','xidan')))),
    ('HB',('CD',('c1',('v1','v2'),'c2',('v10','v20'))))
]
p_list = []
#print(message_list[0][0])
for i in message_list:
    p_list.append(message_list[message_list.index(i)][0])
for i in p_list:
    print(i)
choice = input("Input p: ")

'''










"""
print("这里显示的是省：")
print("*******************************")

for p in message_dict:
    print(p)
    city_list.append(message_dict[p])
choice = input("输入你要查询的省：")
print("*******************************")
for c in message_dict[choice]:
    print(c)
choice = input("输入你要查询的市：")
print("*******************************")

"""
   # print("这里显示的是 : %s 的组成。"% p)
#print(city_list[0])
#
#for v in v_list:
 #   print(v_list[v][0])


#   province_list.append(province)
#    city_list = message_dict[province]
#print(province_list)
'''
print("这里显示的是市: ")
city_list1 = message_dict['SD']
for i in city_list1:
    print(i)
print("这里显示的是县区： ")
city_list2 = city_list1['JN']
for i in city_list2:
    print(i)

'''

#for c in city_list1:
#city_list2 = city_list1[c]

'''
while True:
    choice = input("Input your choice: ")
    if choice not in city_list:
        print("Input error !")
    else:
        city_list1 = city_list[choice]
        print(city_list1)
        for c in city_list1:
            city_list2 = city_list1[c]
            print(city_list2)
            for v in city_list2:
                city_list3 = city_list2.index(v)
                print(city_list3)
                #for h in range(city_list3):
                 #   print(h)

'''
#choice = input("Welcome to City inquiry system !\n1 registry \n2 login \n3 quit").strip()
'''
for i in province_list:
    print(province_list.index(i),i)
    choice = input("Your choice: ").strip()
    if
for i in city_list:
    print(city_list.index(i),i)
for i in villages_list:
    print(villages_list.index(i),i)

'''




'''
if 选择等于 注册：
    注册
elif 选择等于 登录：
    登录
    打印全国的省
    选择一个省，打印所有的市
else:
    quit

'''