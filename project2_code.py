#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  #does this allow for inline graphs? I think it does.

#fixing the dataframe
df=pd.read_csv("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
df.replace(to_replace="k", value="000", inplace=True) #what happens if it doesn't?, will have to iterate through, find the values with "k" then replace, potentially use regex? 
global_df=df.loc(:, "1962":"2011")
pd.to_numeric(global_df, errors="ignore") #does this make it so the column labels aren't touched, but the rest are changed?
or 
#~~this is based on whether or not I had to use a new df
~~new_global_df=global_df[1:]
~~pd.to_numeric(global_df[1:], errors="ignore") #does this raise an error since it's a slice? if so create a new sliced df.
~~years=[1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011] 
~~global_df.loc[0]=years #this should add header row

#check if the new dataframe is int or float
pd.global_df.dtypes

#add country names back, make sure both dataframes are good to go for analysis
global_df["country"]=list(df.loc["country"]) #didn't i do this another way? 
global_df
global_df.info()

westAfrica=["Benin", "Burkina Faso", "Cape Verde", "Cote d'Ivoire", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", "Mali", "Mauritania", "Niger", "Nigeria", "Senegal", "Sierra Leone", "Togo"]
wA_df= global_df.isin(westAfrica)
wA_df
wA_df.info()


#stats time! my questions: what are the overall trends for the region & globally? Within the region, are there any outliers? Does time seem like a significant factor for gdp per person? 
#remember, you can change the axes that they calculate on
global_df.describe()
global_df.mean()
global_df.mode()
global_df.median()

wA_df.describe()
wA_df.mean()
wA_df.mode()
wA_df.median()


#mapping time
#should I transpose the axes so I can do easier look ups by country? or will the following work? 

#this should show a histogram with both sets of data on it. 
global_df.hist(alpha=1, bins= 10, label="Global Trend") #this should show countries' GDP per capita by year
wA_df.hist(alpha=10, label="West African Trend") 
plt.legend();

#looking at a bar chart for all of the WA countries by decade for the average & potential outliers
wA_df.mean().plot(kind="bar"); #this should show averages of the region over time


#maybe this will plot all the points?  I want two views of the global vs regional data
wa_df.value_counts().plot(kind="scatter", color="orange", label="West African GDP per Capita") #there's probably more involved with scatterplots, like x & y axes or you could just keep using bar charts; also the goal is to show each individual point,
global_df.value_counts().plot(kind="scatter", color="blue", label="Global GDP per Capita")
plt.legend();




