import threading,time
def addNum():
    global num
    print('---get num:',num)
    time.sleep(1)
    lock.acquire()
    num -=1
    lock.release()
lock = threading.Lock()
num = 100
thread_list = []
for i in range(1000):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()
print(num)
    
