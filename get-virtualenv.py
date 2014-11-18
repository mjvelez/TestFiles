"""
This command is used to install virtual environments for programming.

This way, projects can be completely separate from each other.

This is best practices
"""


import sys
sys.version_info(2, 6, 4, 'final', 0)
if not sys.version_info[:2] == (2, 6):
    print "Error, I need python 2.6"
else:
    from my_module import twoPointSixCode