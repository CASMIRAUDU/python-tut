# Strings in python are surronded by either single or double quotation marks. Let's look at string formatting and some string methods
name = ' isreal'
age = 17
# Concatenate
print('Hello, my name is as you all know' + name + ' and I am as you know the digits ' + str(age) + ' that is actually my age')
# String Formatting
# Argument by position
 print('My name is as  {name} and I am {age}' . format(name=name, age=age))
# F_Strings (3.6+)
 print(f'Hello, my name is {name} and I am {age}')
# String Methods
s = 'helloworld'
# Capitalize string
print(s. capitalize())
# Make all uppercase
print(s . upper())
# Make all lower
print(s. lower())
# Swap case
print(s. swapcase())
# get length
print(len(s))
# replace
print(s.replace('world', 'everyone'))
# count
sub = 'h'
print(s.count(sub))
# starts with
print (s.endswith('d'))
# split into a list
print(s.split())
# find position
print(s.find('r'))
# is all alphanumeric
print(s.isalnum())
# is all alphabetic
print(s.isalpha())
# is all numeric
print(s.isnumeric()) 

