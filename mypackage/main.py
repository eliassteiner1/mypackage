from dataclasses import dataclass
import tyro
from .core.funx import greet


@dataclass
class CLIArgs:
    """
    Attributes:
        name: which name to greet
        times: how many times to greet
    """
    name: str = "World"
    times: int = 1
    
    
    
def somethingelse():
    print("wow you got here")

def main_func(name: str = "World", times: int = 1):
    """Core function: prints a greeting multiple times"""
    for _ in range(times):
        greet(name)



def cli():
    """CLI entry using Tyro"""
    args = tyro.cli(CLIArgs)
    main_func(args.name, args.times)






    

    