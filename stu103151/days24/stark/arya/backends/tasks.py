#!/usr/bin/env python3

import pika
import json

class TaskHandle(object):
    '''
    generate task
    '''
    def __init__(self,db_model,task_data,settings,module_obj):
        self.db_module = db_model
        self.task_data = task_data
        self.settings = settings
        self.module_obj = module_obj # 哪个模板调用这个类,这个变量就是谁
        self.make_connection()


    def apply_new_task(self):
        '''
        creata s task record in db and return the task id
        :return:
        '''
        new_task_obj = self.db_module.Task()
        new_task_obj.save()
        self.task_id = new_task_obj.id

    def dispatch_task(self):
        '''
        format the task data and make it ready to sent
        :return:
        '''
        if self.apply_new_task():
            self.callback_queue_name = "TASK_CALLBACK_%s" %self.task_id
            data = {
                'data':self.task_data,
                'id':self.task_id,
                'callback_queue':self.callback_queue_name,
                'token':None
            }

        for os_type,os_config_data in self.task_data.items():
            print("________os",os_type)
            for mod_data in os_config_data:
                print('________mod data')
                print(mod_data)

        for host in self.module_obj.host_list:
            self.publish(data,host)
        self.wait_callback()


    def make_connection(self):
        self.mq_conn = pika.BlockingConnection(pika.ConnectionParameters(
            self.settings.MQ_CONN['host'],port=self.settings.MQ_CONN['port']))
        self.mq_channel = self.mq_channel()


    def publish(self,task_data,host):
        queue_name = "TASK_Q_%s" %host.id
        self.mq_channel.queue_declare(queue=queue_name)

        self.mq_channel.basic_publish(exchange='',
                                      routing_key=queue_name,
                                      body=json.dumps(task_data))

    def close_connection(self):
        self.mq_conn.close()

    def task_callback(self,ch,method,properties,body):
        print(body)

    def wait_callback(self):
        '''
        get task callback
        :return:
        '''
        self.mq_channel.queue_declare(queue=self.callback_queue_name)

        self.mq_channel.basic_consume(self.task_callback,
                                      queue=self.callback_queue_name,
                                      no_ack=True)
        self.mq_channel.start_consuming()




