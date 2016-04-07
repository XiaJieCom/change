#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika
import time

#连接服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')
#声明rpc的queue

def cmd(command):
    if len(command) == 0:
        print('Error!')
    else:
        print('ok')

def on_request(ch, method, props, body):
    command = str(body)
    print(" [.] fib(%s)" % command)
    response = cmd(command)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" Awaiting RPC requests")
channel.start_consuming()