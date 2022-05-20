#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates whether you can date a daughter


def main():
    # I calculate circumference

    # input
    is_rich = input("Are you rich (y/n): ")
    is_goodlooking = input("Are you good looking (y/n): ")

    # process & output
    if is_rich == "y" or is_goodlooking == "y":
        print("You can date her")
    elif is_rich == "n" and is_goodlooking == "n":
        print("You can't date her")
    else:
        print("Invalid input")

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
