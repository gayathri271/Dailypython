# ArmStrong Number

num=input("enter:") #371
temp=int(num)
sum,digit=0,0
length=len(str(num))
for i in range(0,length):
    digit=temp%10 #1
    temp=temp//10 #37
    sum+=pow(digit,length) 
print(sum)    
if sum==int(num):
    print("armstrong")
else:
    print("not")




# Armstrong number in a given range
num=int(input("Enter:")) #200
for i in range(1,num+1):
    sum,digit=0,0
    temp=i  
    length=len(str(i))
    while temp>0:
        digit=temp%10
        temp=temp//10
        sum+=pow(digit,length)
    if sum==i:
        print(i,end=' ')

# output:
# Enter:200
# 1 2 3 4 5 6 7 8 9 153         


# Fibonacci Series upto nth term

num=int(input("Enter:"))
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b
print()    

# output:
# Enter:10
# 0 1 1 2 3 5 8 13 21 34 

# Factorial of a number

num=int(input("Enter:"))
fact=1
if num<0:
    print("Not possible")
else:
    for i in range(1,num+1):
        fact=fact*i
print(fact)    

# output:   
# Enter:6
# 720

# Power of a number

num=int(input("Enter")) #3
pow=int(input("Enter"))
value=1
for i in range(pow):
    value*=num
print(value)    

# output:
# Enter:3
# Enter:2
# 9

# Strong number

num=input("enter:") #145
res=0
for i in num: #1 4 5
    x=int(i) 
    fact=1
    for j in range(1,x+1):
        fact=fact*j #1 2 6 24 120
    res+=fact     #1+24+120
result="yes" if res==int(num) else "no"
print(result)

# output:
# enter:145
# yes