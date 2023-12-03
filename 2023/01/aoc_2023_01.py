import os
import re

# Load the calibration document
# Use a regular expression and a string to read from the left and the right
# Add the finding to a running total

def main(filename):

    with open(filename,'r') as file:
        data = file.readlines()
    
    sum_of_calibration = 0
    for line in data:
        numbers = re.findall(r"\d", line)
        calibration_value = int(numbers[0]+numbers[-1])
        sum_of_calibration += calibration_value
    
    print("Sum of calibration:", sum_of_calibration)
    
    spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

if __name__ == "__main__":
    filename = "calibration_data.txt"
    main(filename)