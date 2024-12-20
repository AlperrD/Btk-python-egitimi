# dictionary key - value şeklinde gelir.

# def display_user(*args):
#     print(type(args))
#     print(args)

# display_user(2,3,4,5,6,7,8)

def display_user(**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

display_user(username = "AlperD", email = "alper@gmail.com", country = "Türkiye")

def myFunc (a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60, key1 = "value 1", key2 = "value 2") # İlk üç değerden kwargs'a gelene kadar olan kısım args içine alınır.
