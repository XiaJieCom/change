#!/usr/bin/env python3

# 所有的自定义模块 都先在这里注册
# 格式 '模块名':'模块名.方法名'

from arya.plugins import cmd,state
actions = {
    'cmd':cmd.CMD,
    'state':state.State,
}


