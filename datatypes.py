#!/usr/bin/env python
# coding: utf-8

# #First Program

# In[20]:


x = -1
print(type(x))

y = "thisisastring"
print(type(y))

z = True
print(type(z))

p = 1.01
print(type(p))

q = -9j
print(type(q))

r = 2e10
print(r)

#We use a hash to run a comment in python.


# In[27]:


#Casting

x = int(1.1)
y = int(2)
z = int("3")

l = {x,y,z}
m = (x,y,z)
n = [x,y,z]

#set, tuple, list
print(l,m,n)
print(type(l))
print(type(m))
print(type(n))


# In[40]:


#print("Hello")
#print('Hello')
#same

#slicing strings
a = "apple"
b = "mango"
c = "banana"

print(a[0:],b[1:3],c[:-1])

#reverse string
print(a[::-1])

#excludes last letter of string
print(a[0:-1])

#displays every 2nd element
print(a[0: :2])


# In[48]:


#Modifying strings

str1 = 'ALABAMA'
str2 = 'newyork'
str3 = 'Hell or Heaven'

print(str1.lower())
print(str2.upper())
print(str3.strip())
print(str3.split(" "))
print(str2.replace("n","l"))


# In[ ]:




