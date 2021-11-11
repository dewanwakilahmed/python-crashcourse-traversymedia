# A function is a block of code which only runs when it's called.
# In Python, we do not use curly brackets, we use identation with tabs and spaces.

# Create a Function
def sayHello(name='Sam'):
    print(f'Hello {name}')

sayHello('Dewan')

sayHello()

# Return Values
def getSum(num1, num2):
  total = num1 + num2
  return total

sum = getSum(3, 4)

print(sum)

# A lamba function is a small anonymous function.
# A lamba function can take any number of arguments, but can only have on expression.
# Very similar to arrow functions.

getsum = lambda num1, num2 : num1 + num2
print(getSum(10, 3))