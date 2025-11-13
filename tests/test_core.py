import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mypackage



if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    mypackage.core.greet("Bob")