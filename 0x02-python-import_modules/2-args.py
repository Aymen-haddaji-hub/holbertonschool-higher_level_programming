#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv

    count = len(argv)
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for index in range(count):
        print("{}: {}".format(i + 1, argv[index + 1]))
