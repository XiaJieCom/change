
import threading
import time

def sayhi(num):
    print('running on nuber:%s' %num)
    time.sleep(3)

if __name__ == '__main__':
    '''

    t1 = threading.Thread(target=sayhi,args=(1,))
    t2 = threading.Thread(target=sayhi,args=(2,))

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())

    '''
    t_list = []
    for i in range(20):
        t = threading.Thread(target=sayhi,args=[i,])
        t.start()
        t_list.append(t)
    for i in t_list:
        i.join()
    print('----done-----')


'''
class Demo(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print('running on number:%s' %self.num)
        time.sleep(3)
if __name__ == '__main__':
    t1 = Demo(1)
    t2 = Demo(2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('---done---')
    '''