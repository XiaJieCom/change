#!/usr/bin/env python3

from arya.backends.base_module import BaseSaltModule


class CMD(BaseSaltModule):
    def __init__(self):
        print('in cmd modle')
