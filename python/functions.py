#it is the function which gives always same o/p--->static function
def Sample():
    print("hii")

Sample()

# function which gives different o/ps as per the different i/ps-->dynamic function.
# to define dynamic function-->we need parameters and arguments
#function without return
# def DynamicFun(name):
#     print(f"helloo {name}")

# DynamicFun('harish')
# DynamicFun('kiran')
# DynamicFun('lakshmi')
# DynamicFun('Nandu')

#function with return

def Theatre(mve):
    print(f"now showing {mve}")
    return 'Thankyou-visit again'
# print(Theatre('kingdom'))
# print(Theatre('HHVM'))
x=print(Theatre('kingdom'))
print(x)

#return is used to return some values from function and then re-use 
# that value anywhere in the program

# (additon of 2 numbers)*(subtaction of 2 num)


def add(a,b):
    sum=a+b
    return sum
    print("hello") #this will be ignored
#this function will returns sum 

def sub(a,b):
    sub=a-b
    return sub
    print("hii") #this will be ignored
#this function will returns sub

x=add(12,7)
y=sub(12,7)

op=x*y
print(op)

#function
#static function
#dynamic function
#function without return
#function with return
