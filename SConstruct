"""
SConstruct for building clipboard with MinGW under Win32
"""

import glob
import os

import clipboard_config

# Helper function
def read_bool(s):
    try:
        b = bool(int(s))
    except:
        ch = str(s).lower()
        if   ch in set(["true", "yes", "t", "y"]): b = True
        elif ch in set(["false", "no", "f", "n"]): b = False
        else:                                      b = bool(s)
    return b

ccflags = clipboard_config.ccflags

libs = [
    'user32', 
    'gdi32', 
    'kernel32'
]

include_dirs = list(clipboard_config.include_dirs)

# Any command line build changes
debug = read_bool(ARGUMENTS.get('debug', 0))

if debug:
    print "DEBUG BUILD"
    ccflags = clipboard_config.debug_ccflags

# Build environment and variable
env = Environment(
    ENV = os.environ,
    CPPPATH = ['.'],
)
if clipboard_config.USE_MINGW:
    mingw_tool = Tool('mingw')
    mingw_tool(env)
for d in include_dirs:
    Repository(d)

# Actual build
env.Program(
    target = 'clipboard', 
    source = glob.glob('*.cpp'),
    LIBS = libs, #Don't need LIBPATH
    CCFLAGS = ccflags,
)
