def sym(a,b):
    print('hey im symming')
    c = a+b
    global z
    z = 4

    return c

z = 3
print(sym(2,3))
print(z)