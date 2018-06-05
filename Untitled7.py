
# coding: utf-8

# In[4]:


import requests 
r = requests.get("https://python123.io/ws/demo.html")
r.text



# In[9]:


demo = r.text 
from bs4 import BeautifulSoup 
Soup = BeautifulSoup(demo,"html.parser")
print(Soup.prettify())

