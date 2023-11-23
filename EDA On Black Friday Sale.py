#!/usr/bin/env python
# coding: utf-8

# # EXPLORATORY DATA ANALYSIS ON BLACK FRIDAY SALE DATASET

# In[1]:


##Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#importing Dataset
df_train= pd.read_csv("E:\Black Fridady EDA data\BlackFriday_train.csv")


# In[3]:


df_train.head()  #Quick check Dataset


# In[4]:


df_test = pd.read_csv("E:\Black Fridady EDA data\Balckfriday_test.csv")


# In[5]:


df_test.head()


# In[6]:


#MERGE Both Train and test data
df = df_train.append(df_test)
df.head()


# In[7]:


#Data Information
df.info()


# In[8]:


#Information about Numeric Data
df.describe()


# In[9]:


#Information about Non-Numeric Data
df.describe(include='object')


# In[10]:


#Deleting Unwanted Data
df.drop(['User_ID'],axis=1,inplace=True)


# In[11]:


#check Data again
df.head()


# In[12]:


#Handle data in categorical method on gender
df['Gender']=df['Gender'].map({'F':0,'M':1})
df.head()


# In[13]:


#handle categorivcal feature age
df['Age'].unique()


# In[14]:


df['Age']=df['Age'].map({'0-17':1, '55+':7, '26-35':3, '46-50':5, '51-55':6, '36-45':4, '18-25':2})
df.head()


# In[15]:


#fix City_Category categorical data
df_city=pd.get_dummies(df['City_Category'],drop_first=True) #2 category sufficient to understand data
df_city.head()


# In[16]:


df=pd.concat([df,df_city],axis=1)
df.head()


# In[17]:


##Missing Value
df.isnull().sum()


# In[18]:


df['Product_Category_2'].value_counts()


# In[19]:


df['Product_Category_2'].mode()[0]


# In[20]:


##Replacing missing values with mode
df['Product_Category_2']=df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])


# In[21]:


df['Product_Category_2'].isnull().sum()


# In[22]:


##Replacing missing values for Product_Category_3
df['Product_Category_3'].unique()


# In[23]:


df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])


# In[24]:


df.head()


# In[25]:


df['Stay_In_Current_City_Years'].unique()


# In[26]:


df['Stay_In_Current_City_Years']= df['Stay_In_Current_City_Years'].str.replace('+','')


# In[27]:


df.head()


# In[28]:


df.info()


# In[29]:


##Convert Object into Integer , changing datatype
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)
df.info()


# In[30]:


df['B']=df['B'].astype(int)
df['C']=df['C'].astype(int)


# In[31]:


df.info()


# # DATA VISUALISATION

# In[32]:


##Creating Barplot
sns.barplot('Age','Purchase',hue='Gender',data=df)


# Conclusion - Purchasing with respect to Gender( 0=Female, 1= Male)the male purchase ih higher than female.

# In[33]:


##Viusalization of Product_Category_1 with purchase
sns.barplot('Product_Category_1','Purchase',hue='Gender',data=df,palette='Blues')


# In[ ]:





# In[ ]:




