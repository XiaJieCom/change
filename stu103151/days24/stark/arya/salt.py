#!/usr/bin/env python3

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","stark.settings")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR) # stark 的路径
    from arya.action_list import actions
    from arya.backends.utils import ArgvManagement
    obj = ArgvManagement(sys.argv)



