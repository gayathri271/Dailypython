# Find the First and Second Largest Element in an Array
#       [3, 1, 4, 1, 5, 9]   → 9
#       [3, 1, 4, 1, 5, 9]  → 5

num=[int(i) for i in input().split(",")]  
print(num)
if len(num)<2:
    print("none")
else:
    first,second=float("-inf"),float("-inf")
    for n in num:
        if n >first:
            second=first  
            first=n  
        elif n>second and n!=first:
            second=n
print("first number:",first)    
print("Second number:",second)

#method-2

num=[int(i) for i in input().split(",")]  
num.sort()
print(num)
num.reverse()
print(num[0])
print(num[1])


# Rotate an Array
#       [1, 2, 3, 4, 5], 2  → [4, 5, 1, 2, 3]

numbers=input().split(",")
k=int(input())
for i in range(k):
    last=numbers[-1]
    for j in range(len(numbers)-1,0,-1):
        numbers[j]=numbers[j-1]
    numbers[0]=last    
print(*numbers)    #* is for unpacking  as'2' -> 2

#method-2

numbers=input().split(",")
print (numbers)
k=int(input())%len(numbers) 
# print(numbers[-k:])
# print(numbers[:-k])
numbers=numbers[-k:]+numbers[:-k]
print(*numbers)


# Intersection of Two Arrays
#       [1, 2, 3], [2, 3, 4]  → [2,3]

arr1=input().split(",")
arr2=input().split(",")
print(arr1)
print(arr2)
res=[]
for i in arr1:
    if i in arr2:
        res.append(i)
print(res)    



rows=int(input("Enter:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    

# Enter:5
# * 
# * * 
# * * * 
# * * * * 
# * * * * *  


rows=int(input("Enter:"))
for i in range(1,rows+1):
    spaces=rows-i
    print(" "*spaces,end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()    

#     Enter:5
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 

# Find Missing Number
#        [1, 2, 4, 5]   → [3]
# Given an array of consecutive numbers with one missing, find the missing number.

arr1=[int(i) for i in input().split(",")]    #[1,2,3,5,6]
n=len(arr1)+1 #6
expectedSum= n*(n+1)//2 #6(7) 42/2 21
actualSum=sum(arr1)  #17
res=expectedSum-actualSum  #4
print(res)


1,2,3,4,6
5
