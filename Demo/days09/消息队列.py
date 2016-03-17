import time,threading,queue

def consumer(n):
    while True:
        print('\033[32;1m consermer [%s] \033[0m get task: %s'%(n,q.get()))
        time.sleep(0.1)
        q.task_done()
def producer(n):
    count = 1
    while True:
        print('producer [%s] produced a new task:%s' %(n,count))
        q.put(count)
        count +=1
        q.join()
        print('都吃上啦')
c1 = threading.Thread(target=consumer,args=['haha',])
c2 = threading.Thread(target=consumer,args=['aa',])
c3 = threading.Thread(target=consumer,args=['bb',])

p1 = threading.Thread(target=producer,args=['tom',])
p2 = threading.Thread(target=producer,args=['cat',])

q = queue.Queue()
c1.start()
c2.start()
c3.start()

p1.start()
p2.start()

