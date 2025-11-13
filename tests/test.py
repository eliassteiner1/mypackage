import os
import sys

# add this package to sys.path. this is intended, and allows for stuff from here to be executed without installing the 
# package. otherwise stuff run from here only finds modules and packages from directly inside the test folder but 
# doesn't see the stuff that's actually in the main package.
# 
# os.path.dirname(__file__) -> path to the parent folder of this file
# os.path.join(os.path.dirname(__file__), '..') -> parent_folder/..
# os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) -> now converts the relative /.. into absolute path
# sys.path.insert(0, path) -> adds this package main folder to sys path in the first location so no conflicts happen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# this will only import anything exposed/(also imported) in the topmost __init__.py!
import mypackage

# # this will directly import the whole main.py file, and not care about what's exposed in it's __init__.py
# import mypackage.main

# # this will import anything that is exposed in mypackage/core __init__.py! but also seems to traverse down the parent 
# # __init__.py to this also imports stuff exposed in the topmost __init__.py!
# import mypackage.core

# # this will directly be able to import unexposed stuff
# from mypackage.main import main_func


# this just directly tests some important functions from the package
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    # short circuit the cli's ;)
    mypackage.main_func(argv=["--name", "Asdf", "--times", "3"])
    
    
