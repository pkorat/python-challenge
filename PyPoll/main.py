#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import modules
import pandas as pd
import os


# In[2]:


# load the data using the os module
votes = os.path.join('Resources/election_data.csv')
votes_data = pd.read_csv(votes)

votes_data.head()


# In[3]:


# len() to find the total number of votes cast
total_votes = len(votes_data)
total_votes


# In[4]:


# unique() to get an array of candidate
candidates = votes_data['Candidate'].unique()
candidates


# In[5]:


# groupby() to create a series with percentages of votes
candidate_per = round(votes_data.groupby(['Candidate'])['Voter ID'].count() / total_votes * 100)
candidate_per


# In[6]:


# groupby() to create a series of counts of votes for each candidate
candidate_tally = votes_data.groupby(['Candidate'])['Voter ID'].count()
candidate_tally


# In[7]:


# find the max in the series and return the candidate index
most_votes = candidate_tally.max()
winner = candidate_tally[candidate_tally == most_votes].index[0]
winner


# In[8]:


election_results = """

Election Results \n
------------------------- \n
Total Votes: {} \n
------------------------- \n
{}: {}% ({}) \n
{}: {}% ({}) \n
{}: {}% ({}) \n 
{}: {}% ({}) \n
------------------------- \n
Winner: {} \n
-------------------------

""".format(total_votes, candidate_per.index[0], candidate_per[0], candidate_tally[0],
          candidate_per.index[1], candidate_per[1], candidate_tally[1],
          candidate_per.index[2], candidate_per[2], candidate_tally[2],
          candidate_per.index[3], candidate_per[3], candidate_tally[3],
          winner)

print(election_results)


# In[9]:


file1 = open('analysis/Election Results.txt', 'w')
file1.write(election_results)
file1.close()

