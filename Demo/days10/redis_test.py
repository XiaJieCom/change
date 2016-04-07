import redis
'''
#普通连接
r = redis.Redis(host='localhost',port=6379)
r.set('name','tom')
print(r.get('name'))
'''

#连接池
pool = redis.ConnectionPool(host='localhost',port=6379)
r = redis.Redis(connection_pool=pool)
'''
r.set('name','cat')
print(r.get('name'))
'''


'''
#ex=过期时间(秒),px(毫秒)
r.set('name','cat',ex = 3)
'''
'''
#nx,设置为True,name不存在时,当前set操作才执行
r.set('name','cat',nx=True)
r.set('name','haha',nx=True)
#xx,设置为True,age存在时,当前set操作才执行
r.set('age','ss')
r.set('age','s',xx=True)


print(r.get('name'))
print(r.get('age'))
'''
#r.set('name','tom')
#setnx,key不存在时,才执行操作
#r.setnx('name','cat')
r.setnx('xxx',11)
#print(r.get('xxx'))
r.set('name','tom')
r.set('age',20)
print(r.mget('name','age'))