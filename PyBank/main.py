#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import modules
import pandas as pd
import os


# In[2]:


# using the os module create a path to the data
budget = os.path.join('Resources/budget_data.csv')
budget_data = pd.read_csv(budget)

# show the first five rows
budget_data.head()


# In[3]:


# with the len() method to get number of total months
months = len(budget_data)


# In[4]:


# using sum() to get net total of profit/losses
net_total = budget_data['Profit/Losses'].sum()
net_total


# In[5]:


# mean() to get the average of the profit/losses column
change = budget_data['Profit/Losses'].diff()
avg_change = change.mean()


# In[6]:


# max() to get the greatest increase at the time period
increase_profit = change.max()
increase_profit


# In[7]:


# get index to find date
increase_date = budget_data['Date'][change[change == increase_profit].index[0]]
increase_date


# In[8]:


# min() to get the greatest decrease at the time period
decrease_profit = change.min()
decrease_profit


# In[9]:


# get index to find date
decrease_date = budget_data['Date'][change[change == decrease_profit].index[0]]
decrease_date


# In[10]:


financial_analysis = """
Financial Analysis \n
---------------------------- \n
Total Months: {} \n
Total: ${} \n
Average Change: ${} \n
Greatest Increase in Profits: {} (${})
Greatest Decrease in Profits: {} (${})
""".format(months, net_total, avg_change, increase_date, increase_profit, decrease_date, decrease_profit)

file1 = open('analysis/Financial Analysis.txt', 'w')
file1.write(financial_analysis)
file1.close()

print(financial_analysis)

