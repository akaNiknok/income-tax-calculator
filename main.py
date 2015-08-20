"""Income Tax Calculator: A simple program that calculates users income tax"""

# Get salary from user
while True:
    try:
        salary = int(raw_input("Please enter your salary: "))
        break
    except ValueError:
        print "Invalid input, please try again..."
