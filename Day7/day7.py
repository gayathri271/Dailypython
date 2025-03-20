
# Find the Maximum Product of Two Elements
#        [3, 5, -2, 8, 11] → 8*11 →88
# Write a function to find the maximum product of two elements in an array.


num=[int(i) for i in input().split(",")]  
print(num)
first,second=float("-inf"),float("-inf")
for n in num:
    if n >first:
        second=first  
        first=n  
    elif n>second and n!=first:
        second=n
print(first*second)    



# Move Zeros to End
#        [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
# Write a function that moves all zeros in an array to the end while maintaining the order of other elements.


arr=[int(i) for i in input().split()]
res=[]
for i in arr:
    if i!=0:
        res.append(i)
res=res+[0]*(len(arr)-len(res))  
print(res)


# Pair Sum
#        [2, 4, 3, 5, 7, 8, 9], 7 →  [[4, 3], [2, 5]]
# Write a function to find all pairs in an array whose sum is equal to a given target.


num=[int(i) for i in input().split()] #[2,3,4,6,7,8]
print(num)
tar=int(input())  #8  [2,6]
sum=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==tar:
            sum.append([num[i],num[j]])
print(sum)            

# SORTED arr

num=[int(i) for i in input().split(",")]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[j]<num[i]:
            num[i],num[j]=num[j],num[i]
print(num)    


# Find Peak Element
#        [1, 3, 20, 4, 1, 0] →  20
# Write a function to find a peak element in an array. An element is a peak if it is not smaller than its neighbours.

arr=[int(i) for i in input().split()]
peak=arr[0]
for i in range(1,len(arr)):
    if arr[i]>peak:
        peak = arr[i]
print(peak)