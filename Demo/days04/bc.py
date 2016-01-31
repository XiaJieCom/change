import re
#格式化函数
def format_func(raw):
     #替换所有的空格
    raw = re.sub('\s','',raw)
    #print(raw)
    #替换,正负为负
    raw = raw.replace('+-','-')
    #print(raw)
     #替换,负正为负
    raw = raw.replace('-+','-')
    #print(raw)
     #替换,正正为正
    raw = raw.replace('++','+')
    #print(raw)
     #替换,负负为正
    raw = raw.replace('--','+')
    #print(raw)
     #最后返回格式化后的字符串
    return raw
#计算函数
def compute(raw):
    #加减函数
    raw = multiply_divide_func(raw)
    #乘除函数
    raw = add_subtract_func(raw)
    #返回结果
    return raw
#计算乘除的函数
def multiply_divide_func(raw):
    #首先格式化字符串
    raw = format_func(raw)
    #判断是否包含乘除,没有的话就返回
    if not re.search('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*',raw):
        return raw
    s = re.search('\d+\.*\d*[\*,\/]+[\+\-]?\d+\.*\d*',raw).group()
    #如果有*,以'*'进行列表分割;替换
    if re.search('\*',s):
        res = float(s.split('*')[0]) * float(s.split('*')[1])
        raw = raw.replace(s,str(res),1)
    else:
    #如果有'/',以'/'进行列表分割;替换
        res = float(s.split('/')[0]) / float(s.split('/')[1])
        raw = raw.replace(s,str(res),1)
    #返回执行结果
    return multiply_divide_func(raw)
#计算加减
def add_subtract_func(raw):
    #格式化字符串
    raw = format_func(raw)
    #是否存在'+','-',不存在就返回值
    if not re.search('\d+\.?\d*[\+\-]\d+\.?\d*',raw):
        return raw
    s = re.search('\d+\.*\d*[\+,\-]\d+\.*\d*',raw).group()
    #是否包含加号,包含则以'+'列表分割;替换
    if re.search('\+',s):
        res = float(s.split('+')[0]) + float(s.split('+')[1])
        raw = raw.replace(s,str(res),1)
    else:
    #否则则以'-'列表分割;替换
        res = float(s.split('-')[0]) - float(s.split('-')[1])
        raw = raw.replace(s,str(res),1)
    #返回计算结果
    return add_subtract_func(raw)
#该函数功能是移除空格
def remove_func(raw):
    #执行format_func函数,进行格式化
    raw = format_func(raw)
    #如果前面格式化后的字符串没有包含括号,就返回执行compute()计算函数
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',raw):
        return compute(raw)
    #否则就查找里面的括号
    s = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',raw).group()
    res = s.strip('\(\)')#去除括号
    #然后再次计算去除括号后的字符串
    compute_res = compute(res)
    #将计算后的结果替换为之前括号里的内容
    raw = raw.replace(s,compute_res,1)
    #输出结果
    return remove_func(raw)

if __name__ == '__main__':
    #用户输入
    raw = input('Please input: ').strip()
    #raw = '1 - 2 * ((-40.0/5) * (9-2*5/3 )) - (-4*3)/ (16-3*2) ) '
    #(2 *(1+(2-3)*5/5) +2)-3*6/6+1 raw = '(2 *(1+(2-3)*5/5) +2)-3*6/6+1 '
    #raw = '1 - 2 * ( (60-30 +(-40.0/5) - (9-2*5/3)) - (-4*3)/ (16-3*2) ) '
    #执行remove_func,移除空格
    print(remove_func(raw))







