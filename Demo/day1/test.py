
message_dict =[
    ('SD',('JN',('lixia','huaiyin')),('HZ',('juancheng','yuncheng'))),
    ('BJ',('HD',('zhongguancun','huangzhuang')),('CY',('xidan','dongdan'))),
    ('SH',('PD',('jichang','chezhan')),('PX',('zheli','nali')))
]

#for i in message_dict:
    #print(message_dict.index(i),i)

#    print(message_dict[][0])
p_list = []
c_list = []
v_list = []
i = 0
print("这里输出的是省")
'''
while i < len(message_dict):
    print(i,message_dict[i][0])
    p_list.append(message_dict[i][0])
    i += 1
'''
#print(p_list)
#choice = input("请输入你要查询的省: ")
#for c in message_dict[0][0]:
#    print(c)
for i in range(len(message_dict)):
    print(i,message_dict[i])
#    p_list.append(message_dict[i][0])
#for i in p_list:
#    print(i)