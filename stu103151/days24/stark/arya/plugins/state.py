#!/usr/bin/env python3

from arya.backends.base_module import BaseSaltModule
import os


class State(BaseSaltModule):

    def load_state_files(self,self_filename):
        '''
        解析yaml文件
        :param self_filename:  yaml 文件名
        :return:
        '''
        from yaml import load,dump
        try:
            from yaml import CLoader as Loader,CDumper as Dumper
        except ImportError:
            from yaml import Loader,Dumper
        state_file_path = "%s/%s" %(self.settings.SALT_CONFIG_FILES_DIR,state_filename) # yaml文件路径
        if os.path.isfile(state_file_path):
            with open(state_file_path) as f: # 读取yaml 文件
                data = load(f.read(),Loader=Loader)
                return data
        else:
            exit("%s is not a valid yaml config file " % state_filename)

    def apply(self):
        '''
        1,加载配置文件
        2,解析配置文件
        3,创建任务并将其发送到MQ
        4,收集任务返回结果
        :return:
        '''

        if '-f' in self.sys_argvs: # 如果 -f 存在命令参数中
            yaml_file_index = self.sys_argvs.index('-f') + 1 # 获取到yaml文件索引
            try:
                yaml_filename = self.sys_argvs[yaml_file_index] # 获取到yaml文件名
                state_data = self.load_state_files(yaml_filename) #解析yaml文件


                for os_type,os_type_data in self.config_data_dic.items(): # 按照不同的操作系统单独生成一份配置文件
                    for section_name,section_data in setate_data.items():
                        print('section',section_name)

                        for mod_name,mod_data in section_data.items():
                            base_mod_name = mod_name.split(".")[0]
                            module_obj = self.get_module_instance(base_mod_name=base_mod_name,os_type=os_type)
                            module_parse_result = module_obj.syntax_parser(section_name,mod_name,mod_data,os_type)
                            self.config_data_dic[os_type].append(module_parse_result)
                            # plugin_file_path = "%s/%s.py" %(self.settings.SALT_CONFIG_FILES_DIR,base_mod_name)
                            # if os.path.isfile(plugin_file_path):
                            #     # 导入 模块
                            #     module_plugin = __import__('plugins.%s' %base_mod_name)
                            #     special_os_module_name = "%s/%s" %(os_type.capitalize(),base_mod_name.capitalize())
                            #     module_file = getattr(module_plugin,base_mod_name) # 导入模块
                            #     if hasattr(module_file,special_os_module_name): #判断有没有根据操作系统的类型进行特殊解析的类
                            #         module_instance = getattr(module_file,special_os_module_name)
                            #     else:
                            #         module_instance = getattr(module_file,base_mod_name.capitalize())
                            #
                            #         # 开始调用 此 module 进行配置解析
                            #         module_obj = module_instance(self.sys_argvs,self.db_models,self.settings)
                            #         module_obj.syntax_parser(section_name,mod_name,mod_data)
                            # else:
                            #     exit("module [%s] is not exist" %base_mod_name)
                new_task_obj = tasks.TaskHandle(self.db_models,self.config_data_dic,self.settings,self)
                new_task_obj.dispathch_task()

            except ImportError as e:
                exit("state file must be provided after -f")
        else:
            exit("statefile must be specified.")


