import argparse

from greetings import hello, bye

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say hello or bye to someone.")
    parser.add_argument("command", choices=["hello", "bye"])
    parser.add_argument("--name", required=True, help="Name of the person to greet")
    
    args = parser.parse_args()

    if args.command == "hello":
        hello(args.name)
    else:
        bye(args.name)
