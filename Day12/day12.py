# Check for Anagrams
#   "listen", "silent"  → true

def is_anagram(s1,s2):
    fre_dict={}
    for i in s1:
        if i in fre_dict:
            fre_dict[i]+=1
        else:
            fre_dict[i]=1
    count=0
    for i in s2:
        if i in fre_dict:
            fre_dict[i]-=1
            if fre_dict[i]==0:
                count+=1
            else:
                return False
    return count==len(fre_dict)
print(is_anagram("silent","listen"))

# Check if a String is a Rotation of Another String
#       "abcde", "cdeab" → true

s1="abcde"
s2="cdeab"
result=False
if len(s1)!=len(s2):
    result=False
else:
    for i in range(len(s1)-1):
        if s1[i]==s2[0]:
            rotate=s1[i:]+s1[:i]
            if rotate==s2:
                result=True
                break
print(result)    

#with functions

def rotate(s1,s2):
    result=False
    if len(s1)!=len(s2):
        result=False
    else:
        for i in range(len(s1)-1):
            if s1[i]==s2[0]:
                rotate=s1[i:]+s1[:i]
                if rotate==s2:
                    result=True
                    break
        return result
print(rotate("abcde","cdeab"))    



#anagram 

s1=[i for i in input("enter1: ")]
s2=[i for i in input("enter2: ")]

def sort(x):
    for i in range(len(s1)):
        for j in range(i+1,len(s1)):
            if s1[i] >s1[j]:
                s1[i],s1[j]=s1[j],s1[i]
    return x
print(sort(s1))
def join(s1):
    res=""
    for i in s1:
        res+=i
    return res
print(join(s1)) #ate

def isanagram(s1,s2):
    if len(s1)==len(s2):
        s2=join(sort(s2))
        s1=join(sort(s1))
        if s2==s1:
            return True
        else:
            return False
    return False

print(isanagram(s1,s2))


x=[10,9,2,5,3,7,101,18]   

def longest(a1):
    a2=[]
    for i in range(len(a1)):
        count=1
        max1=a1[i] #10
        for j in range(i+1,len(a1)):
            if a1[j]>max1:
                count+=1
                max1=a1[j]
        a2+=[count]   
    return a2
print(longest(x))  


x=[10, 9, 2, 5, 3, 7, 101, 18] 
def longest(a1):
    a2=[]
    a3=[]
    for i in range(len(a1)):
        temp=[a1[i]]
        count=1
        max1=a1[i]
        for j in range(i+1,len(a1)):
            if a1[j]>max1:
                temp+=[a1[j]]
                count+=1
                max1=a1[j]
        a2+=[temp] 
        a3+=[count]
    max2=a2[0] 
    for i in range(1,len(a2)):
        if len(a2[i])>len(max2):
            max2=a2[i]
    return [a2,a3,max2]
print("all increasing subsequences in the array:",longest(x)[0])  
print("length of subsequence:",longest(x)[1]) 
print("longest increasing subsequence:",longest(x)[2])  