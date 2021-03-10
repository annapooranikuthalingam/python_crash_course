"""
10-6. Addition: One common problem when prompting for numerical input occurs when people provide
text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError.
Write a program that prompts for two numbers. Add them together and print the result. Catch the
ValueError if either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a number.
"""
number1=input("Enter the first number: ")
number2=input("Enter the second number: ")
try:
    sum=int(number1)+int(number2)
except ValueError:
    print("Enter a numerical value")
else:
    print(f"The result is : {sum}")

