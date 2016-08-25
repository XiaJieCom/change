#!/usr/bin/env python3

from conf import configs,registered_modules
from modules import files

import pika
import platform
import subprocess
import json
import threading


class CommandManagement(object):
    def __init__(self,argvs):
        self.argvs = argvs[1:]
        self.argv_handler()


    def argv_handler(self):
        if len(self.argvs) == 0:
            exit("argument: start\stop")
        if hasattr(self,self.argvs[0]):
            func = getattr(self,self.argvs[0])
            func()
        else:
            exit("invalid argument.")


    def start(self):
        client_obj = Needle()
        client_obj.listen()

    def stop(self):
        pass


class TaskHandle(object):
    def __init__(self,main_obj,task_body):
        self.main_obj = main_obj
        self.task_body = json.loads(task_body.decode())


    def processing(self):
        '''
        process task
        :return:
        '''
        check_res = self.check_data_valiation()
        if check_res:
            self.current_os_type,data = check_res
            self.parse_task_data(self.current_os_type,data)



    def task_callback(self,callback_queue,callback_data):
        '''
        把任务执行结果返回给服务器
        :param callback_queue:
        :param callback_data:
        :return:
        '''
        data = {
            'client_id':self.main_obj.client_id,
            'data':callback_data
        }

        self.main_obj.mq_channel.queue_declare(queue=callback_queue)

        self.main_obj.mq_channel.basic_publish(exchange='',
                                               routing_key=callback_queue,
                                               body=json.dumps(data))


    def parse_task_data(self,os_type,data):
        '''
        解析任务数据并执行
        :param os_type:
        :param data:
        :return:
        '''
        applied_list = [] # 所有已经执行的子任务(section)都放到这个列表中
        applied_result = [] # 把所有应用得section的执行结果放到这里
        last_loop_section_set_len = len(applied_list)
        while True:
            for section in data:
                if section.get('called_flag'): # 表示已经执行过了
                    print('_____called alread')
                else:
                    apply_status,result = self.apply_section(section)
                    if apply_status == True: # 代表执行成功
                        applied_list.append(section)
                        applied_result += result



            if len(applied_list) == last_loop_section_set_len:
                # 这两个变量相等,代表2种可能
                # 1,任务执行完成
                # 2,相互依赖形成了死锁
                break
            last_loop_section_set_len = len(applied_list)

        self.task_callback(self.task_body['callback_queue'],applied_result)



    def check_pre_requisites(self,conditions):
        '''
        检查依赖条件是否成立
        :param conditions:
        :return:
        '''
        condition_results = []
        for condition in conditions:
            cmd_res = subprocess.run(condition,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            condition_results.append(int(cmd_res.stdout.decode().strip()))


    def run_cmds(self,cmd_list):
        '''
        运行命令,返回结果
        :param cmd_list:
        :return:
        '''
        cmd_results = []
        for cmd in cmd_list:
            cmd_res = subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_results.append([cmd_res.returncode,cmd_res.stderr.decode()])

        return cmd_results  #所有命令都执行成功,返回 0

    def apply_section(self,section_data):
        '''
        执行指定得 task section
        :param section_data:
        :return:
        '''
        if section_data['required_list'] != None:
            # 检查requsite条件是否满足
            if self.check_pre_requisites(section_data['required_list']) == 0: # 依赖满足
                if section_data.get('file_source') == True: # 文件section 需要单独处理
                    res = self.file_handle(section_data)
                else:
                    res = self.run_cmds(section_data['raw_cmds'])
                section_data['called_flag'] = True
                return [True,res]
            else:
                return [False,res] # 依赖条件不满足
        else: # 没依赖需求,直接执行
            if section_data.get('file_source') == True: # 文件section需要单独处理
                res = self.file_handle(section_data)
            else:
                res = self.run_cmds(section_data['raw_cmds'])

            section_data['called_flag'] = True
            return [True,res]


    def file_handle(self,section_data):
        '''
        对文件进行操作
        :param section_data:
        :return:
        '''
        file_module_obj = files.FileModule(self)
        file_module_obj.process(section_data)
        return []


    def check_data_validtion(self):
        '''
        确保服务器发来的任务是本客户端上可执行的
        :return:
        '''

        os_version = platform.version().lower()
        for os_type,data in self.task_body['data'].items():
            if os_type not in os_version:
                return os_type,data

        else:
            print("salt is not supported on this os %s" % os_version)



class Needle(object):

    def __init__(self):
        self.configs = configs
        self.make_connection()
        self.client_id = self.get_needle_id()
        self.task_queue_name = "TASK_Q_%s" % self.client_id

    def get_needle_id(self):
        '''
        去服务器端取自己的ID
        :return:
        '''
        return configs.NEEDLE_CLIENT_ID

    def listen(self):
        '''
        开始监听服务器得call
        :return:
        '''
        self.msg_consume()


    def make_connection(self):
        self.mq_conn = pika.BlockingConnection(pika.ConnectionParameters(
            configs.MQ_CONN['host']
        ))

        self.mq_channel = self.mq_conn.channel()

    def publish(self,data):
        # 声明 queue
        self.mq_channel.queue_declare(queue='hello')
        self.mq_channel.basic_publish(exchange='',
                                      routing_key='hello',
                                      body='hello world!')

        self.mq_conn.close()


    def msg_callback(self,ch,method,properties,body):
        therad = threading.Thread(target=self.start_thread,args=(body,))
        therad.start()


    def start_thread(self,task_body):
        task = TaskHandle(self,task_body)
        task.processing()



    def msg_consume(self):
        self.mq_channel.queue_declare(queue=self.task_queue_name)

        self.mq_channel.basic_consume(self.msg_callback,
                                      queue=self.task_queue_name,
                                      no_ack=True)

        self.mq_channel.start_consuming()










