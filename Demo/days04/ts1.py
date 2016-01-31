#! /usr/bin/env python
# -*- coding:utf-8 -*-
import re

#格式化函数，去除空格
def format_add_sub(string):
    string = re.sub('\s*','',string)
    #负负为正
    string = string.replace('--','+')
    #正负为负
    string = string.replace('+-','-')
    #负正为负
    string = string.replace('-+','-')
    #正正为正
    string = string.replace('++','+')
#    string = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', string).group()
    return string
# 计算乘除
def mul_div(string):
    #格式化
    string = format_add_sub(string)
    #如果没有乘除，直接返回值。
    if not re.search('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*',string):
        return string
    #搜索第一个乘除
    s = re.search('\d+\.*\d*[\*,\/]+[\+\-]?\d+\.*\d*',string).group()
    #如果是乘
    if re.search('\*',s):
        #以乘号进行列表分隔
        resuit = float(s.split('*')[0]) * float(s.split('*')[1])
        string = string.replace(s,str(resuit),1)
    #如果是除
    else:
        #以除号进行列表分隔
        resuit = float(s.split('/')[0]) / float(s.split('/')[1])
        string = string.replace(s,str(resuit),1)
    #循环此函数
    return mul_div(string)
#计算加减函数
def add_sub(string):
    string = format_add_sub(string)
    #如果没有检测到加、减，直接返回值。
    if not re.search('\d+\.?\d*[\+\-]\d+\.?\d*',string):
        return string
    #检索第一个加、减
    s = re.search('\d+\.*\d*[\+,\-]\d+\.*\d*',string).group()
    #如果是加
    if re.search('\+',s):
        resuit = float(s.split('+')[0]) + float(s.split('+')[1])
        string = string.replace(s,str(resuit),1)
    #如果是减
    else:
        resuit = float(s.split('-')[0]) + float(s.split('-')[1])
        string = string.replace(s,str(resuit),1)
    #循环此函数
    return add_sub(string)

#计算函数
def compute(string):
    #计算乘除
    string = mul_div(string)
    #计算加减
    string = add_sub(string)

    return string
#检测括号函数
def remove_bracket(string):
    #格式化函数。
    string = format_add_sub(string)
    #如果没有括号，返回计算函数。
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',string):
        return compute(string)
    #检索最内层括号
    s = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',string).group()
    #去掉括号后的内容
    ds = s.strip('\(\)')
    #计算括号中的内容
    resut = compute(ds)
    #用计算结果，替换原括号中的内容。
    string = string.replace(s,resut,1)
    #循环此函数，知道没有括号出现。
    return remove_bracket(string)

if __name__ == '__main__':
    #string = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) '
    string = '(2 *(1+(2-3)*5/5) +2)-3*6/6+1 '
    print(remove_bracket(string))