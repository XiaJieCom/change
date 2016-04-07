import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import sql_init


def menu():
    pass




def run():
    sql_init.init_start()
    menu()
if __name__ == '__main__':
    host = run()
