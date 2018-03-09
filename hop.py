
# coding: utf-8

# # Heroes of Pymoli Data Analysis
# 

# In[48]:


import pandas as pd
import numpy 
import json
with open("purchase_data.json") as datafile:
    data = json.load(datafile)
df = pd.DataFrame(data)
df.head()


# **Player Count**

# In[49]:


#total number of players
uniqueplayers = df['SN'].nunique()
total_players_final = pd.DataFrame({"Total Players": [uniqueplayers]}, columns= ["Total Players"])
total_players_final


# **Purchase Analysis (Total) **

# In[50]:


#find number of unique items sold, purchase price, number of purchases, and total revenue for full dataframe
uniqueitems = df['Item ID'].nunique()
avgprice = (hop_df['Price'].sum()/df['Price'].count()).round(2)
totalpurchases = df['Price'].count()
totalrevenue = df["Price"].sum()

total_analysis_df = pd.DataFrame({"Number of Unique Items": [uniqueitems], 
                              "Average Purchase Price": [avgprice],
                             "Number of Purchases": [totalpurchases],
                             "Total Revenue": [totalrevenue]}, columns= ["Number of Unique Items", "Average Purchase Price",
                            "Number of Purchases", "Total Revenue"])

total_analysis_df.style.format({"Average Purchase Price": "${:.2f}", "Total Revenue": "${:.2f}"})


# **Gender Demographics**

# In[51]:


fullcount = df["SN"].nunique()
malecount = df[df["Gender"] == "Male"]["SN"].nunique()
femalecount = df[df["Gender"] == "Female"]["SN"].nunique()
othercount = fullcount - malecount - femalecount
maleperc = ((malecount/fullcount)*100)
femaleperc = ((femalecount/fullcount)*100)
otherperc = ((othercount/fullcount)*100)

gender_demo_df = pd.DataFrame({"Gender": ["Male", "Female", "Other / Non-Disclosed"], "Percentage of Players": [maleperc, femaleperc, otherperc],
                                        "Total Count": [malecount, femalecount, othercount]}, columns = 
                                        ["Gender", "Percentage of Players", "Total Count"])
                                        
gender_demo_final = gender_demo_df.set_index("Gender")
gender_demo_final.style.format({"Percentage of Players": "{:.2f}%"})                                      


# **Purchasing Analysis (Gender)**

# In[52]:


malepurch = df[df["Gender"] == "Male"]["Price"].count()
femalepurch = df[df["Gender"] == "Female"]["Price"].count()
otherpurch = totalpurchases - malepurch - femalepurch
mpriceavg = df[df["Gender"] == "Male"]['Price'].mean()
fpriceavg = df[df["Gender"] == "Female"]['Price'].mean()
opriceavg = df[df["Gender"] == "Other / Non-Disclosed"]['Price'].mean()
mpricetot = df[df["Gender"] == "Male"]['Price'].sum()
fpricetot = df[df["Gender"] == "Female"]['Price'].sum()
opricetot = df[df["Gender"] == "Other / Non-Disclosed"]['Price'].sum()
mnorm = mpricetot/malecount
fnorm = fpricetot/femalecount
onorm = opricetot/othercount

gender_purchase_df = pd.DataFrame({"Gender": ["Male", "Female", "Other / Non-Disclosed"], "Purchase Count": [malepurch, femalepurch, otherpurch],
                                        "Average Purchase Price": [mpriceavg, fpriceavg, opriceavg], "Total Purchase Value": [mpricetot, fpricetot, opricetot],
                                "Normalized Totals": [mnorm, fnorm, onorm]}, columns = 
                                        ["Gender", "Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"])
                                        
gender_purchase_final = gender_purchase_df.set_index("Gender")
gender_purchase_final.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}", "Normalized Totals": "${:.2f}"})



# **Age Demographics**

# In[53]:


#create age parameters - 4 year length
#create dataframe of unique players in each age group, find percentage against full count of players

tenyears = df[df["Age"] <10]
loteens = df[(df["Age"] >=10) & (df["Age"] <=14)]
hiteens = df[(df["Age"] >=15) & (df["Age"] <=19)]
lotwent = df[(df["Age"] >=20) & (df["Age"] <=24)]
hitwent = df[(df["Age"] >=25) & (df["Age"] <=29)]
lothirt = df[(df["Age"] >=30) & (df["Age"] <=34)]
hithirt = df[(df["Age"] >=35) & (df["Age"] <=39)]
loforty = df[(df["Age"] >=40) & (df["Age"] <=44)]
hiforty = df[(df["Age"] >=45) & (df["Age"] <=49)]

age_demo_df = pd.DataFrame({"Age": ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49"],
                        "Percentage of Players": [(tenyears["SN"].nunique()/fullcount)*100, (loteens["SN"].nunique()/fullcount)*100, (hiteens["SN"].nunique()/fullcount)*100, (lotwent["SN"].nunique()/fullcount)*100, (hitwent["SN"].nunique()/fullcount)*100, (lothirt["SN"].nunique()/fullcount)*100, (hithirt["SN"].nunique()/fullcount)*100, (loforty["SN"].nunique()/fullcount)*100, (hiforty["SN"].nunique()/fullcount)*100],
                        "Total Count": [tenyears["SN"].nunique(), loteens["SN"].nunique(), hiteens["SN"].nunique(), lotwent["SN"].nunique(), hitwent["SN"].nunique(), lothirt["SN"].nunique(), hithirt["SN"].nunique(), loforty["SN"].nunique(), hiforty["SN"].nunique()]
                       })

age_demo_final = age_demo_df.set_index("Age")
age_demo_final.style.format({"Percentage of Players": "{:.2f}%"})  
                        


# **Purchasing Analysis (Age)**

# In[54]:


age_purchasing_df = pd.DataFrame({"Age": ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49"],
                              "Purchase Count": [tenyears["Price"].count(), loteens["Price"].count(), hiteens["Price"].count(), lotwent["Price"].count(), hitwent["Price"].count(), lothirt["Price"].count(), hithirt["Price"].count(), loforty["Price"].count(), hiforty["Price"].count()],
                              "Average Purchase Price": [tenyears["Price"].mean(), loteens["Price"].mean(), hiteens["Price"].mean(), lotwent["Price"].mean(), hitwent["Price"].mean(), lothirt["Price"].mean(), hithirt["Price"].mean(), loforty["Price"].mean(), hiforty["Price"].mean()], 
                              "Total Purchase Value": [tenyears["Price"].sum(), loteens["Price"].sum(), hiteens["Price"].sum(), lotwent["Price"].sum(), hitwent["Price"].sum(), lothirt["Price"].sum(), hithirt["Price"].sum(), loforty["Price"].sum(), hiforty["Price"].sum()],
                              "Normalized Totals": [tenyears["Price"].sum()/tenyears['SN'].nunique(), loteens["Price"].sum()/loteens['SN'].nunique(), hiteens["Price"].sum()/hiteens['SN'].nunique(), 
                                                    lotwent["Price"].sum()/lotwent['SN'].nunique(), hitwent["Price"].sum()/hitwent['SN'].nunique(), 
                                                    lothirt["Price"].sum()/lothirt['SN'].nunique(), hithirt["Price"].sum()/hithirt['SN'].nunique(), 
                                                    loforty["Price"].sum()/loforty['SN'].nunique(), hiforty["Price"].sum()/hiforty['SN'].nunique()]}, 
                             columns = 
                            ["Age", "Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"])

age_purchasing_final = age_purchasing_df.set_index("Age")

age_purchasing_final.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}", "Normalized Totals": "${:.2f}"})


# **Top Spenders**

# In[55]:


sn_total_purchase = df.groupby('SN')['Price'].sum().to_frame()
sn_purchase_count = df.groupby('SN')['Price'].count().to_frame()
sn_purchase_avg = df.groupby('SN')['Price'].mean().to_frame()

sn_total_purchase.columns=["Total Purchase Value"]
join_one = sn_total_purchase.join(sn_purchase_count, how="left")
join_one.columns=["Total Purchase Value", "Purchase Count"]

join_two = join_one.join(sn_purchase_avg, how="inner")
join_two.columns=["Total Purchase Value", "Purchase Count", "Average Purchase Price"]

top_spenders_df = join_two[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]
top_spenders_final = top_spenders_df.sort_values('Total Purchase Value', ascending=False).head()
top_spenders_final.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})


# **Most Popular Items**

# In[56]:


#merge dataframes to find purchase count, total purchase value for items
#reset indices to dataframes can be merged on specific elements
premergeone = df.groupby("Item Name").sum().reset_index()
premergetwo = df.groupby("Item ID").sum().reset_index()
premergethree = df.groupby("Item Name").count().reset_index()

#merge dataframes
mergeone = pd.merge(premergeone, premergetwo, on="Price")
mergetwo = pd.merge(premergethree, mergeone, on="Item Name")

#start to create final dataframe by manipulating data
mergetwo["Gender"] = (mergetwo["Price_y"]/mergetwo["Item ID"]).round(2)

mergetwo_renamed = mergetwo.rename(columns={"Age": "Purchase Count", "Gender": "Item Price", "Item ID": "null", "Price_y": "Total Purchase Value", "Item ID_y": "Item ID"})

#grab columns we are looking for
clean_df = mergetwo_renamed[["Item ID", "Item Name", "Purchase Count", "Item Price", "Total Purchase Value"]]

prefinal_df = clean_df.set_index(['Item Name', 'Item ID'])
popular_items_final = prefinal_df.sort_values('Purchase Count', ascending=False).head(6)
popular_items_final.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})


# **Most Profitable Items**

# In[57]:


#use prefinal dataframe from prior to step to find most profitable items

profit_items_final = prefinal_df.sort_values('Total Purchase Value', ascending=False).head()
profit_items_final.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})

