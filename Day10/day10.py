# Find the First Duplicate
#        [2, 1, 3, 5, 3, 2] → 3
# Write a function to return the first duplicate value in an array.



arr1=[int(i) for i in input().split()]
temp=[]
dup=" "
for i in arr1:
    if i not in temp:
        temp.append(i)
print(temp)       
for j in temp:
    if arr1.count(j)>1:
        dup+=str(j)+" "
        break  #to return first duplicate
print(dup)        
        
#length of highest string in array


arr1=input("Enter:").split(",")
print(arr1)
maxi=len(arr1[0])
for i in range(1,len(arr1)):
    if len(arr1[i])>maxi:
        print(arr1[i])
        maxi=len(arr1[i])
print(maxi)            

#method-2
arr=input("enter: ").split(",")
max_len=len(arr[0])
for i in arr:
    if len(i)>max_len:
        max_len=len(i)
print(max_len)
        
#method-3
arr=input("enter:").split(",")
print(arr)
max_len=0
dic=""
for i in arr:
    if len(i) >max_len:
        dic=len(i)
print(dic)


# output:

# Enter:apple,banana,cherry,grapes
# ['apple', 'banana', 'cherry', 'grapes']
# banana
# 6

arr1=input("Enter:").split(",")
arr2=[]
max1=[]
for i in arr1:
    if len(i)>0:
        arr2+=str(i).split(",")
print(arr2)
max2=arr2[0]
for j in range(1,len(arr2)):
    if len(arr2[j])==len(max2) or len(arr2[j])>len(max2):  #banana>apple
        max2=arr2[j]
        max1+=max2.split(",")
print(max1)      

# Enter:apple,banana,orange,cherry
# ['apple', 'banana', 'orange', 'cherry']
# ['banana', 'orange', 'cherry']


# Flatten a Nested Array
#        [1, [2, [3, [4]], 5]] → [1, 2, 3, 4, 5]
# Write a function to flatten a nested array into a single array.


arr1=[[1, [2, 3]], [4, [5, 6]], 7] 
arr2=[]
for i in arr1:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for k in j:
                    arr2+=[k]
            else:
                arr2+=[j]
    else:
        arr2+=[i]
print(arr2)   

#using functions

def flated_array(arr1):
    arr2=[]
    for i in arr1:
        if isinstance(i,list):
            arr2.extend(flated_array(i))
        else:
            arr2+=[i]
    return arr2

arr1=[1,[2,3]],[4,[5,6],7]   
print(flated_array(arr1))