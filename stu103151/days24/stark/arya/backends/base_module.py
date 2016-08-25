#!/usr/bin/env python3

class BaseSaltModule(object):
    def __init__(self,sys_argvs,db_models,settings):
        self.db_models = db_models
        self.settings = settings
        self.sys_argvs = sys_argvs


    def argv_validation(self,argv_name,val,data_type):
        if type(val) is not data_type:
            exit("Erro:[%s]'s data type is not valid" %argv_name)

    def get_selected_os_types(self):
        '''
        获取主机的系统类型
        :return:
        '''
        data = {}
        for host in self.host_list: #如果主机在主机列表中就判断它的系统类型
            data[host.os_type] = [] 
            return data



    def process(self):
        '''
        获取主机类型列表
        :return:
        '''
        self.fetch_hosts()
        self.config_data_dic = self.get_selected_os_types()


    def require(self,*args,**kwargs):
        os_type = kwargs.get('os_type')     #获取操作系统类型

        self.require_list = []

        for item in args[0]:
            for mod_name,mod_val in item.items():
                module_obj = self.get_module_instance(base_mod_name=mod_name,os_type=os_type)
                require_condition = module_obj.is_required(mod_name,mod_val)
                self.require_list.append(require_condition)


    def fetch_hosts(self):
        '''
        处理参数
        如果参数格式错误,返回错误信息 参数结果为True
        如果参数格式正确, 获取到一个主机列表
        :return:
        '''
        if '-h' in self.sys_argvs or '-g' in self.sys_argvs: # 如果 -h 或 -g 存在参数中
            host_list = []  #创建一个主机空列表
            if '-h' in self.sys_argvs: # 先处理 -h 参数
                host_str_index = self.sys_argvs.index('-h') +1 # -h 索引值+1 ,及 -h 后面的主机名
                if len(self.sys_argvs) <= host_str_index:   # 如果 -h 后面没有参数
                    exit('host argument must be provided after -h') # 命令格式错误
                else:
                    host_str = self.sys_argvs[host_str_index]   # 获取到-h 后面的参数
                    # web1,web2,web3
                    host_str_list = host_str.split(',') # 把参数以 ',' 分割
                    host_list += self.db_models.Host.objects.filter(hostname__in=host_str_list) # 添加入主机列表中
            if '-g' in self.sys_argvs: # 如果 存在 -g 参数
                group_str_index = self.sys_argvs.index('-g') +1 # 获取 -g 后的参数的索引值
                if len(self.sys_argvs) <= group_str_index:
                    exit("group argument must be provided after -g")
                else:
                    group_str = self.sys_argvs[group_str_index] # 获取 -g 后面的参数
                    # group1,group2
                    group_str_list = group_str.split(',')   # 把参数以 ',' 分割
                    group_list = self.db_models.HostGroup.objects.filter(name__in=group_str_list) # 获取到主机组列表
                    for group in group_list:    # 循环主机组列表
                        host_list += group.hosts.select_related() # 取出主机组内的主机,添加入主机列表
            self.host_list = set(host_list) # 主机列表去除重复
            return True
        else:
            exit("host [-h] or group [-g] argument must be provided")



    def is_required(self,*args,**kwargs):
        exit("Error: is_required() method must be implemented is module class [%s]" %args[0])

    def get_module_instance(self,*args,**kwargs):
        base_mod_name = kwargs.get('base_mod_name')
        os_type = kwargs.get('os_type')
        plugin_file_path = "%s/%s.py" %(self.settings.SALT_PLUGINS_DIR,base_mod_name)
        if os.path.isfile(plugin_file_path):
            module_plugin = __import__('plugins.%s' %base_mod_name)
            special_os_module_name = "%s%s" %(os_type.capitalize(),base_mod_name.capitalize())
            module_file = getattr(module_plugin,base_mod_name)
            if hasattr(module_file,special_os_module_name):
                module_instance = getattr(module_file,special_os_module_name)
            else:
                module_instance = getattr(module_file,base_mod_name.capitalize())
            module_obj = module_instance(self.sys_argvs,self.db_models,self.settings)
            return module_obj
        else:
            exit("module [%s] is not exist" % base_mod_name)





    def syntax_parser(self,section_name,mod_name,mod_data):
        '''
        处理模块名,获取到模块名,以及模块内的方法并执行
        :param section_name:
        :param mod_name:
        :param mod_data:
        :return:
        '''
        self.raw_cmds =[]
        self.single_line_cmds = []

        for state_item in mod_data:
            for key,val in state_item.items():
                if hasattr(self,key):
                    state_func = getattr(self,key)
                    state_func(val)
                else:
                    exit("Error:module [%s] has no argument [%s]" %(mod_name,key))
        else:
            if '.' in mod_name:     #如果模块名里包含'.'那么就分割为mod_name和mod_action
                base_mod_name,mod_action = mod_name.split('.')
                if hasattr(self,mod_action):    #判断这个mode_action 是否存在
                    mod_action_func = getattr(self,mod_action)
                    cmd_list = mod_action_func(section=section_name,mod_data=mod_data)
                    data = {
                        'cmd_list':cmd_list,
                        'required_list':self.require_list
                    }

                    if type(cmd_list) is dict:
                        data['file_module'] = True
                        data['sub_action'] = cmd_list.get('sub_action')
                        # 上面代表一个section里的具体得一个module 已经解析完毕了
                    return data
                else:
                    exit("Error:module [%s] has no method [%s]" %(mod_name,mod_action))
                    #如果不存在则输出改mod_name，没有对应的 mod_action
            else:
                exit("Error:module action of [%s] must be supplied" %(mod_name))





