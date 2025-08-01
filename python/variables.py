# x=5
# y=10

# # rules to be follow while creating a variables
# # 1.variable name should not starts with number,@,$..except _ 
# # 2.variable name should not contain spaces
# # 3.should not use keywords as a variable names
# #4.case sensitive 
# # a=10
# # A=5
# # a,b,c=1,2,3

# #naming conventions
# # uppercase --->FIRSTNAME
# # lowercase --->firstname
# # camelcase--->firstName
# # pascalcase--->FirstName
# # snakecase--->first_name
# # kebabcase---->first-name

# # www.bookmyshow.com/show-times/movies

# # x=25
# # print(id(x))
# # y=2.5
# # print(id(y))
# # z='hello'
# # print(id(z))
# # id() is a predefined method to get the memory id/address of a value/object.

# # x=5
# # y='hello'
# # z=True
# # c=2.5

# # #primitive-->int,float,bool and string

# # #primitives are immutable

# # print(type(x))
# # print(type(y))
# # print(type(z))
# # print(type(c))


# # x=5
# # print(id(x))
# # x=20
# # print(id(x))
# # print(x)

# # x=['hi','hello',4,5]
# # print(id(x))

# # x[1]='welcome'
# # print(id(x))

# # str='welcome'

# # str[2]='x'

# x=5
# y=2.5
# z='hello world'
# # string:-group of characters enclosed in b/w '' or ""
# # len()- to find the length/size of the string
# # print(len(z)) #it will display only output

# #size of the given string is 5

# # print('len(z)')

# # print(f"size of the given string is {len(z)}")

# op="""Among the 155 passengers and 
# seven crew flying from Surabaya to 
# Singapore are three Koreans, one Malaysian,
# and one person variously reported as a French or
# UK national. The rest are Indonesians. 
# There are sixteen children and an infant. 
# The plane was diverting around weather formations 
# over the Java Sea when 
# contact with air traffic 
#     control (ATC) in Jakarta was lost."""
# # print(type(op))

# # x=input("please enter value : ")
# # print(f"user enetered value is {x}")
# # print(type(x))
# # int()-->changes from one type to int type 
# # float()--->changes from one type to float type 
# # str()-->chaanges from one type to string type.
# # a=125
# # b=str(a)
# # print(type(b))

# str1="hello world"

# # print(str1[6]) #positive indexing will go in left to right..starts from 0
# # print(str1[-3])  #negative indexing will go in right to left..starts from -1

# # num1=125
# # cnrt=str(num1)
# # print(cnrt[2])


# #list,tuples,sets,dictionaries.

# #[],(),{},{}

# # list1=["kiran","naresh",'123',True,12.5,[4,5,6]]
# # # print(len(list1))
# # # print(list1[5][2]+5)
# # print(type(list1[2]))

# tuple1=('b+ve','o-ve','o+ve','Mon',125,True,12.5,[4,5,6],('hi',9))
# # print(tuple1[4])
# # print(len(tuple1))
# # tuple1[3]='helloooo'

# # set1={3,4,5,3,4,6}
# # set1={'hii',"hello","hii","welcome","welcome"}
# # print(set1)

# # print(hash('helloo'))

# set1={'89','45','23','124',125}
# print(set1)
# #set will generates hashing values for string internally 
# #for every execution

# a=10
# b=5
# temp=a 
# a=b
# b=temp
# print(a,b)

# a,b=b,a 
# print(a,b)

# set and frozenset


# x={4,5,6} #using literals
# print(type(x))
# ip=set([1,2,3,"hi","hello"]) #it is the predefined method to build set
# print(ip)
# print(type(ip))
# #remove one element from set using remove()
# ip.remove('hi') #it will removes hi value from existing set
# print(ip)
# ip.add('python')
# print(ip)

ip=frozenset(['hi','hello',45])
print(ip)
# ip.remove('hi')
#frozensets are immutable