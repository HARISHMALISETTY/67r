#print("iam a sample")

# 1.normal statements
# 2.control statements
#2.1 conditional
    # 1.simple -if 
    # 2.if-else 
    # 3.nested-if 
    # 4.elif
#2.2 looping statements

# is_got_placement=False 

# if(is_got_placement):
#     print("he can go the job")
# else:
#     print("he should join in institue")


# is_got_placement=True
# is_rich=False
# is_skilled=False
# if(is_got_placement and is_rich and is_skilled):
#     print("go and get marriage")
# elif(is_got_placement):
#     print("go and join the job")
# elif(is_rich):
#     print("u can start ur own startup")
# elif(is_skilled):
#     print("u can do freelancing")
# else:
#     print("go and join any institute")


FrontEnd=False
BackEnd=False
DataBase=False

if(FrontEnd and BackEnd and DataBase):
    print("fullstack developer")
elif(FrontEnd):
    if(BackEnd):
        print("go and learn database to become fullstack dev")
    else:
        print("go and learn Backend to become fullstack dev")
elif(BackEnd):
    if(DataBase):
        print("go and learn frontend to become fullstack dev")
    else:
        print("go and learn both F.E and Databse to become fullstack dev")
elif(DataBase):
    print("go and learn F.E AND B.E to become fullstack dev")
else:
    print("go and join in 10000coders")

