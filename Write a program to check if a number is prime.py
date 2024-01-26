
def is_prime(number):

    # Check if the number is less than 2, as 0 and 1 are not prime numbers

    if number < 2:

        return False

    

    # Check for divisibility from 2 to the square root of the number

    for i in range(2, int(number**0.5) + 1):

        if number % i == 0:

            return False

    

    # If no divisor is found, the number is prime

    return True



# Taking user input

num = int(input("Enter a number: "))



# Checking if the number is prime and printing the result

if is_prime(num):

    print(f"{num} is a prime number.")

else:

    print(f"{num} is not a prime number.")



