from mypackage.main import CLIArgs, main_func
import tyro

if __name__ == "__main__":
    args = tyro.cli(CLIArgs)
    main_func(args.name, args.times)