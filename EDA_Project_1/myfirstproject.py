import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r'D:\DataAanalytics\MyProjects\Taxi_Trips_-_2024_20240408.csv')
# print(df)
#table info
# df.info()

# check null value
# print(df.isna().sum()) 

#deleted column with maximum null values
del df['Pickup Census Tract']
df.pop('Dropoff Census Tract')
#check duplicates
# print(df['Pickup Census Tract'])
df.info()
# print(df.isna().sum()) 

# to fill null values
# mean1=df["Trip Seconds"].mean()
# df["Trip Seconds"].fillna(mean1,inplace=True)
# print(df)
# print("No of null values:",df.isna().sum())

df[['Trip Seconds','Trip Miles','Pickup Community Area','Dropoff Community Area','Fare','Tips','Tolls','Extras','Trip Total']] = df[['Trip Seconds', 'Trip Miles', 'Pickup Community Area','Dropoff Community Area','Fare','Tips','Tolls','Extras','Trip Total']].fillna(df.mean(numeric_only=True))

print(df)

df['Trip Start Timestamp'] = pd.to_datetime(df['Trip Start Timestamp'], errors='coerce')
df['Trip End Timestamp'] = pd.to_datetime(df['Trip End Timestamp'], errors='coerce')


del df['Pickup Centroid Latitude']
del df['Pickup Centroid Longitude']
del df['Dropoff Centroid Latitude']
del df['Dropoff Centroid Longitude']
print(df.isna().sum()) 

# to fill column object values using 'unknown'
df.loc[df['Dropoff Centroid  Location'].isna(),'Dropoff Centroid  Location'] = 'unknown'
df['Pickup Centroid Location'] = df['Pickup Centroid Location'].replace({None: 'unknown'})
df['Taxi ID'] = df['Taxi ID'].replace({None: 'unknown'})



print(df.isna().sum())

# print("No of duplicates:",df.duplicated().sum())

df.columns = df.columns.str.replace(" ", "_")
print(df)

df['Trip_Start_Timestamp'] = df['Trip_Start_Timestamp'].replace({None: 'unknown'})
df['Trip_End_Timestamp'] = df['Trip_End_Timestamp'].replace({None: 'unknown'})
df.info()

print(df.columns)
#T check duplicate values
print("No of duplicates:",df.duplicated().sum())

df.info()

#To round column values 
df['Dropoff_Community_Area']=df['Dropoff_Community_Area'].round(2)
df['Pickup_Community_Area']=df['Pickup_Community_Area'].round(2)
# print(df['Dropoff_Community_Area'])

df.info()

# correlation = df.select_dtypes(include=['number']).corr()
# sns.heatmap(correlation,annot=True,cmap='plasma')
# plt.show()

#updated file to new csv
# df.to_csv(r"D:\DataAanalytics\MyProjects\Taxi_Trip.csv")


#Groupby Questions

#what is the average trip duration and fare for each payment type?
df.groupby("Payment_Type").agg({"Trip_Seconds": "mean", "Fare": "mean"})

print(df)

#What is the average trip duration
print('Mean of total number of trip: ',df['Trip_Total'].mean())

#What is the distribution of payment types?
payment_count=df['Payment_Type'].value_counts()

fig, ax = plt.subplots(figsize=(6, 4))

payment_count.plot(kind='bar', stacked=True, color=['blue', 'orange', 'green'], ax=ax)


plt.xlabel('payment Type')
plt.ylabel('Count')
plt.title('Distribution of payment Types')
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()




#What is the distribution of Company?

diff_company=df['Company'].value_counts()
plt.figure(figsize=(50,50))
plt.pie(diff_company, labels=diff_company.index, autopct='%1.1f%%', 
        colors=['blue', 'orange', 'green'], startangle=140, wedgeprops={'edgecolor': 'black'})

plt.title('Distribution of Payment Types')

plt.show()


# #1.What are the top 5 pickup locations?
# top_pickups = df["Pickup_Community_Area"].value_counts().head(5)
# print(top_pickups)

# #2.What is the most common payment type?
# payment_counts = df["Payment_Type"].value_counts()
# print(payment_counts)

# plt.figure(figsize=(8, 5))
# sns.barplot(x=payment_counts.index, y=payment_counts.values, palette="pastel")
# plt.xlabel("Payment Type")
# plt.ylabel("Number of Trips")
# plt.title("Most Common Payment Type in Taxi Trips")
# plt.xticks(rotation=45)
# # Show plot
# plt.show()


# #3.Do passengers who pay with credit cards tip more than those who pay with cash?

# plt.figure(figsize=(8, 5))
# sns.boxplot(x="Payment_Type", y="Tips", data=df, palette="pastel")
# plt.xlabel("Payment Type")
# plt.ylabel("Tips ($)")
# plt.title("Tips Distribution by Payment Type")
# plt.xticks(rotation=45)
# plt.ylim(0, 10) 
# plt.show()

# # 5.what community has lowest number of pickups?

# top_pickups = df["Pickup_Community_Area"].value_counts().head(10)

# plt.figure(figsize=(10, 5))
# sns.barplot(x=top_pickups.index, y=top_pickups.values, palette="coolwarm")
# plt.xlabel("Pickup Community Area")
# plt.ylabel("Number of Trips")
# plt.title("Top 10 Pickup Community Areas")
# plt.show()

# we can find outlayers with boxplot 