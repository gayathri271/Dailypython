#   Given sring rebels divided into two parts, reb and els. 
# In both parts vowels count is same that is 1(e is presented in both the parts) so it returns true.


def vowels(s):
    res = list(s)
    a = res[:len(res)//2]
    b = res[len(res)//2:]
    print(a, b)

    vowels = "aeiouAEIOU"
    for v in vowels:
        if v in a and v in b:
            return True  
    return False 
s1="rebels"    
print(vowels(s1))    