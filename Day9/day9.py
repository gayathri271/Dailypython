# Convert Array to Object
#       [["name", "Alice"], ["age", 25]] → {name: "Alice", age: 25}
# Write a function that converts an array of key-value pairs into an object.


obj1=input("Enter:")
obj2=input("Enter:")
key1,value1=eval(obj1) #converts or evaluates string to obj
key2,value2=eval(obj2)
final={key1:value1,key2:value2}
print(final)

#method-2

arr=[["name","Alice"],["age",25]]
obj1={}
for pair in arr:
    key=pair[0]
    value=pair[1]
    obj1[key]=value
print(obj1)    

# Merge Two Objects
#       {a: 1, b: 2}, {b: 3, c: 4} → {a: 1, b: 3, c: 4}
# Write a function that merges two objects, giving priority to the properties of the second object in case of conflict.

obj1={"a": 1, "b": 2}
obj2={"b":3, "c":4}
merged={}
for key in obj1:
    merged[key]=obj1[key]
for key in obj2:
    merged[key]=obj2[key]
print(merged)    


obj1=input("enter:")
obj2=input("enter:")
obj1,obj2=eval(obj1),eval(obj2)
res=obj1.copy()
res.update(obj2)
print(res)

# Count Object Properties
#        {a: 1, b: 2, c: 3} → 3 
# Write a function that returns the number of properties in an object.


obj1={"a": 1, "b": 2, "c":3}
count=0
for key in obj1:
    count+=1
print(count)    

# Get Object Keys
#       {a: 1, b: 2, c: 3} → ["a", "b", "c"]
# Write a function that returns an array of all the keys in an object.

obj1={"a": 1, "b": 2, "c":3}
obj2=[] 
for key in obj1:
    obj2+=[key]
    # obj2.append(key)
print(obj2)    

# Get Object Values
#       {a: 1, b: 2, c: 3} → [1, 2, 3]
# Write a function that returns an array of all the values in an object.


obj1={"a": 1, "b": 2, "c": 3}
values=[]
for key in obj1:
    values+=[obj1[key]]
print(values)   

# Check if Object is Empty
#         {} → true 
# Write a function to check if an object is empty (i.e., has no properties).

obj1={}
is_empty=True
for key in obj1:
    is_empty=False
    break
print(is_empty)


arr=[int(i) for i in input().split()]
res=[]
def co(k):
    cou=0
    for j in arr:
        if j==k:
            cou+=1
    return cou
for i  in arr:
    if i not in res and co(i)==1:
        res+=[i]
print(res)




