# using global keyword to modify global variable in function definetion

def inc():
    global a
    a = a+1
    return a
a = 10
print(a)
z = inc()
print(z)
