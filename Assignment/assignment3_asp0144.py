# Declaraing epsilon
epsilon = 0.0001

# Declaring user_input to -1
user_input = -1

# Looping until user input positive number
while user_input < 0:
    user_input = int(input('Enter a number: '))
    if user_input < 0:
        print('Your number must be positive integer. Please try again')

estimate = user_input
goodness = 1

# looping until goodness doesn't get less than epsilon
while goodness > epsilon:
    goodness = abs ( (user_input/estimate) - estimate)
    estimate = ( (user_input / estimate) + estimate) / 2

# printing the final input
print(f'{user_input} estimate:', end=' ')
print(format(estimate, '.3f'))