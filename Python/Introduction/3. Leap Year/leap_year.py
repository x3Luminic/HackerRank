# Leap Year Solution

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Constraints: 1900 <= year <= 10^5
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# Thought Process:
# Ensure the year is within the constraints, firstly check the year is evenly divisible by 4
# Then check if the year is not evenly divisible by 100 or is evenly divisible by 400
def is_leap(year):
    leap = False
    
    # Write your logic here
    if 1900 < year <= 10**5:
        if year % 4 == 0:
            if year % 100 != 0 or year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))