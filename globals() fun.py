a= 30
b = 40
def add():
    a = 100
    b = 200
    c = a+b+globals()['a']+globals().get('b')
    print(c)

add()