# Question 1: Toggle Case Order
# Problem:
#  Given a string, transform it such that:
# Convert all lowercase letters to uppercase.
# Convert all uppercase letters to lowercase.
# Maintain the order of the characters.

# Example:
# Input: "aaazaAx"
# Output: "AAAZaX"

s="aaxxZC"
res=""
for char in s :
    if char.islower():
        res+=char.upper()
    elif char.isupper():
        res+=char.lower()
    else:
        res+=char
print(res)   


s="aaaZZZ"
res=""
for char in s:
    if char>='a' and char<='z': # Check if it's a lowercase letter
        res+=chr(ord(char)-32)   # Convert to uppercase
    elif char>='A' and char<='Z':  # Check if it's an uppercase letter
        res+=chr(ord(char)+32) # Convert to lowercase
    else:
        res+=char # Keep other characters unchanged
print(res)     


#  Given a string containing a mix of lowercase and uppercase letters, transform it so that:
# All uppercase letters come first.
# All lowercase letters follow them.
# Maintain their original order within their groups.

# Example:

# Input: "aaZaAx"
# Output: "ZAaaax"

s="aaZZxx"
upper=""
lower=""
res=""
for char in s:
    if char>='A' and char<='Z':
        upper+=char
    elif char>='a' and char<='z':
        lower+=char
res+=upper+lower
print(res)


# "Hello world" ->  hello worlD
# convert first characters and  last characters into alternative case
# test 1 : mApadD   => MApadd
# test2 : Sharath  => sharatH
# status - not solved


s="Hello world"
res=""
for i in range(len(s)): #indexes
    char=s[i] #value in that index
    if i==0 or i==len(s)-1:   
        if char>='a' and char<='z':
            res+=chr(ord(char)-32)
        elif char>='A' and char<='Z':
            res+=chr(ord(char)+32)
    else:
        res+=char
print(res)

#if we want 2 letters from start and 2 from end the (if i==0 or i==1 or i==(len(s)-1) or i==(len(s)-2):)


# find second lowest values from array
# input = [1, 2, 4, -1, -1, -2, -2]
# output = [-1, -1]
# status- not solved find lowest  value from sorting but not return expected value

arr1=[int(i) for i in input("Enter:").split(",")] #[1,2,3,-1,-1,-2,-2]
res=[]
first,second=float("inf"),float("inf")
for n in arr1:
    if n<first:
        second,first=first,n  
    elif n>first and n<second:
        second=n
for n in arr1:
    if n==second:
        res+=[n]
print(res)

# Convert String to Camel Case
# Input:
# toCamelCase("hello world this is javascript");
# Output:
# "helloWorldThisIsJavascript"

str1=input("Enter:")
str2=str1.split()
print(str2)
cap=str2[0]
for word in str2[1:]:
    cap+=word[0].upper()+word[1:]
print(cap)   ## "helloWorldThisIsJavascript"

#method-2

str1=input("Enter:")
str2=str1.split()
cap=''
for word in str2:
    cap+=word[0].upper()+word[1:]
print(cap)  #HelloWorldThisIsJavascript

# Find First Non-Repeating Character

s1=input("Enter:")  #swiss
count={} #s:2 w:1 i:1 
for char in s1:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
for char in s1:
    if count[char]==1:
        print("first non repeating is",char)
        break

# output:
# Enter:swiss
# first non repeating is w




 