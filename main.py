"""Income Tax Calculator: A simple program that calculates users income tax"""

# Get salary from user
while True:
    try:
        salary = float(raw_input("Please enter your salary: "))
        break
    except ValueError:
        print "Invalid input, please try again..."

#TODO: Deduct SSS and Philhealth Premiums


if salary <= 10000:
    print "Your salary is P" + format(salary * .95, ".2f")
elif salary <= 30000:
    print "Your salary is P" + \
          format(salary - (((salary - 10000) * .10) + 500), ".2f")
elif salary <= 70000:
    print "Your salary is P" + \
          format(salary - (((salary - 30000) * .15) + 2500), ".2f")
elif salary <= 140000:
    print "Your salary is P" + \
          format(salary - (((salary - 70000) * .20) + 8500), ".2f")
elif salary <= 250000:
    print "Your salary is P" + \
          format(salary - (((salary - 140000) * .25) + 22500), ".2f")
elif salary <= 500000:
    print "Your salary is P" + \
          format(salary - (((salary - 250000) * .30) + 50000), ".2f")
else:
    print "Your salary is P" + \
          format(salary - (((salary - 500000) * .32) + 125000), ".2f")
