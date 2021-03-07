"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a
message that reads I love Python. Make a large shirt and a medium shirt with the default message,
and a shirt of any size with a different message.
"""
def make_shirt(size='Large',text='I Love Python'):
    """function specifies the size and text to be printed in a tshirt"""
    print(f"Size of the Tshirt is {size} and the message to be printed is '{text}'.")

make_shirt()
make_shirt(size='Medium')
make_shirt('Medium','Happy Coding')