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
