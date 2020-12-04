"""
def main():
    print('hello world')
if __name__ == '__main__':
    main()
print('learning programming')

print('Value in built variable name is :', __name__)
"""
'''
def function1():
    print("I am learning python :")
function1()
'''
'''
def square(x):
    print(x*x)
print(square(4))
'''
'''
def square(x):
    return (x*x)
print (square(4))
'''
'''
def multify(x,y):
    return(x*y)
print(multify(4,8))
'''
'''
def multiply(x, y=0):
    print("value of x=", x)
    print("value of y=", y)

    return x * y


print(multiply(y=2, x=4))
'''
# Float, List, For loop Examples
'''
for i in range(5):
    print(i, end='')
'''
'''
for i in range(3,10):
    print(i, end='')
'''
'''
for i in range(3,10,2):
    print(i, end='')
'''
'''
for i in range(15,5,-1):
    print(i,' ',end='')
'''
'''
arr_list =['MySql','Mongodb','PostGresSQL','firebase']
for i in range(len(arr_list)):
    print(arr_list[i],' ',end='')
'''

def square(n):
    return n*n
my_list=[1,2,3,4,5,6,7,8,9]
update_list=map(square,my_list)
print(update_list)
print(list(update_list))