import gevent




def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')
def bar():
    print('Running in bar')
    gevent.sleep(0)
    print('Explicit context switch to bar again')
def ex():
    print('Running in ex')
    gevent.sleep(0)
    print('Explicit context switch to ex again')

gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
        gevent.spawn(ex),

     ])

