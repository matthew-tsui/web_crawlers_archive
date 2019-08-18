#!/usr/bin/env python
# coding: utf-8

# In[116]:


import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[117]:


http = urllib3.PoolManager()


# In[109]:


record = {'serial_no':'','cert_no':'','unit_name':'','address':'','domain':'','class':''}
df = pd.DataFrame()

start_page = 1
last_page = 1109

for i in range(start_page, last_page):
    r = http.request('GET', 'http://183.62.232.215/szsti/hightech.jsp?currentpage='+str(i)+'&eos_key=&name=')
    soup = BeautifulSoup(r.data, 'html.parser')
    
    # Skip the first row
    rows = soup.find_all('tr')[4:]
    for row in rows:
        tds = row.find_all('td')
        new_record = {'serial_no':tds[0].text.strip(),'cert_no':tds[1].text.strip(),'unit_name':tds[2].text.strip(),'address':tds[3].text.strip(),'domain':tds[4].text.strip(),'class':tds[5].text.strip()}
        df = df.append(new_record, ignore_index = True)

    time.sleep(0.1)
    print("Completed page", i)

print('Finished!!')


# In[111]:


df.shape


# In[114]:


df.to_csv('1-100.csv',  encoding='utf_8_sig')


# In[19]:





# In[118]:


df


# In[ ]:




