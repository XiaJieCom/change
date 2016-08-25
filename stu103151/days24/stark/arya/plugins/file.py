#!/usr/bin/env python3

from Arya.backends.base_module import BaseSaltModule
'''
      file.managed:
        - source: salt://apache/httpd.conf
        - user: root
        - group: root
        - mode: 644
        - require:
          - pkg: nginx
'''

class File(BaseSaltModule):
    def managed(self,*args,**kwargs):
        kwargs['sub_action'] = "managed"
        return kwargs

    def source(self,*args,**kwargs):
        pass

    def user(self,*args,**kwargs):
        pass

    def group(self,*args,**kwargs):
        pass

    def mode(self,*args,**kwargs):
        pass

    def is_required(self,*args,**kwargs):
        file_pach = args[1]
        cmd = "test -f %s;echo$?" % file_pach
        return cmd








