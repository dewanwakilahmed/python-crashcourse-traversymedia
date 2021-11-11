# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a Constructor
numbers2 = list((6, 7, 8, 9, 10))

print(numbers, numbers2)
print(fruits)

# Get a Value
print(fruits[2])

# Get Length
print(len(fruits))

# Append to List
fruits.append('Mangoes')
print(fruits)

# Insert into Position
fruits.insert(2, 'Strawberries')
print(fruits)

# Change a value
fruits[0] = 'Blueberries'
print(fruits)

# Remove from List
fruits.remove('Grapes')
print(fruits)

# Remove with Pop
fruits.pop(2)
print(fruits)

# Reverse the List
fruits.reverse()
print(fruits)

# Reverse Sort Lists
fruits.sort(reverse=True)
print(fruits)

# Sort List
fruits.sort()
print(fruits)
