import sys
from . import calc
from . import convert
import argparse


def main():
    args=sys.argv[1:]
    comm=args[0]

    argu=' '.join(args[1:])

    if comm=='calc':
        sys.stdout.write(str(calc.calc(argu)))
    if comm=='conv':
        sys.stdout.write(str(convert.conv(argu)))
if __name__=="__main__":
    main()