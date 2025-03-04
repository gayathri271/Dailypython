# print sorted array 

# 1)Method-1

num=input().split() #1 2 3 5 2 4
print(num)
for i in range(len(num)-1):
    if num[i] > num[i+1]:
        print("not sorted")
        break
else:
    print("sorted")

# Output:

# 1 2 3 5 2 4
# ['1', '2', '3', '5', '2', '4']
# not sorted

# 2)Method -2

num1=[3,5,6,8,9]
sort=sorted(num1)
if num1== sort:
    print("sorted")
else:
    print("not sorted")    

# output
#sorted    


# Reverse of array

# method-1

n=input().split()
n.reverse()
print(n)

# method-2

n=input().split()
num=n[::-1]
print(num)

#output
# 2  4 7 9 4 0 7 
# ['7', '0', '4', '9', '7', '4', '2']


# "Removing Duplicates from List"

num=input().split()  # 1 6 8 9 2 5 3 3 6
print(num)
temp=[]
for i in num:
    if i not in temp:
        temp.append(i)
print(temp)        

# output
#  1 6 2 9 3 6 3 9 2
# ['1', '6', '2', '9', '3', '6', '3', '9', '2']
# ['1', '6', '2', '9', '3']


#print unique and duplicate values

numbers=input().split()
print(numbers)
uni=dup=""
temp=[]
for i in numbers:
    if i not in temp:
        temp.append(i)
print(temp)        
for num in temp:
    if numbers.count(num)>1:
        uni+=num+" "
    else:
        dup+=num+" "    
print("unique values:",uni)     
print("duplicate value:",dup)   

#output:
# 1 3 4 6 2 3 4 1
# ['1', '3', '4', '6', '2', '3', '4', '1']
# ['1', '3', '4', '6', '2']
# unique values: 1 3 4 
# duplicate value: 6 2 


# sum of even:

num=input().split()
sum=0
for i in num:
    if int(i)%2==0:
        sum+=int(i)
print("sum of even numbers:",sum)

#output:
# 1 2 3 5 2 6 
# sum of even numbers: 10


#sum of all numbers

num=input().split()
sum=0
for i in num:
    sum+=int(i)
print(sum)    

#output:
# 1 3 5 7 4
# 20

#Swap two numbers:

# method-1

num1=int(input("enter a number:")) #7
num2=int(input("enter a number:")) #6
temp=num1
num1=num2
num2=temp
print(num1,num2)

#output:
# enter a number:6
# enter a number:7
# 7 6

# method-2
num1=int(input("enter a number:")) #7
num2=int(input("enter a number:")) #6
num1,num2=num2,num1
print(num1,num2)


#Fibonacci numbers

num=int(input("enter a no.of series:"))
a,b=0,1
i=1
while i<=num:
    print(a,end=" ")
    c=a+b
    a,b=b,c
    i+=1

#output:
# enter a no.of series:5
# 0 1 1 2 3     




