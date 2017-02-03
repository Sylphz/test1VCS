import random
def generate_list():
    alist = [x for x in range(random.radint(-10,10))]
    return alist

"""
print a generate_list
"""

def printIt():
    print(generate_list())
    
def main():
    printIt()
    
"""
If this script file is called, it will run main() directly
"""

if_name_=='_main_'
    print("Test printIt():")
    main()