"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can
continue entering numbers even if they make a mistake and enter text instead of a number.
"""
while True:
    try:
        number1=input("Enter the first number: ")
        number1=int(number1)
    except ValueError:
        print("Enter a numerical value: ")
        pass
    else:
        while True:
            try:
                number2=input("Enter the second number: ")
                number2=int(number2)
            except ValueError:
                print("Enter a numerical value: ")
                pass
            else:
                sum=number1+number2
                print(f"The result is : {sum}")
                break
        break