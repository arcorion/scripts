#!/usr/bin/env python3
# Christopher Crader
# Take a monthly rate and returns it as an yearly rate.
# If multiple arguments passed, returns a range
import sys

def main():
    output: str = ""
    for i in range(1, len(sys.argv)):
        yearly = month_to_year(float(sys.argv[i]))
        if output != "":
            output = output + \
            " - {amount:.2f}".format(amount = yearly) 
        else:
            output = "Yearly: " + "{amount:.2f}".format(amount = yearly) 

    print(output)

def month_to_year(monthly: float) -> float:
    months_per_year = 12
    return monthly * months_per_year
    
if __name__ == "__main__":
    main()
