# Reverse a String
#       "hello" → "olleh"
# Write a function to reverse a given string.


str1=input("Enter:")
rev=str1[::-1]
print(rev)


str1=input("Enter:")
rev=""
for char in str1:
    rev=char+rev
    print(rev)
print(rev)

# Enter:hello
# h
# eh
# leh
# lleh
# olleh
# olleh

#method-2

str1=input("Enter:")
print("".join(reversed(str1)))


# Check if a String is a Palindrome
#       "racecar"  → true 
# Write a function to check if a given string is a palindrome.


str1=input("Enter:")
rev=""
for char in str1:
    rev=char+rev
    # print(rev)
print(rev)
if rev==str1:
    print("true")
else:
    print("not a palindrome")


# Count Vowels in a String
#        "hello world" → 3
# Write a function to count the number of vowels in a given string.

str1=input("Enter:")
vowels="aeiouAEIOU"
count=0
for char in str1:
    if char in vowels:
        count+=1
print(count)   


# Remove Vowels from a String
#        "hello world" → "hll wrld"
# Write a function to remove all vowels from a given string.

str1=input("Enter:")
vowels="aeiouAEIOU"
res=""
for char in str1:
    if char not in vowels:
        res+=char
print(res) 


# Convert String to Title Case
#        "hello world" → "Hello World"
# Write a function that converts a string to title case (capitalize the first letter of each word).

str1=input("Enter:").split()
cap=[word[0].upper()+word[1:] for word in str1]
print(" ".join(cap))

#method-2

str1=input("Enter:")
print(str1.title())


# Convert String to Number
#        "123" → 123
# Write a function to convert a string to a number (without using parseInt or Number).


str1=input("Enter:")
num=0
for char in str1:
    num=num*10+(ord(char)-ord('0'))  # Converting character to number  ord('0')=48  ord(1)=51
print(num,type(num))    

str1=input("Enter:")
num1=int(str1)
print(num1)


# Check if String Contains Only Digits
#       "12345" → true 
# Write a function to check if a string contains only numeric digits.

str1=input("Enter:")
num=True
for char in str1:
    if char<'0' or char>'9':
        num=False
        break
print(num)


# Count Occurrences of a Character
#        "hello world", "l" → 3
# Write a function that counts the occurrences of a specific character in a string.

str1=input("Enter:")
count={}
for char in str1:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
for char in count:
    if count[char]>1:
        print(f"'{char}'occurs {count[char]} times")


# Enter:hello world
# 'l'occurs 3 times
# 'o'occurs 2 times
