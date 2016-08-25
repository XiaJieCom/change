#!/usr/bin/env python3

import sys

from arya import action_list
import django
django.setup()

from stark import settings
from arya import  models


class ArgvManagement(object):
    '''
    接收用户指令并分配到相应的模块
    '''

    def __init__(self,argvs):
        self.argvs = argvs
        self.argv_parse()

    def help_msg(self):
        '''
        帮助
        :return:
        '''
        for regisrered_module in action_list.actions:
            print(" %s" % regisrered_module)
        exit()

    def argv_parse(self):
        if len(self.argvs) < 2: # 如果参数个数小于2个,表示命令格式错误
            self.help_msg()
        module_name = self.argvs[1] # 获取到模块名和方法
        # cmd.cmd
        if '.' in module_name:
            mod_name,mod_method = module_name.split('.')
            module_instance = action_list.actions.get(mod_name) # 获取到模块名
            if module_instance: # 模块名存在
                module_obj = module_instance(self.argvs,models,settings)
                module_obj.process()# 获取主机
                if hasattr(module_obj,mod_method):
                    # 解析任务,发送到队列,获取任务结果
                    module_method_obj = getattr(module_obj,mod_method)
                    module_method_obj() # 调用指定得指令
                else:
                    exit("module [%s] doesn't hae [%s] method" %(mod_name,mod_method))
        else:
            exit("invalid module name argument")








