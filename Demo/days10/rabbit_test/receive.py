import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch,method,properties,body):
    print("[x] received %r" %body)
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print('[*] waiting for messages. To exit press ...')
channel.start_consuming()