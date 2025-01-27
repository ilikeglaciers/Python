#!/usr/bin/env python
# coding: utf-8

# In[1]:


#bool function
a=10
b=20
c=30

print(bool(""))
print(bool("string"))

print(bool(12))
print(bool(0))

print(bool({}))
print(bool({a,b,c}))

print(bool([]))
print(bool([a,b,c]))


# In[2]:


#operators
#exponent
print(9**2)

#floor division
print(100//3)


# In[17]:


#list operations
l1 = ["one","two","two"]
l2 = [1,2,3,4,5,6,7,8,9,10]
l3 = [True,False]
l4 = [1,"random"]

#list constructor with two round brackets
l5 = list(("new","list","consructor"))

print(l4)
print(l1[0],l1[1])
print(l1)
print(len(l1))
print(l5[-1])
print(l2[2:5])

if 'one' in l1:
    print("Yes, the string \"one\" is present in l1 list")


# In[ ]:




