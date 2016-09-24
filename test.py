#!/usr/bin/python3

from sys import stdin

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(bool(int(x)))

    print(input_list)


if __name__ == "__main__":
    main()
