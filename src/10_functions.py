# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
    return x % 2 == 0

print(is_even(7))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# updating function
# def is_even_prints(x):
#     if is_even(x) == True:
#         print('Even!')
#     else:
#         print('Odd')

def is_even_prints(x):
    print("Even!" if is_even(x) else "Odd")

is_even_prints(num)
   
