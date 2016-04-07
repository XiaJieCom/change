import redis
class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis()
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm87.5'
    def public(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub