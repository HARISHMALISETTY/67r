# to pack the multiple values into a list,tuple,dictionary 
# or set in simple way then we can use comprehensions

# [1,2,3,4,5,6,7,8,9,10]--->list comprehension
# ()--->tuple comprehensions

# comprehensions is a comb of  operation/expression , 
# iteration and conditions(optional)

#if we want to create a list then we will use list comprehensions

# str='welcome'

# op=[x+'-hi' for x in str]
# print(op)


#create a list of numbers from 1 to 10 using comprehensions
#[1,2,3,4,5,6,7,8,9,10]

# op=[expression iteration filteration(optional)]

# op=[x**2 for x in range(1,11)]
# print(op)

#create list of even numbers from 1 to 10 usnng list comprehensions

# op=[x for x in range(1,11) if x%2==0]
# print(op)

# #if filteration is there
# then-->1.iteration
#        2.filteration
#        3.operation

# #if no filteration
# -->1.iteration 
# -->2.operation
# ip=[1,4,7,9,11,13,24,56,108,234,125]

#create a new list from given list with multiplying 2 for every even numbers

# op=[x*2 for x in ip if x%2==0]
# print(op)

# def factorial(num):
#     // logic for factorial
#     return value

# op=[factorial(x) for x in range(1,6)]

