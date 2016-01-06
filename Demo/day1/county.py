
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