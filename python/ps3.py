# ip=[10,2,2,4,3,5]
# sm=ip[0]
# ssm=ip[0]
# for x in ip:
#     if x<sm:
#        ssm=sm 
#        sm=x
#     elif x<ssm and x!=sm:
#         ssm=x
# print("smallest num is",sm)
# print("second smallest number is", ssm)

# x=23
# is_prime=True

# for i in range(2,x):
#     if x%i==0:
#        is_prime=False
#        break
# if(is_prime):
#     print("num is prime")
# else:
#     print("num is not prime")  


# make a list of prime numbers within range of 1 to 25 using comprehension
def PrimeCheck(x):
    is_prime=True
    for i in range(2,x):
        if x%i==0:
            is_prime=False
            break
    if(x>1 and is_prime):
        return True
    else:
       return False

# op={x**2 for x in range(1,25) if PrimeCheck(x)}
# op={x:x**2 for x in range(1,25)}

# print(op)
# 1.list comprehnsion-->[] 
# 2.tuple comprehension--->tuple()
# 3.set comprehension--->{}
# 4.dictionary comprehensions-->{}



#((2,4),(3,9),(4,16),(5,25)) using tuple comprehensions

op=tuple((x,x**2) for x in range(1,10))
print(op)

# task:
# ------

# ['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']

# (('sravani','female'),('sravan','male'),('kumar','male'))