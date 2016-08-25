#!/usr/bin/env python3

from Arya.backends.base_module import BaseSaltModule


class Pkg(BaseSaltModule):

    def is_required(self,*args,**kwargs):
        return 'echo 0'



