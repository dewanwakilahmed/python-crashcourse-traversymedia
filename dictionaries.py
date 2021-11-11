# A Dictionary is a collection which is unordered and, changeable and indexed. No duplicate members.

# Create a Dictionary
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}
# print(person, type(person))

# Using a Constructor
person2 = dict(first_name='Sarah', last_name='Williams', age=28)
print(person2, type(person2))

# Get a Value
print(person['first_name'])
print(person.get('last_name'))

# Add Key/Value
person['phone'] = '555-555-555'
print(person)

# Get Dictionary Keys
print(person.keys())

# Get Dictionary Items
print(person.items())

# Copy Dictionary
person3 = person.copy()
person3['city'] = 'Boston'
print(person3)

# Remove Item
del(person3['age'])
print(person3)

person3.pop('phone')
print(person3)

# Clear
person3.clear()
print(person3)

# Get Length
print(len(person2))

# List of Dictionaries
people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 26}
]
print(people, type(people))
print(people[1]['age'])