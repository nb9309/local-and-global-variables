def add(a,b):
    c = a+b
    return c

x = int(input('enter value1: '))
y = int(input('enter value2: '))
z = add(x,y)
print('{}+{}={}'.format(x,y,z)) # x,y are global variables