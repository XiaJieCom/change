import queue


#q = queue.Queue(maxsize = 3)
#先入先出
#q = queue.LifoQueue(maxsize = 3)
#后入先出
q = queue.PriorityQueue(maxsize = 3)
#根据优先级取值,值越小,优先级越高
print(q.empty())

q.put((1,100))
q.put((20,102))
q.put((3,103))

#q.put(4,timeout=1)
'''
q.put(123)
q.put('asd')
q.put(34534534)
'''
print(q.get())
print(q.get())
q.put((4,104))
print(q.full())
