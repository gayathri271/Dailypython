# Program for prime

num=int(input())
if num<2:
    print("not")
for i in range(2,(num//2)+1):
    if num%i==0:
        print("not")
        break
else:
    print("prime")



#  Program to print the primes in the range(1,50)

sum=0
for i in range (1,51):  
    if i<2:
        continue
    count=True #2
    for j in range(2,int(i**0.5)+1): 
        if i%j ==0:
            count=False
            break
    if count==True:
        print(i)
        sum+=i
print(sum) 

# Output:
# Enter:50
# 2 # 3 # 5 # 7# 11 # 13 # 17 # 19 # 23 # 29 # 31 # 37 # 41 # 43 # 47 # 328

# sum of all prime numbers that ends with 7 in the range(1,50).

num=int(input("Enter:"))
sum=0
for i in range(1,num+1):
    if i<2:
        continue
    count=True
    for j in range(2,int(i//2)+1):
        if i%j==0:
            count=False
            break
    if count==True and i%10==7:
        print(i)
        sum+=i
print(sum)  

# Output:
# Enter:50
# 7# 17# 37# 4# 108


# reverse of all the  numbers in the range(1,50).

num=input("Enter:")
for i in range(1,int(num)+1):
    rev=int(str(i)[::-1])
    print(i,rev)

# output
# Enter:20
# 1 1# 2 2# 3 3# 4 4# 5 5# 6 6# 7 7# 8 8# 9 9# 10 1# 11 11# 12 21# 13 31# 14 41# 15 51# 16 61# 17 71# 18 81# 19 91# 20 2
    
# reverse of prime numbers in the range(1,50).  

num=input("Enter:")
sum=0
for i in range(1,int(num)+1):
    if i<2:
        continue
    count=True
    for j in range(2,int(i//2)+1):
        if i%j==0:
            count=False
            break
    if count==True:
        rev=int(str(i)[::-1])
        print(i,rev)
        sum+=rev
print(sum)  

# output
# Enter:50
# 2 2# 3 3# 5 5# 7 7# 11 11# 13 31# 17 71# 19 91# 23 32# 29 92# 31 13# 37 73# 41 14# 43 34# 47 74
# 553

#  print the sum of individual digits in a number in the range(1,50)
for num in range(1,51):
    sum1=sum(int(digit) for digit in str(num))
    print(sum1) 

# method-2
for i in range(1,51):
    sumdigit=0
    temp=i 
    while temp >0:
        # digit=temp %10
        # sumdigit+=digit
        sumdigit+=temp%10 #combination of above to lines 2
        temp//=10
    print(sumdigit)


# check whether the sum of individual digits is a prime number or not in the range(1,50)

sum=0
for i in range(1,51): 
    temp=i
    sumdigits=0
    while temp>0:
        sumdigits+=temp%10
        temp//=10
        sum+=sumdigits
    if sumdigits<2:
        continue
    count=True
    for j in range(2,int(sumdigits//2)+1):
        if sumdigits%j==0:
            count=False
            break
    print(sumdigits,count,end=" ")   
print(sum)    

# output:
# 2 True 3 True 4 False 5 True 6 False 7 True 8 False 9 False 2 True 3 True 4 False 5 True 6 False 7 True 8 False 9 False 10 False 2 True 3 True 4 False 5 True 6 False 7 True 8 False 9 False 10 False 11 True 3 True 4 False 5 True 6 False 7 True 8 False 9 False 10 False 11 True 12 False 4 False 5 True 6 False 7 True 8 False 9 False 10 False 11 True 12 False 13 True 5 True 510

    


