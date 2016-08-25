#!/usr/bin/env python3

from Arya.backends.base_module import BaseSaltModule


class Group(BaseSaltModule):

    def gid(self,*args,**kwargs):
        cmd = "-g %s" %args[0]
        self.raw_cmds.append(cmd)

    def present(self,*args,**kwargs):
        cmd_list = []
        name = kwargs.get('section')

        self.raw_cmds.insert(0,"groupadd %s" %name)

        cmd_list.append(' '.join(self.raw_cmds))
        cmd_list.extend(self.single_line_cmds)

        return cmd_list


    def is_required(self,*args,**kwargs):
        name = args[1]
        cmd = '''more /etc/group |awk -F':' '{print $1}' |grep -w %s -q;echo $? ''' %name

        return cmd


