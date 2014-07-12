"""
This file is imported by SConstuct and is used for build configuration:
change to suit your platform
"""

#Default ccflags and ccflags used for debug
ccflags = '-O3'
debug_ccflags = ''

include_dirs = []

#Special: do we want mingw on windows?
USE_MINGW = True
