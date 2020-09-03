#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    print("{:d} {:s}{:s}".format(l - 1, "argument" if l <= 2 else "arguments",
                                 "." if l == 1 else ":"))
    for index, alist in enumerate(args):
        if index > 0:
            print("{:d} {:s}".format(index, alist))

