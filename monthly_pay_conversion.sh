#!/usr/bin/bash
# Call two Python scripts for converting from monthly to hourly and yearly pay
# Takes one or more numbers

echo "Conversion from monthly pay to:"
echo "$(mo_to_yr.py $@)"
echo "$(mo_to_hr.py $@)"
