"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

### Write a print statement that combines x + y into the integer value 12

# first way - cast y into a integer
print(int(y) + x)

# second way - manually change y type to integer
y = 7
print(x + y)


### Write a print statement that combines x + y into the string value 57

# first way - cast x and y to strings
print(str(x) + str(y))

# second way - manually change x and y types to strings
x = '5'
y = '7'

print(x + y)