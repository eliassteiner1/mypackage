from dataclasses import dataclass
import tyro
from .core.funx import greet


@dataclass
class CLIArgs:
    """
    controls the cli of tyro and directly stores the input arguments (sys.argv)
    
    Attributes:
        name: which name to greet
        times: how many times to greet
    """
    name: str = "World"
    times: int = 1
    
def somethingelse():
    print("wow you got here")

def greetings_producer(name: str = "World", times: int = 1):
    """ important function: prints a greeting multiple times. uses greet method from core """
    for _ in range(times):
        greet(name)

def main_func(argv=None):
    """ main entry point """
    cli_args = tyro.cli(CLIArgs, args=argv)
    greetings_producer(cli_args.name, cli_args.times)
    



    

    