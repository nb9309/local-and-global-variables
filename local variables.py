def add(a,b):  #a,b are local variables
    c = a+b    # c is a local variable
    return a,b,c

z = add(10,20)
print('{}+{}={}'.format(z[0],z[1],z[2]))