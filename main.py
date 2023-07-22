import numpy as np
import pandas as pd
from matplotlib import *
import matplotlib.pyplot as plt
from datetime import datetime
# import sklearn
import seaborn as sns

# import data
walmart_data = pd.read_csv(
    'C:\\Users\\1Marwan Ashraf\\.1MyStuff\\.0college\\3'
    'rd Semster\\data science methodology ✓\\Project\\walmart-sales-dataset-of-45stores.csv')
# end of importing data

# exploratory data analysis
print(f'Information about data:\n{walmart_data.info}\n')
print(f'Data description:\n{walmart_data.describe()}\n')
print(f'shape of the data:\n{walmart_data.shape}\n')
print(f'The columns of the data:\n{walmart_data.columns}\n')
print(f'The data types of the columns of the data:\n{walmart_data.dtypes}\n')
print(
    f'Is there duplicates?\n{walmart_data.duplicated().to_string() == True}.\n')
# End of exploratory analysis

# display data
print(f'First 10 Rows of the data:\n{walmart_data.head(10)}\n')
print(f'Last 10 Rows of the data:\n{walmart_data.tail(10)}\n')
print(f'we can also use walmart_data.to_string() to display all the data\n')
# End of displaying data

print(f'The shape before cleaning is:\n{walmart_data.shape}\n')

# perform data cleaning
# Detecting outliers :
print('Detecting outliers:')
x = ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
for i in x:
    sns.boxplot(walmart_data[i])
    plt.title(i)
    plt.show()
# Dropping outliers
print('Dropping outliers:')
walmart_data = walmart_data[
    (walmart_data['Unemployment'] < 10) & (walmart_data['Unemployment'] > 4.5) & (walmart_data['Temperature'] > 10)]
walmart_data
# Checking data for outliers
X = walmart_data[['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]
for i in x:
    sns.boxplot(walmart_data[i])
    plt.title(i)
    plt.show()
# End of data cleaning.

print(f'The shape after cleaning is:\n{walmart_data.shape}\n')

# question 1: Which store has maximum sales?
total_sales = pd.DataFrame(walmart_data.groupby('Store')['Weekly_Sales'].sum().sort_values(ascending=False))
print(f'Top 3 highest total weekly sales of stores:\n{total_sales.head(3)}\nSo we can deduce that store 20 has the '
      f'highest sales of the 45 stores')
# End of Answer 1

# question 2: Which store has maximum standard deviation i.e., the sales vary a lot
# The way of calculating the standard deviation is using .std() method
# dataFrame of the standard deviations of all
# the stores arranged in descending order
walmart_data_std = pd.DataFrame(walmart_data.groupby('Store')['Weekly_Sales'].std().sort_values(ascending=False))
print(f'Top 3 standard deviations of stores:\n{walmart_data_std.head(3)}\nSo we can deduce that store 14 has the most '
      f'variation of sales.')
# End of answer of question 2

# question3
# all data of sales within holidays dates
holiday_season = walmart_data[walmart_data['Holiday_Flag'] == 1]
# all data of sales not in holidays dates
non_holiday_season = walmart_data[walmart_data['Holiday_Flag'] == 0]
negative_impact = holiday_season[holiday_season['Weekly_Sales'] > non_holiday_season['Weekly_Sales'].mean()]
print(f'The holidays that have negative impact on the sales:\n{negative_impact.to_string()}\n')
# End of answer of question 3

# Convert date to datetime format
walmart_data['Date'] = pd.to_datetime(walmart_data['Date'])
walmart_data.info()
walmart_data.isnull().sum()
walmart_data["Day"] = pd.DatetimeIndex(walmart_data['Date']).day
walmart_data['Month'] = pd.DatetimeIndex(walmart_data['Date']).month
walmart_data['Year'] = pd.DatetimeIndex(walmart_data['Date']).year
# End of converting date to datetime format

# question 4
# classify data by year (2010, 2011, 2012)
walmart_data_2010 = walmart_data[(
    walmart_data['Year'] == 2010)].sort_values('Month')
monthly_total_weekly_sales_2010 = walmart_data_2010.groupby(
    'Month')['Weekly_Sales'].sum().sort_values(ascending=False)
walmart_data_2011 = walmart_data[(
    walmart_data['Year'] == 2011)].sort_values('Month')
monthly_total_weekly_sales_2011 = walmart_data_2011.groupby(
    'Month')['Weekly_Sales'].sum().sort_values(ascending=False)
walmart_data_2012 = walmart_data[(
    walmart_data['Year'] == 2012)].sort_values('Month')
monthly_total_weekly_sales_2012 = walmart_data_2012.groupby(
    'Month')['Weekly_Sales'].sum().sort_values(ascending=False)
# end of classifying data by year
# print(f'{walmart_data_2010}\n\n{walmart_data_2011}\n\n{walmart_data_2012}')
print(
    f'The total weekly sales for ever month for the year 2010:\n{monthly_total_weekly_sales_2010}\n'
    f'The total weekly sales for ever month for the year 2011:\n\n{monthly_total_weekly_sales_2011}\n'
    f'The total weekly sales for ever month for the year 2012:\n\n{monthly_total_weekly_sales_2012}')

plt.figure(figsize=(15,7))
plt.bar(walmart_data["Month"],walmart_data["Weekly_Sales"])
plt.xlabel("Months")
plt.ylabel("Weekly Sales")
plt.title("Monthly view of sales")
plt.show()

# End of question 4

# question 5
plt.scatter(walmart_data['Temperature'], walmart_data['Weekly_Sales'])
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.title('Weekly Sales vs Temperature')
plt.show()

plt.scatter(walmart_data['CPI'], walmart_data['Weekly_Sales'])
plt.xlabel('CPI')
plt.ylabel('Weekly Sales')
plt.title('Weekly Sales vs CPI')
plt.show()


plt.scatter(walmart_data['Unemployment'], walmart_data['Weekly_Sales'])
plt.xlabel('Unemployment')
plt.ylabel('Weekly Sales')
plt.title('Weekly Sales vs Unemployment')
plt.show()

plt.scatter(walmart_data['Weekly_Sales'], walmart_data['Fuel_Price'])
plt.xlabel('Weekly Sales')
plt.ylabel('Fuel Price')
plt.title('Weekly Sales vs Fuel Price')
plt.show()

sns.barplot(x= walmart_data['Year'], y=walmart_data['Weekly_Sales'], palette= 'Reds')
plt.title ('weekly sales vs years')
plt.show()
# End of question 5 

walmart_data_groupped = pd.DataFrame(walmart_data.groupby('Store'))

print(walmart_data_groupped.head(4))







# Visualization Start
label = [20, 4, 14, 13, 2, 10, 27, 6, 1, 39, 19, 31, 23, 24, 11, 28, 41, 32, 18, 22, 12, 26, 34, 40, 35, 8, 17, 45, 21,
         25, 43, 15, 7, 42, 9, 29, 16, 37, 30, 3, 38, 36, 5, 44, 33]
sns.barplot(x=label[:20],
            y=total_sales['Weekly_Sales'].head(20),
            palette='Blues',
            capsize=2)
plt.title('total sales')
plt.show()

fig, axis = plt.subplots()
walmart_data['Temperature'].plot.kde(ax=axis, legend=False, title='Temperature')
walmart_data['Temperature'].plot.hist(density=True, ax=axis)
axis.grid(axis='y')
plt.show()

plt.hist(walmart_data['Temperature'], bins=15)
plt.show()
# Visualization End

print(f'The final walmart data:\n{walmart_data}')

print(f'The total sales array is:\n{total_sales}')

print(walmart_data.groupby('Year')['Weekly_Sales'].sum())