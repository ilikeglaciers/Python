#!/usr/bin/env python
# coding: utf-8

# In[36]:


#regular expressions
import re
str1 = "thisisasamplestring"
print(re.search("sample",str1))

#metacharacters
print(re.search('[all]take[s]','alltakesonyou')) # [ ]
print(re.search('[i] like [the] ','i like the weeknd'))

print(re.search('[0-9][0-9][0-9][0-9][0-9][0-9]','123456')) # -
print(re.search('[^0-9]','elephant')) # ^
print(re.search('[a-z|A-Z|0-9]','a')) # |
print(re.search('[a-z|$]','$2.47'))
print(re.search('..Z','ABCDEFGZ'))


# In[41]:


#Regex Anchors
import re
print(re.search('^bud','buddy'))
print(re.search('^bud','dummy'))

print(re.search('Zeb$','ronicsZeb'))
print(re.search('align$','postalign'))


# In[42]:


#all() and any()
a,b,c=10,20,30
x=all((a>5,b<2,c>20))
print(x)

y=any((a>5,b<2,c>20))
print(y)


# In[47]:


s = input("Type a name: ")
y = int(input("Type the age: "))
m = float(input("Type your marks: "))
print(s+" whose age is "+str(y)+" has scored "+str(m)+" percentage in his/her exams")


# In[ ]:




