# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create Tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a Constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Single value needs trailing command
fruits3 = ('Apples')
print(fruits3, type(fruits3))

fruits4 = ('Apples', )
print(fruits4, type(fruits4))

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'
print(fruits)

# Delete Tuple
del fruits2

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create Set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}
print(fruits_set)

# Check if a item in Set
print('Apples' in fruits_set)

# Add an item to Set
fruits_set.add('Grapes')
print(fruits_set)

# Remove an item from Set
fruits_set.remove('Apples')
print(fruits_set)

# Add duplicate
fruits_set.add('Mangoes')
print(fruits_set)

# Clear Set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set
print(fruits_set)