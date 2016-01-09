message = {

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

p_list = []
c_list = []
h_list = []
print("*********************************\n欢迎进入城市查询系统，请按提示操作")
    #打印省份信息，以及下标，生成省份列表，循环打印
for p in message.keys():
    p_list.append(p)
#print(p_list)
for i in p_list:
    print(p_list.index(i),i)
while True:
    p_choice = input("\033[1;33m 请输入要查询的省编号: \033[0m").strip()
#print("显示的为：%s" % p_list[p_choice])
    if p_choice == 'q':
        print("您选择了退出！")
        exit()
    elif int(p_choice) >= len(message.keys()):
        print("请重新输入正确的编号")
    else:
        break
#打印城市信息，以及下标；生成城市列表，循环打印
for c in message[p_list[int(p_choice)]]:
    c_list.append(c)
print("*********************************")
for i in c_list:
    print(c_list.index(i),i)
while True:
    c_choice = input("\033[1;33m 请输入要查询的城市编号: \033[0m").strip()
#print("显示的为：%s" % c_list[c_choice])
    if c_choice == 'q':
        print("您选择了退出！")
        exit()
    elif int(c_choice) >= len(c_list):
        print("请重新输入正确的编号")
    else:
        break
#打印乡镇信息，生成一张表格，然后for循环打印
for i in message[p_list[int(p_choice)]][c_list[int(c_choice)]]:
    h_list.append(i)
#print(h_list)
print("*********************************\n显示的为城市\033[1;32m %s \033[0m的组成\n" % c_list[int(c_choice)])
for i in h_list:
    print(i)
print("\n*********************************")




