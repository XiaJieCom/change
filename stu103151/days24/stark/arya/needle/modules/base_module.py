#!/usr/bin/env python3

from core.utils import MsgPrint

class BaseSaltModule(object):

    def __init__(self,task_obj):
        self.task_obj = task_obj


    def process(self,module_data,*args,**kwargs):
        section_name = module_data['raw_cmds']['section']
        section_data = module_data['raw_cmds']['mod_data']
        sub_action = module_data['raw_cmds'].get('sub_action')

        for mod_item in section_data:
            for k,v in mod_item.items():
                state_func = getattr(self,'func__%s'%k)
                state_func(v)

        if sub_action:                  
            # 如果没有,就执行,基本只针对文件和模块
            sub_action_func = getattr(self,'func__%s' % sub_action)
            sub_action_func(module_data=module_data['raw_cmds'])


    def func__require(self,*args,**kwargs):
        print('require:',*args,**kwargs)



    def type_validate(self,item_name,data,data_type):
        if type(data) is not data_type:
            MsgPrint.error("[%s] requires %s, not a %s" %(item_name,data_type,type(data)))




