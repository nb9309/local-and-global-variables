# a,b are global variables used in different functions

def add():
    c = a+b
    return c
b = 20
def sub():
    c = a-b
    return c

a = 10
z = add()
print('{}+{}={}'.format(a,b,z))
res = sub()
print('{}-{}={}'.format(a,b,res))