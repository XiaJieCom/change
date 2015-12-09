#!/usr/bin/env python
# -*- coding: utf-8 -*-

shopping_list = [
('Iphone',5800),
('Bike',800),
('Book',45),
('Coffee',35),
('Solo 2 Beats',1590),
('MX4',1999),
]
#定义一个商品列表

budget = int(raw_input("please input your budget:").strip())
#输入预算

buy_list = []
#定义购物车列表

while True:
	for i in shopping_list:
		print shopping_list.index(i),i
#循环打印出商品的index和商品名称
	choice = int(raw_input("please input your choice:").strip())
#输入选择的商品，strip()表示忽略空格
	item_price = shopping_list[choice][1]
#输出选择商品的价格，这里把（‘xxx’,xxxx）当成两个元素，单独取第二个输出为价格

	print item_price
	#判断预算是否大于商品价格，如果大于就减去当前商品，打印输出已经购买的商品，和剩余的预算；否则提示重新输入
	if budget >= item_price:
		budget -= item_price
		buy_list.append(shopping_list[choice])
		print "Added \033[1;33m %s \033[0m into shopping list." % shopping_list[choice][0]
		print "You just  only have \033[1;32m %s \033[0m. \n" % budget
	else:
		print "Sorry, you can not afford to buy %s,try another!" %shopping_list[choice][0]


