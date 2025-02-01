#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))


# In[9]:


#using tuple to create an array
import numpy as np
ar1 = np.array(('a','b','c','d','e'))
print(ar1)
print(type(ar1))

#0D array
a1 = np.array(45)

#1D array
a2 = np.array([1,2,3,4,5])

#2D array
a3 = np.array([[1,2,3],[4,5,6]])

#3D array
a4 = np.array([[[1,2,3],[4,5,6]],[[3,6,9],[2,4,8]]])
print(a4)

#printing number of dimensions of array
print([a1.ndim,a2.ndim,a3.ndim,a4.ndim])

a5 = np.array([1,2,3,4,5],ndmin=5)
print(a5)


# In[17]:


import numpy as np

#accessing 1D array elements
one = np.array([1,2,3,4,5])
print(one[0],one[1])

#accessing 2D array elements
two = np.array([[1,2,3],[4,5,6]])
print(two[0,1])

#accessing 3D array elements
three = np.array([[[1,2,3],[4,5,6]],[[3,6,9],[4,5,7]]])
print(three[0,1,2])

#negative indexing
print(three[0,1,-1])


# In[29]:


import numpy as np

#array slicing
b1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(b1[1:4])

#to the end of array
print(b1[0:])

#Negative SLicing
print(b1[-3:-1])

#step = every other element type operations
print(b1[1:7:2])

#return every other element from the array
print(b1[::2])

#slicing 2D array
b2 = np.array([[1,2,3,4],[5,6,7,8]])
print(b2[1,1:3])


# In[1]:


#Numpy Datatypes
import numpy as np
d1 = np.array([1,2,3,4,5])
d2 = np.array(["abc","bcd","cghyr"])

print(d1.dtype)
print(d2.dtype)


# In[5]:


#defining datatypes
import numpy as np
e1 = np.array([1,2,3,4,5],dtype='S')
print(e1)
print(e1.dtype)

e2 = np.array([1.1,2.2,3.3,4.4,5.5])
newArr = e2.astype('i')
print(e2.dtype)
print(newArr.dtype)


# In[10]:


#copy and view
import numpy as np
q1 = np.array([1,2,3,4,5])
newQ = q1.copy()
q1[0] = 0

print(q1)
print(newQ)

q1[1] = 1
newQQ = q1.view()
print(newQQ)

x = q1.view()
y = q1.copy()

print(x.base) #view owns the data
print(y.base) #copy doesn't own the data


# In[ ]:




