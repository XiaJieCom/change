#Python和shell交互
import os
value = 123
os.environ['var'] = str(value)
os.system('echo $var')

