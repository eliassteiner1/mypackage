import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mypackage


# this is an entry point if the package is not installed. Then this script is run
if __name__ == "__main__":
    mypackage.main_func()