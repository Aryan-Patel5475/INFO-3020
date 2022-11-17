print('Welcome to the Compound Interest Calculator.')

# Declaring variable in Compound Interest formula and taking in user input
P = float(input('Please enter the initial amount of your investment: '))
r = float(input('Please enter the interest rate (e.g., \'0.3\' for 3% interest): '))
t = float(input('Please enter the number of years for the investment: '))
n = float(input('Please enter the number of compounding per year: '))

# Calculating the final balance using compound interest formula
Final_Balance = P * float(pow(1 + (r/n), (n * t)))

# Calcularing interest by minusing Initial investment from final balance
Interest_Earned = Final_Balance - P

# Outputting the result
print('Original Investment: $', end='')
# formating ouput so it has commas and upto 2 decimal point
print("{:,.2f}".format(P))

print('Interest Earned:     $', end='')
print("{:,.2f}".format(Interest_Earned))

print('Final Balance:       $', end='')
print("{:,.2f}".format(Final_Balance))
