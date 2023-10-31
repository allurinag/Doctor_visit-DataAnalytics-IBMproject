# -*- coding: utf-8 -*-
"""doctor visit in DATA ANALYTICS.ipynb
"""

print("hello world")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

"""#Read the Dataset"""

df = pd.read_csv("DoctorVisits.csv")

print(df.head())

"""#Load the datasets and Display first 15 rows"""

print(df.head(15))

"""#Dispaly complete information about the cloumns of the dataset such as cloumn name,count, datatype and overall memory usage"""

df.info()

"""#Find out the total number of people based on their count of illeness"""

df["illness"].value_counts()

df["gender"].value_counts()

df["private"].value_counts()

"""#visuailze and analyse the maximum,minimumand medium income"""

y = list(df.income)
plt.boxplot(y)
plt.show()

"""# Find out the number of days of reduced activity of male and female seperatly due to illness"""

df.groupby(['gender', 'reduced']).mean()

"""# Visualize is there is any missing values in the dataset based on a heat map"""

sns.heatmap(df.isnull(),cbar=False,cmap='viridis')

"""#Find the correlation between variables in the given dataset correlation between different variables"""

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')

"""#Analyse how the income of a patient affects the number of visits to the hospital"""

#relation between income and visits
plt.figure(figsize=(20,20))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')

"""#count and visulize the number of males and females affected by illness"""

sns.histplot(df.gender,bins=3)

"""#Visualize the percentage of people getting govt heatlth due to low income,due to old and also the percentage of people having private health insurance"""

# % of people getting govt insurance due to low income
label=['yes','no']
Y = df[df['freepoor']=='yes']
N = df[df['freepoor']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt health insurance due to low income")
plt.show()
# % of people having private insurance
Y = df[df['private']=='yes']
N = df[df['private']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting private health insurance")
plt.show()
# % of people getting govt insurance due to old age, disability or veteran status
Y = df[df['freerepat']=='yes']
N = df[df['freerepat']=='no']
x = [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt health insurance due to old age, disability or veteran status")
plt.show()

"""#Plot a Horizontal bar chart to analyze the reduced days of activity due to illness based on Gender"""

db= df.groupby('gender')['reduced'].sum().to_frame().reset_index()
#creating the bar chart
plt.barh(db['gender'],db['reduced'],color = ['skyblue','purple'])
#adding the aesthatics
plt.title('Bar Chart')
plt.xlabel('gender')
plt.ylabel('reduced activity')
#show the plot
plt.show()
