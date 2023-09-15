#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("Video Games Sales.csv")
df.head()


# In[64]:


df[df['Year'] == 2006]


# In[3]:


df.shape


# The 'Rank' column identifies each game's ranking according to its global sales (highest to lowest). This can help you identify which games are most popular globally.<br>
# The 'Game Title' column contains the name of each video game, which allows you to easily discern one entry from another.<br>
# The 'Platform' column lists the type of platform on which each game was released, e.g., PlayStation 4 or Xbox One, so that you can make comparisons between platforms as well as specific games for each platform.<br>
# The 'Year' column provides an additional way of making year-on-year comparisons and tracking changes over time in global video game sales.<br>

# In addition, this dataset also contains metadata such as genre ('Genre'), publisher ('Publisher'), and review score ('Review') that add context when considering a particular title's performance in terms of global sales rankings.

# Lastly but no less important are the three variables dedicated exclusively for geographic breakdowns: North America ('North America'), Europe (Europe), Japan (Japan), Rest of World (Rest of World), and Global (Global). This allows us to see how certain regions contribute individually or collectively towards a given title's overall sales figures; by comparing these metrics regionally or collectively an interesting picture arises -- from which inferences about consumer preferences and supplier priorities emerge!

# # Data Exploration

# ## Univariate EDA

# ### Column "Rank"

# In[4]:


df['Rank'].describe()


# In[5]:


df['Rank'].unique()


# All of the values are unique

# ### Column "Game Title"

# In[6]:


df['Game Title'].describe()


# In[7]:


df['Game Title'].nunique()


# The column 'Game Title' seems to have duplicate values

# In[8]:


df['Game Title'].value_counts()


# In[9]:


df[df['Game Title'] == 'LEGO Batman: The Videogame']


# In[10]:


df[df['Game Title'] == 'FIFA Soccer 08']


# Some video game titles are released for more than one platform

# ### Column 'Platform'

# In[11]:


df['Platform'].describe()


# In[12]:


df['Platform'].unique()


# ### Column 'Year'

# In[13]:


df['Year'].describe()


# The data type of the column is float64, won't be a problem for analytics.

# In[14]:


# df['Year'] = pd.to_datetime(df['Year'].fillna(0).astype(int), format='%Y')
# df['Year'] = pd.to_datetime(pd.to_numeric(df['Year'], errors='coerce'), errors='coerce', format='%Y').fillna(df['Year'])
# df.head()


# In[15]:


df.groupby('Year')['Game Title'].count()


# In[61]:


temp1 = pd.DataFrame(df.groupby(['Year', 'Genre'])['North America'].sum())
temp1.to_csv(r'/Users/abimanyu/Desktop/Notes and Docs/COSC/temp1.csv', index=True)


# ### Column 'Genre'

# In[16]:


df['Genre'].describe()


# In[17]:


df['Genre'].unique()


# ### Column 'Publisher'

# In[18]:


df['Publisher'].describe()


# In[19]:


df['Publisher'].unique()


# ### Null values

# In[20]:


df.isnull().sum()


# We have a small number of null values in the data, we'll remove them for now.

# In[21]:


df1 = df.dropna()
df1.isnull().sum()


# ## Bivariate EDA

# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns


# ### Columns 'Genre' and 'Review'

# In[23]:


genre_reviews = df1[['Genre', 'Review']].groupby('Genre').mean()
genre_reviews


# In[24]:


plt.bar(genre_reviews.index, genre_reviews['Review'])
plt.xticks(rotation = 45)
plt.show()


# We see that the role-playing genre has the highest average review score.There is not much difference between the average review scores of the different genres.

# ### Column 'Platform' and 'Review'

# In[25]:


platform_reviews = df1[['Platform', 'Review']].groupby('Platform').mean()
platform_reviews


# In[26]:


plt.bar(platform_reviews.index, platform_reviews['Review'])
plt.xticks(rotation = 60)
plt.show()


# Video games on Sega Dreamcast has the highest average review score

# ### Column 'Publisher' and 'Review'

# In[27]:


publisher_reviews = df1[['Publisher', 'Review']].groupby('Publisher').mean().sort_values('Review', axis=0, ascending=False)
publisher_reviews


# In[28]:


plt.bar(publisher_reviews.head().index, publisher_reviews.head()['Review'])
plt.xticks(rotation = 45)
plt.show()


# Here are the top 5 publishers of video games with the highest average review score.

# ### Column 'Genre' and 'North America'

# Here, we are assuming that the sales are not percentages, but profits in dollars.

# In[29]:


genre_NA = df1[['Genre', 'North America']].groupby('Genre').sum().sort_values('North America', ascending=False)
genre_NA


# In[30]:


plt.bar(genre_NA.head().index, genre_NA.head()['North America'])
plt.xticks(rotation = 45)
plt.show()


# Here are the top 5 most profitable video game genres in North America

# ### Colum 'Genre' and 'Europe'

# In[31]:


genre_EU = df1[['Genre', 'Europe']].groupby('Genre').sum().sort_values('Europe', ascending=False)
genre_EU


# In[32]:


plt.bar(genre_EU.head().index, genre_EU.head()['Europe'])
plt.xticks(rotation = 45)
plt.show()


# The top 5 most profitable genre in Europe are the same as in North America

# ### Column 'Genre' and 'Japan'

# In[33]:


genre_JP = df1[['Genre', 'Japan']].groupby('Genre').sum().sort_values('Japan', ascending=False)
genre_JP


# In[34]:


plt.bar(genre_JP.head().index, genre_JP.head()['Japan'])
plt.xticks(rotation = 45)
plt.show()


# We see that the most popular genre of video games in Japan are different from NA and EU. Here, Role-Playing games takes the top spot.

# ## Exploring Trends in Video Games

# ### Popular Video Games Each Year In NA

# In[35]:


yearly_NA = df1.loc[df1.groupby('Year')['North America'].idxmax()]
yearly_NA


# In[ ]:


years = yearly_NA['Year'].tolist()
sales = yearly_NA['North America'].tolist()
titles = yearly_NA['Game Title'].tolist()

plt.scatter(yearly_NA['Year'], yearly_NA['North America'])

for i, txt in enumerate(sales):
    plt.annotate(titles, (years[i], sales[i]))


# In[ ]:


df[df['Year'] == 1983]


# ### Popular Video Games Each Year In EU

# In[38]:


df1.loc[df1.groupby('Year')['Europe'].idxmax()]


# ### Popular Video Games Each Year In JP

# In[39]:


df1.loc[df1.groupby('Year')['Japan'].idxmax()]

