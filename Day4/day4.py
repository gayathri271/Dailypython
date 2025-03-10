# print the sum of all prime digits in a number

num=input("Enter:") 
sum=0
for i in num:
    x=int(i)
    if x>1:
        div=0
        for j in range(2,(x//2)+1):
            if x%j==0:
                div+=1
                break
        if div==0:
            sum+=x
print(sum)

# input: 46732
# output: 12


# print the prime digits in a number in asc order

num=input("Enter:")   #46732
primdigits=" "
for i in num:
    # x=int(i)
    div=0
    for j in range(2,(int(i)//2)+1):
        if int(i)%j==0:
            div+=1
            break
    if div==0:
        primdigits+=i
sorted_primdigits = "".join(sorted(primdigits))   #for ascending
dec=sorted_primdigits[::-1]  #for decending
print(sorted_primdigits)
print(dec)

# output: 237
#output:732

# Method-2

num=input("Enter:")   #46732
primdigits=[]
for i in num:
    # x=int(i)
    div=0
    for j in range(2,(int(i)//2)+1):
        if int(i)%j==0:
            div+=1
            break
    if div==0:
        primdigits+=i
        primdigits.sort()
# sorted_primdigits = "".join(sorted(primdigits)) 
des=primdigits[::-1]
print(des[0])

#  find the largest digit in the given number

# method-1

num=input()
dec=sorted(num)[::-1]
print(dec[0])

# method-2

num=input()
max1=num[0]
for i in range(1,len(num)):
    if num[i]>max1[0]:
        max1=num[i]
print(max1)        

# print the sum of largest number and smallest number in an array.

num=[int(i) for i in input().split(",")]
print(num)
max1=num[0]
for i in range(1,len(num)):
    if num[i]>max1:
        max1=num[i]
print(max1)     