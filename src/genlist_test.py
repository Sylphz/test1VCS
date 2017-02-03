#! Insert the curret directory path to python path
import sys
import os

cwd=os.getcwd() # current Working Directory
sys.path.append(cwd)
# print(sys.path)

# Test the module:generate_list
for x in xrange(1000):
    from generate_list import printIt
    printIt()
