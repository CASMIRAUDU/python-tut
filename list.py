# A list is a collection which is odered and changeable. Allows duplicate members.
# creat list
numbers = [1, 2, 3, 4, 5]
fruits = [ 'Apples', 'Orange', 'grapes', 'pears']
# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))
# Get a value
print(fruits[1])
# Get lenght
print(len(fruits))
# Append to list
fruits.append('mangos')
# remove from list
fruits.remove('grapes')
# Insert into position
fruits.insert(2, 'Strawberries')
# Change value
fruits[0] = 'Blueberries'
# Remove with pop
fruits.pop(2)
# Reverse list
fruits.reverse()
# sort list
fruits.sort()
# Reverse sort
fruits.sort(reverse=true)
print(fruits)