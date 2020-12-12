#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program does exponents with for loops


def main():
    # Function does exponents with for loops

    print("I will give you the square of every positive number up to",
          "the inputted number")

    # Input
    number_string = input("Enter number: ")

    # Process
    try:
        number = int(number_string)
        assert number > 0

        for loop_counter in range(number + 1):
            number_exponent = loop_counter ** 2
            # Output
            print("{0}² = {1}".format(loop_counter, number_exponent))

    except AssertionError:
        # Output
        print("This isn't a valid number")
    except Exception:
        # Output
        print("This isn't a valid number")


if __name__ == "__main__":
    main()
