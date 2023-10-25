
print("Welcome to FizzBuzz! Enter a number to see if it's divisible by 3 or 5!")
print("Fizz = the number is divisible by 3")
print("Buzz = the number is divisible by 5")
print("FizzBuzz = the number is divisible by 3 and 5")
print("If the result is the same number you input, it isn't divisible by 5 nor 3!")

n = int(input("\nEnter your number: "))

if n % 5 == 0 and n % 3 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)