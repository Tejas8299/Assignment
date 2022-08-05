#!/usr/bin/env python
# coding: utf-8

# ## To Create a python script (myscript.py) which will take in a csv file and convert it into a JSON file

# ### Importing the required modules

# In[30]:


import csv
import json
 


# ### Creating a function which will take in a csv file and convert it into a json file

# In[31]:



def csv_to_json(csv_file_path, json_file_path):
    
    data_dict = {}
 
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        
        for rows in csv_reader:
            
            key = rows['Serial no.']
            data_dict[key] = rows
            
    with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent = 4))
    
    
csv_file_path = input('Enter the absolute path of the CSV file: ')
json_file_path = input('Enter the absolute path of the JSON file: ')

csv_to_json(csv_file_path, json_file_path)


# ###  Here, I created a function in which I give a csv file name as Book1.csv as an input and it is converted into the json file format. I give it name as a Book1.json 

# ### Now,  Import the Module (converts the string to camelCase) and convert the keys of all the keys in the JSON file to camel case

# In[35]:


import Module as m


# In[36]:


import pandas as pd


# In[39]:


data=pd.read_json(r'C:\Users\TEJAS\Documents\Book1.json')
data.T


# ### Here, I used pandas for importing the json file. Pandas give it in dataframe.

# ### To view the data in json formate, I used the above method

# In[41]:


with open(r'C:\Users\TEJAS\Documents\Book1.json') as f:
    data_json=json.load(f)
    
print(data_json)   


# In[42]:


data_json


# In[ ]:





# In[ ]:





# In[ ]:




