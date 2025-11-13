import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mypackage 
from mypackage.util.someutils import hidden_func # can also test some "not accessible" functions


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    # directly tests some isolated function
    mypackage.core.greet("Bob")
    hidden_func()