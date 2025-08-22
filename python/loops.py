#looping statement:
#set of statements will executes multiple times in a loop until a specific condition
#reach.

#to start this execution and end this execution we have to use
#starting value and ending value. this can be achieve with help of
#predefined method range().

#range() will contains starting value(optional), ending value and stepper(optional).

#for loop
#while loop

# for loop:
# for x in range():
#     #stat1
#     #stat2
#     #stat3

# for x in range(1,10,3):
    # print("hello world")
    # print(x)

# 2x1=2
# 2x2=4
# 2x3=6
# .
# .
# .
# 2x10=20

# for x in range(1,11):
#     print(f"2x{x}={2*x}")

# print num from 20 to 50

# for i in range(20,51):
#     if(i%3==0):
#        print(i)

 #print num from 10 to 40
 # if num is divisible by 3 then print num-fizz
 # if num is divisible by 5 then print num-buzz
 # if num is divisible by both then print num-fizzbuzz      

# for y in range(10,41):
#     if(y%3==0 and y%5==0):
#         print(f"{y}-fizz buzz") 
#     elif(y%5==0):
#         print(f"{y}-buzz")
#     elif(y%3==0):
#         print(f"{y}-fizz") 

        # 1 to 10
        # 10 to 1
# for x in range(10,0,-1):
#     print(x)


# str="fullstack"
# for x in str:
#     print(x)

# li=['hi','hello','some','thing']
# for x in li:
#     print(x)

# str="something"

#s-hi
#o-hi
#m-hi
# .
# .
# .
# g-hi

# for x in str:
#     print(f"{x}-hi")

# str="something"

# for x in range(0,len(str),2):
#     print(str[x])

#1st-->x=0
#2nd--->x=1

# range-->single arg--->ending value 
# range--->two args--->start and end 
# range---->3 args--->start,end and stepper

# str="something"
# for x in range(len(str)-1,-1,-1):
#     print(str[x])

#hello
#olleh

ip="hello"
#how to print
# o 
# l 
# l 
# e 
# h

#olleh
op=""
for x in range(len(ip)-1,-1,-1):
    op+=ip[x]
    print(op)

#print numbers from 100 to 0 in reverse which are divisible by 5 
#check whether given string is a palindrome or  not using a function
#wirte a function to print tables in reverse
# # for eg: 3x10=30
#           3x9=27
#           3x8=24    

