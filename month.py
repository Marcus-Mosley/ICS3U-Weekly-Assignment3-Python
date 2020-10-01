#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program gives the number of days in a month,
#     even when there is a leap year


def main():
    # This function gives the number of days in a month,
    #     even when there is a leap year

    # Input
    year_str = 0
    month_str = input("Enter a month in the form of a number (1-12): ")
    print("")
    if month_str == 2:
        year_str = input("Please enter the year: ")
        print("")

    # Process & Output
    try:
        month_int = int(month_str)
        year_int = int(year_str)
    except Exception:
        print("You have not inputted two integers,"
              " please input a number for both the month"
              " (0 - 12) and the year!")
    else:
        if month_int == 1:
            print("January has 31 days!")
        elif month_int == 2:
            if year_int % 4 == 0:
                if year_int % 100 == 0:
                    if year_int % 400 == 0:
                        print("February has 29 days during a leap year!")
                    else:
                        print("February has 28 days during a common year!")
                else:
                    print("February has 29 days during a leap year!")
            else:
                print("February has 28 days during a common year!")
        elif month_int == 3:
            print("March has 31 days!")
        elif month_int == 4:
            print("April has 30 days!")
        elif month_int == 5:
            print("May has 31 days!")
        elif month_int == 6:
            print("June has 30 days!")
        elif month_int == 7:
            print("July has 31 days!")
        elif month_int == 8:
            print("August has 31 days!")
        elif month_int == 9:
            print("September has 30 days!")
        elif month_int == 10:
            print("October has 31 days!")
        elif month_int == 11:
            print("November has 30 days!")
        elif month_int == 12:
            print("December has 31 days!")
        else:
            print("That is not a valid month!")


if __name__ == "__main__":
    main()
