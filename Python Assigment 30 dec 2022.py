#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get the Fibonacci series between 0 to 50.

# In[4]:


x,y=0,1

while y<50:
    print(y , end = ' ')
    x,y = y,x+y
	


# # Write a Python program that accepts a word from the user and reverse it.

# # 1.1.Reverse String using Slicing

# In[5]:


str= "Edyoda"

#reverse string using slicing

reversed = str[::-1]

#print reversed string

print(reversed)


# # Write a Python program to count the number of even and odd numbers from a series of numbers.

# In[6]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("No. of even numbers :",count_even)
print("No. of odd numbers :",count_odd)

