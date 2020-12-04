# Understanding the type casting, print formats & input

"""
x = 21
y = 'START'
Development = ('node js', 'angular js', 'java', 'python')


print(type(x))
print(type(y))
print(type('Development'))

x = str(x)

print('after type casting x is converted to a string')
print(type(x))

Development = list (Development)
print('After type casting development is converted to a LIST . ')
print(type(Development))
"""

"""
x = 21
y = 'START'
Development = ('node js', 'angular js', 'java', 'python')

print(y)
print('The value of y is :', y)
print ('The value of y is : ' " " + y + " " + str(31))

print('%s y is the value of y' %y)
print ("%d is the value of x" %x)

print('%s is the value of y and %d is the value of x ' % (y,x))
print('%s is the value of Development ' % list (Development))
"""

'''inputstr = input('Enter any string: ')
print(type(inputstr))
inputint = input('Enter any number : ')
print(type(inputint))'''

inputstr = input('Enter any string: ')
print(type(inputstr))

inputint = input('Enter any number : ')
print(type(inputint))