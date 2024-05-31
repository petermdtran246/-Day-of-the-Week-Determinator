# Day-of-the-Week-Determinator
This Python program helps you determine the day of the week (Sunday, Monday, etc.) based on a numerical input (1 for Sunday, 2 for Monday, and so on).

## Match Statement:

The function uses a match statement, a relatively new feature in Python, to compare the value of day with different cases:
  -  case 1: If day is 1, print "sun" (Sunday).
  -  case 2: If day is 2, print "mon" (Monday).
  -  Similar cases for day values 3 to 7.
  -  case _:: This acts as a default case. If day doesn't match any of the specific cases above, it prints "Invalid day".
