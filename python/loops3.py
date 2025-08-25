# 1.12540
# 0
# 4
# 5
# 2
# 1

# num=12540
# while(num>0):
#     ld=num%10
#     print(ld)
#     num=num//10




# ld=7
# rev=7

# ld=4

# 1, 5

# 15

# 1x10-->10+5--->15

# 15 8
# 15x10--->150+8=158

# ip=12521
# ip1=ip
# rev=0
# while(ip>0):
#     ld=ip%10
#     rev=rev*10+ld
#     ip=ip//10 #1252 #125 #0
# print(rev)

# if(ip1==rev):
#     print("given num is palindrome")
# else:
#     print("given num is not a palindrome")


# ip=12521
# sum=0
# while(ip>0):   
#     sum+=ip%10
#     ip=ip//10 #1252 #125 #0
# print(sum)

#find the length of given num without cnverting into string

# ip=12345
# count=0
# while(ip>0):
#     count +=1
#     ip //= 10
    
# print(count)

#count only odd num in given ip
# ip=12589
# count=0
# while(ip>0):
#     ld=ip%10
#     if(ld%2!=0):
#         count +=1
#     ip //= 10
# print(count)

#sum of only even num in given ip

# num=6
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)


num=153
num1=num
num2=num
count=0
sum=0
while(num>0):
	count+=1
	num=num//10
print(count)
print(num)

while(num1):
	sum=sum+(num1%10)**count
	num1=num1//10
print(num1)

if(num2==sum):
	print("it is a armstrong")
else:
	print("it is not a armstrong ")

# while(num1>0):
# 	sum=sum+(num%10)**count
# 	sum=0+(153%10)**3
# 	sum=0+3**3
# 	sum=27	
	
#     num1=num1//10
#     sum=sum+(num1%10)**count
#     sum=27+(15%10)**3
#     sum=27+5**3
#     sum=152

#     num=num//10
#     sum=sum+(num%10)**count
#     sum=152+(1%10)**3
#     sum=152+1
#     sum=153

# if(sum==num2):
# 	print("armstrong")
# else:
# 	"not"


#check whether 

# 152
# 151 and 153 are armstrongs or not?


