from utils import square, is_even, celsius_to_fahrenheit, greet
num = float(input("Enter a number: "))
name = input("Enter your name: ")
print(f"Square of {num} is: {square(num)}")
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
print(f"{num} Celsius is {celsius_to_fahrenheit(num)} Fahrenheit")
print(greet(name))
