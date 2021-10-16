#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program calculated area of parallelogram


def calcutate_area(base, height):
    # This function area of parallelogram
    # process
    area_parallel = round(base * height, 2)

    return area_parallel


def main():
    # this is he main function
    base_user = input("Enter the base of the parallelogram (cm) : ")
    height_user = input("Enter the length of the parallelogram (cm) : ")

    try:
        base_user = float(base_user)
        height_user = float(height_user)
        # call functions
        area_parallel = calcutate_area(base_user, height_user)
        print("\nThe area of the parallelogram is {0} cm²".format(area_parallel))
    except (Exception):
        print("\nInvalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
