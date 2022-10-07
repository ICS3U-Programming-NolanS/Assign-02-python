#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: October 7th, 2022
# This program calculates and displays the volume and surface area
# of a parallelepiped with length 15cm and width 12cm and height 9cm

import math


def main():
    # input
    length = int(input("Enter the length of the parallelepiped (cm): "))
    width = int(input("Enter the width of the parallelepiped (cm): "))
    height = int(input("Enter the height of the parallelepiped (cm): "))

    # process
    volume = length * width * height
    surface_area = 2 * length * width + 2 * length * height + 2 * height * width

    # output
    print("The volume of the parallelepiped is = {:,.2f}cm^3".format(volume))
    print(
        "The surface area of the parallelepiped is = {:,.2f}cm^2".format(surface_area)
    )


if __name__ == "__main__":
    main()
