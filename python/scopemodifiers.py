# x=50
# def demo():
#     global x #trying to access global variable
#     x=34
#     # print(x)

# demo()
# print(x)
# x=105
# def sample():
#     x=35
#     # print(x)
# def sample1():
#     global x
#     x=45
#     # print(x)
# sample()
# sample1()
# print(x)
#with the help of global keyword, we can update global  variable from local .

def sample():
    global x
    x='kiran'
sample()
print(x)

#with the help of global keyword, we can declare variables globally from the function also.

# a=125
# def outer():
#     a=12 
#     def inner():
#         nonlocal a
#         a=15
#         print(a,"printing a in inner function")
#     inner()
#     print(a,"printing a in outer function")
# outer()
# print(a,"globally printing")

