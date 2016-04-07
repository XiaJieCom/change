import rpyc
try:
    conn = rpyc.connect('localhost',9990)
except:
    print('Connetion fail!')
while 1:
    try:
        cmd = input('请输入您的指令：')
        if cmd == 'q' or cmd=='exit':
            break
        cr = conn.root.cmd(cmd)
        if cr == 0:
            print(cmd,'执行成功!')
        else:
            print(cmd,'执行失败!')
    except:
        conn.close()