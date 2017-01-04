#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

# The script is used by python tab Completion script
import sys
import readline
import rlcompleter
import atexit
import os

# tab completion
readline.parse_and_bind('tab: complete')
# history file
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
    atexit.register(readline.write_history_file, histfile)

    # del os, histfile, readline, rlcompleter