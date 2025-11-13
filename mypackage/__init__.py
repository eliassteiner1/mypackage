# funtion explicitly imported here is then usable as mypackage.main_func instead of mypackage.main.main_func. 
# I guess this can be used to shorten the namespace for soome functions
# from .main import main_func

# # stuff like this just "provides" these modules to the outside but still requires to use mypackage.main.something
# # so this kind of preserves the namespace and is preferred I guess
# from . import main


from .main import main_func, cli
from . import core



# this only controls what gets imported when "from mypackage import *"" is used
# __all__ = [
#     "main_func"
# ]

