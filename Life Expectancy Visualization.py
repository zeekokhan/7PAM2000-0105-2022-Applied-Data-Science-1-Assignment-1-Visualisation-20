#!/usr/bin/env python
# coding: utf-8

# # Loading Modules & Data

# In[1]:


import pycountry
import pandas as pd
import seaborn as sns
import pycountry_convert as pc
import matplotlib.pyplot as plt

import warnings
warnings.simplefilter("ignore")


# In[2]:


df = pd.read_csv("API_SP.DYN.LE00.IN_DS2_en_csv_v2_4770434.csv", skiprows=4).iloc[:, :-2]
df.head(3)


# In[3]:


countries = list(pycountry.countries)
country_names = [country.name for country in countries]

df = df[df["Country Name"].isin(country_names)]


# # Visualization

# In[4]:


df_temp = df.iloc[:, 4:].T
df_temp.columns = df["Country Name"]
df_temp.dropna(axis=1, inplace=True)
temp_low = df_temp.mean().sort_values().iloc[:10].index
temp_up = df_temp.mean().sort_values().iloc[-10:].index


# In[14]:


df_temp[temp_low].plot(kind="box", figsize=(16, 5))
plt.title("Distribution of Average Life Expectancy of top 10 Lowest Countries")
plt.xlabel("Age")
plt.ylabel("Country")
plt.show()


# In[6]:


df_temp[temp_up].plot(kind="line", figsize=(15, 6))
plt.title("Life Expectancy of 10 Countries whose average is Highest")
plt.show()
