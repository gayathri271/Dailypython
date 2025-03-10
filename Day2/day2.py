# Find odd sum


num=input()
sum=0
for i in num:
    if int(i)%2!=0:
        sum=sum+int(i)
print(sum)

# Output:
# 6543
# 8

# diff b/w evenSum & oddSum

num=input("Enter:")#76321
evenSum=0
oddSum=0
for i in num:
    if int(i)%2==0:
        evenSum+=int(i)
    else:
        oddSum+=int(i)
print("Sum of Even:",evenSum)    
print("Sum of Odd:",oddSum)
print("Difference is:",evenSum-oddSum)

#output:
# Enter:76321
# Sum of Even: 8
# Sum of Odd: 11
# Difference is: -3


#Sum of even positions

n=[int(i) for i in input().split()]
sum=0
for i in range (1,len(n)+1):
    if i%2==0:
        sum+=n[i-1]
print("sum of even positions:",sum)   

#Output:
# 10 20 30 40 50
# sum of even positions: 60


# difference between sum of even position digits, difference between odd position digits.

n=[int(i) for i in input().split()]
sumEven=0
sumOdd=0
for i in range(1,len(n)+1):
    if i%2==0:
        sumEven+=n[i-1]
    else:
        sumOdd+=n[i-1]
print("Sum of Even positions:",sumEven)     
print("Sum of Odd positions:",sumOdd)
print("diff is:",sumEven-sumOdd)

# output:
# 2 4 6 8  4 2
# Sum of Even positions: 14
# Sum of Odd positions: 12
# diff is: 2

