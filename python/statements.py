# print("statement1")
# print("statement2")
# print("statement3")

# conditional statements:
# statements which executes based on condition.
# depends on the condition 
# used for decision making

# 1.simple-if
# 2.if-else 
# 3.elif 
# 4.nested-if

# if (condition):
#     statement1
#     statement2
#     statement3

# if not True:
#     print("statement1")
#     print("statement2")
# print("statement3")
# money=550
# ticket_cost_war2=295
# ticket_cost_koolie=395
# ticket_cost_kingdom=200

# if money>ticket_cost_war2:
#     print("will go to war2 movie")
# if money>ticket_cost_koolie:
#     print("will go to koolie movie")
# if money>ticket_cost_kingdom:
#     print("will go to kingdom movie")

#if we want to execute something else when condition is fail, then we can use else.

# if condition:
#     statement
# else:
#     statement 

#if executes whenever condition is satisfied or true, else will executes automatically
#when condition fails in if statement.
#no need to give condition in else


# def sample(money,ticket_cost,user):
#     if(money>ticket_cost):
#         print(f"{user} can watch the movie in theatre")
#     else:
#         print(f"{user} should scroll instagram")

# sample(250,295,'kiran')
# sample(300,295,'naresh')
# sample(245,295,'lakshmi')


# def decideFuture(eamcet_result,student):
#     if(eamcet_result):
#         print(f"{student} can join in engineering college")
#     else:
#         print(f"{student} can join in degree college")

# decideFuture(True,'kiran')
# decideFuture(False,'Naresh')
# decideFuture(True,'lakshmi')

# def checkEvenOrOdd(num):
#     # if num%2==0:
#     if num & 1==0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
# checkEvenOrOdd(2125478901)

# 1254789
# "02468"


# num=1547890
# ld=num%10
# if ld in (0,2,4,6,8):
#     print('num is even')
# else:
#     print('num is odd')

#whenever u have multiple conditions/options then we can use elif
# if cond1 fail then check cond2, if cond2 also fail then check cond3...
# if all conditions fail then by default else block will executes.
# if condition:
#     #st1 
# elif cnd2:
#     #st2
# elif cnd3:
#     #st3
# else:
#     #ds
# def college(eamcet_rank):
#     if (eamcet_rank<25000):
#         print("got seat in jntuh")
#     elif(eamcet_rank<50000):
#         print("got seat in mallareddy")
#     elif(eamcet_rank<75000):
#         print("got seat in sri indhu eng college")
#     else:
#         print("join in degree college")
# college(16500)


# terinary

# nested-if :
# if inside another if
# won_last_match=True
# total_matches_won=4
# net_run_rate=0.78

# if(won_last_match or total_matches_won>=6):
#     if(total_matches_won>=5):
#         if(net_run_rate>=0.75):
#             print("team is entered into playoffs")
#         else:
#             print("team is disqualified due to low run rate")
#     else:
#         print("team should win more than 6 matches atleast to go to playoffs")
# else:
#     print("team lost in the current match, so not qualified")

#terinary operator:
#it is also known as conditional operator
#it is used to write if-else in shorthand form in single line
#with this we can assign the values to a variable conditionally.
#we will use this only for simple and short requirement purpose only.
#syntax---> True statement if True else False statement

# print("true statement") if not True else print("false statement") 

# username_matched=False
# password_matched=True  
# print("login success") if username_matched and password_matched else print("login failed")
# print("login success") if username_matched and password_matched else print("login failed due to incorrect username") if not username_matched and password_matched else print("login failed due to incorrent password")


# age=5
# person="adult" if age>=18 else "minor"
# print(person)


login_as="owner"
user="customer" if login_as=='customer'else 'owner'
print(user)

locality='local'
shippingcost=5 if locality=='local' else 10
print(shippingcost)

marks=96
grade='A' if marks>=95 else 'B'
print(grade)