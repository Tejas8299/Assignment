#!/usr/bin/env python
# coding: utf-8

# ## To Create a python module and a function within the module which takes a string as input and converts the string to camelCase.

# ### Importing the required module

# In[6]:


from re import sub


# ### Creating the function to convert the string to camelCase

# In[7]:


def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].lower() + string[1:]


# #### Now, we can check that how our function are works

# In[8]:


camelCase('Intelligence Quotient')


# #### Hence, as we observe here we give a string as a input and it is converted to the camelCase.
