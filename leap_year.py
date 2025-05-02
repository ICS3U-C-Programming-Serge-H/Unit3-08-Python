#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: Mar 28, 2025
# This program will ask the user to enter a year and then tell the user if it is a "leap" year.


def main():
    try:
        # Get user input
        user_year = int(input("Enter a year: "))

        is_leap = False
        error_message = False

        # Process
        if user_year < 0:
            error_message = "Year must be a non-negative integer."
        elif user_year % 4 == 0:
            if user_year % 100 == 0:
                if user_year % 400 == 0:
                    is_leap = True
                else:
                    is_leap = False
            else:
                is_leap = True
        else:
            is_leap = False

    except ValueError:
        error_message = "Enter a valid year."

    # Output
    if error_message:
        print(error_message)
    elif is_leap:
        print(f"{user_year} is a leap year.")
    else:
        print(f"{user_year} is not a leap year.")


main()
