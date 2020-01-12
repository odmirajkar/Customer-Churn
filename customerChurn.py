import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df=pd.read_csv('datasets-for-churn-telecom/cell2celltrain.csv')
churn_df=df[df['Churn']=='Yes']
non_churn_df= df[df['Churn']=='No']
plt.style.use("fivethirtyeight")

churn_df=df[df['Churn']=='Yes']
non_churn_df= df[df['Churn']=='No']


#Q1. how many customers are lost 
churned= df[df['Churn']=='Yes'].shape[0]
notchurned= df[df['Churn']=='No'].shape[0]
slices=[churned,notchurned]
labels=['Churned','Not Churned']
explode=[0.1,0]
plt.pie(slices,labels=labels,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,autopct='%1.1f%%')
plt.title("Percentage of customer churned")

plt.tight_layout()
plt.show()

#Q3 In terms of subscriber how many are chrun
# Customer can disconnect is one of subscribtion , instead of completing disconnecting. but it is also 
df['ChurnSubs']=df['UniqueSubs']-df['ActiveSubs']
slices=[df['ActiveSubs'].sum(),df['ChurnSubs'].sum()]
labels=['Active Subscriber','Churned']
explode=[0,0.1]
plt.pie(slices,labels=labels,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,autopct='%1.1f%%')
plt.title("Percentage of subscribers churned")

#plt.tight_layout()
plt.show()

#Q2 is there any difference in revenue distribution of customer
non_churn_df['MonthlyRevenue'].fillna(non_churn_df['MonthlyRevenue'].mean(),inplace=True)
churn_df['MonthlyRevenue'].fillna(churn_df['MonthlyRevenue'].mean(),inplace=True)
plt.hist(non_churn_df['MonthlyRevenue'],bins=[0,50,100,150,200,250,300,350,400,450,500],alpha=0.5, label='Non Churn customer')
plt.hist(churn_df['MonthlyRevenue'],bins=[0,50,100,150,200,250,300,350,400,450,500],alpha=0.5,label='Churn customer')
mean_rev=df['MonthlyRevenue'].mean()
plt.axvline(mean_rev,label='Mean Monthly Revenue',color='#91ee9a',linewidth=2)
plt.ylabel("No of customers")
plt.xlabel("Monthly revenue")
plt.legend()
plt.tight_layout()
plt.title('Revenue Distribution')
plt.show()


#Q3 are we loosing existing customer or new customer
non_churn_df['MonthsInService'].fillna(non_churn_df['MonthsInService'].mean(),inplace=True)
churn_df['MonthsInService'].fillna(churn_df['MonthsInService'].mean(),inplace=True)
plt.hist(non_churn_df['MonthsInService'],bins=[0,5,10,12,20,25,30,35,40,45,50,60],alpha=0.5, label='Non Churn customer')
plt.hist(churn_df['MonthsInService'],bins=[0,5,10,12,20,25,30,35,40,45,50,60],alpha=0.5,label='Churn customer')
mean_rev=df['MonthsInService'].mean()
plt.axvline(mean_rev,label='Mean MonthsInService',color='#91ee9a',linewidth=2)
plt.ylabel("No of customers")
plt.xlabel("Months in service")
plt.legend()
plt.tight_layout()
plt.title('MonthsInService Distribution')
plt.show()

#Q4 what is sucess rate of retention calls
retention_df=df[df['MadeCallToRetentionTeam']=='Yes']
slices=[retention_df[retention_df['Churn']=='No'].shape[0],retention_df[retention_df['Churn']=='Yes'].shape[0]]
labels=['Not Churned','Churned']
explode=[0,0.1]
plt.pie(slices,labels=labels,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,autopct='%1.1f%%')
plt.title("success rate of retention calls")
plt.show()

#Q5 sucess rate pf retention offers
retention_df=df[df['RetentionOffersAccepted']>0]
slices=[retention_df[retention_df['Churn']=='No'].shape[0],retention_df[retention_df['Churn']=='Yes'].shape[0]]
labels=['Not Churned','Churned']
explode=[0,0.1]
plt.pie(slices,labels=labels,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,autopct='%1.1f%%')
plt.title("success rate of retention offers")
plt.show()

#Q6 TruckOwner	RVOwner	Homeownership RespondsToMailOffers	OptOutMailings	NonUSTravel	OwnsComputer	HasCreditCard OwnsMotorcycle
cols=['TruckOwner','RVOwner','Homeownership','RespondsToMailOffers','OptOutMailings','NonUSTravel','OwnsComputer','HasCreditCard', 'OwnsMotorcycle']
impact_dict={}
for col in cols:
    no_churn_cust=churn_df[churn_df[col]=='Yes'].shape[0]
    normalize_no_churn_cust=no_churn_cust/churn_df.shape[0]
    no_non_churn_cust=non_churn_df[non_churn_df[col] == 'Yes'].shape[0]
    normalize_no_non_churn_cust=no_non_churn_cust/non_churn_df.shape[0]
    impact_score = normalize_no_non_churn_cust-normalize_no_churn_cust
    impact_dict[col]=impact_score
impact_dict={k: v for k, v in sorted(impact_dict.items(), key=lambda item: item[1],reverse=True)}    
    

#Q7 how is distribution of churn customer across income groups
income_groups=df['IncomeGroup'].unique()
income_groups.sort()
churn_customer_per_group=[]
df['IncomeGroup'].fillna(df['IncomeGroup'].mode())
non_churn_customer_per_group=[]
for income in income_groups:
    no_cust=churn_df[churn_df['IncomeGroup'] == income].shape[0]
    normalize_no_cust=no_cust/churn_df.shape[0]
    churn_customer_per_group.append(normalize_no_cust)
    no_cust=non_churn_df[non_churn_df['IncomeGroup'] == income].shape[0]
    normalize_no_cust=no_cust/non_churn_df.shape[0]
    non_churn_customer_per_group.append(normalize_no_cust)

x =  income_groups # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, churn_customer_per_group, width, label='Churn')
rects2 = ax.bar(x + width/2, non_churn_customer_per_group, width, label='Non Churn')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('No Of customers')
ax.set_title('Customer per income group')
ax.set_xticks(x)
ax.set_xticklabels(income_groups)
plt.xlabel("Income Groups")
ax.legend()



fig.tight_layout()

plt.show()    

#8 Credit rating 

credit_groups=df['CreditRating'].unique()
credit_groups.sort()
df['CreditRating'].fillna(df['CreditRating'].mode())
churn_customer_per_group=[]
non_churn_customer_per_group=[]
for credit in credit_groups:
    no_cust=churn_df[churn_df['CreditRating'] == credit].shape[0]
    normalize_no_cust=no_cust/churn_df.shape[0]
    churn_customer_per_group.append(normalize_no_cust)
    no_cust=non_churn_df[non_churn_df['CreditRating'] == credit].shape[0]
    normalize_no_cust=no_cust/non_churn_df.shape[0]
    non_churn_customer_per_group.append(normalize_no_cust)

x =  np.arange(len(credit_groups))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, churn_customer_per_group, width, label='Churn')
rects2 = ax.bar(x + width/2, non_churn_customer_per_group, width, label='Non Churn')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('No Of customers')
ax.set_title('Customer per credit group')
ax.set_xticks(x)
ax.set_xticklabels(credit_groups)
plt.xlabel("Credit Group")
ax.legend()



fig.tight_layout()
plt.show()    

#print("Total customer accepted the retention offer {}, conversion rate customer making call for retention offer then accepting it {}".format(retention_offer_df.shape[0],retention_offer_df.shape[0]/retention_df.shape[0])