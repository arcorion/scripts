#!/usr/bin/env python3
# Take a monthly rate and returns it a an hourly rate.
# If multiple arguments passed, returns a range
import sys

def main():
    output: str = ""
    for i in range(1, len(sys.argv)):
        hourly = month_to_hour(float(sys.argv[i]))
        if output != "":
            output = output + \
                     " - {amount:.2f}".format(amount = hourly) 
        else:
            output = "Hourly: " + "{amount:.2f}".format(amount = hourly) 

    print(output)

def month_to_hour(monthly: float) -> float:
    hours_per_week = 40
    weeks_per_month = 4.34
    return monthly / hours_per_week / weeks_per_month 
    
if __name__ == "__main__":
    main()
