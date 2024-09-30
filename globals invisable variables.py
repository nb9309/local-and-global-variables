a = 100
b = 'ravi'
def fun_name():
    d = globals()
    for w,val in d.items():
        print('{} ---> {}'.format(w,val))
    print('a ---> ',d.get('a'))
    print('b ----> ',d['b'])

fun_name()