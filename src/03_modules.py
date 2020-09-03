"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# This link was also helpful: https://www.pythonforbeginners.com/system/python-sys-argv
print('This is the name of the script: ', sys.argv[0])
print('Number of arguments: ', len(sys.argv))
print('The arguments are: ' , str(sys.argv))

# Print out the OS platform you're using:
print('The OS platform I am using is', (sys.platform))

# Print out the version of Python you're using:
print('The version of Python I am using is', (sys.version))


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('My current process ID is', (os.getpid())) # this is a function - needs ()

# Print the current working directory (cwd):
print('My current working directory is', (os.getcwd()))

# Print out your machine's login name
print("My machine's login name is", (os.getlogin()))
print("My machine's name is", (os.uname().nodename))

