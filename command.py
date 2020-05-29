#!/bin/python3
import argparse

def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(description='Python cli boilerplate', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
        '--num',
        help='A number',
        metavar='int',
        type=int,
        default=10)
    args = parser.parse_args()
    return args


def main():
    """Do stuff here"""
    args = get_args()

if __name__ == '__main__':
    main()
