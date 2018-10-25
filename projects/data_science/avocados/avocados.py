#!/usr/bin/env python
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

avocados = pd.read_csv('csv_files/avocado.csv')


# Rounding all of the columns that have to do with 'bags' to the nearest integer
avocados['Total Bags'] = avocados['Total Bags'].apply(lambda x: int(round(x)))
avocados['Small Bags'] = avocados['Small Bags'].apply(lambda x: int(round(x)))
avocados['Large Bags'] = avocados['Large Bags'].apply(lambda x: int(round(x)))
avocados['XLarge Bags'] = avocados['XLarge Bags'].apply(lambda x: int(round(x)))


# Finding the yearly average of total volume and plotting a bar chart with the results
plt.figure()
vol_avg_yearly = avocados.groupby('year')['Total Volume'].mean()
vol_avg_yearly.plot.bar()
plt.title('Average total volume of avocados per year')
plt.ylabel('Total volume')
plt.xlabel('year')
plt.savefig('avocados_data/yearly_volume_avg_bar.png')


# Finding the monthly total volume average for each year, line graph 
plt.close('all')
plt.figure()
ax = plt.subplot()
vol_avg_month_year = (vol_avg_yearly / 12) 
vol_avg_month_year.plot.line()
ax.set_xticks([2015, 2016, 2017, 2018])
plt.title('Monthly average of total volume per year')
plt.ylabel('Units')
plt.xlabel('Year')
plt.savefig('avocados_data/monthly_volume_avg_by_year_line.png')


# Percentage breakdown of all bags, pie chart
plt.close('all')
plt.figure()
df_bags = avocados[['Small Bags', 'Large Bags', 'XLarge Bags']] 
df_bags_sum = df_bags.sum()
df_bags_sum.plot.pie(y='total_bags_sum', autopct='%0.1f%%')
plt.axis('equal')
plt.title('Distribution of bag sizes')
plt.ylabel('')
plt.legend()
plt.savefig('avocados_data/bag_percentage_pie.png')


# Total volume by region
regional_vol = avocados.groupby('region')['Total Volume'].mean()
regional_vol = regional_vol.round(decimals=0).astype(int)
regional_vol = regional_vol.reset_index(name='average volume')
regional_vol.to_csv('avocados_data/regional_average_volume.csv')


# Further breaking down average regional volume by year now
yearly_reg_vol = avocados.groupby(['region', 'year'])['Total Volume'].mean().reset_index()
yearly_reg_vol['Total Volume'] = yearly_reg_vol['Total Volume'].astype(int)
regions_list = yearly_reg_vol['region'].unique().tolist()

# Defining function that will find the change in Total Volume from 2015 to 2018. By finding the difference
def four_change(x):
    year_2018 = yearly_reg_vol.loc[((yearly_reg_vol['region'] == x) & (yearly_reg_vol['year'] == 2018), 'Total Volume')] 
    year_2018 = int(year_2018)
    year_2015 = yearly_reg_vol.loc[((yearly_reg_vol['region'] == x) & (yearly_reg_vol['year'] == 2015), 'Total Volume')]
    year_2015 = int(year_2015)
    change = year_2018 - year_2015
    return change

# Applying the function to each row, and creating a new column to store the Total Volume change.
yearly_reg_vol['2015_to_2018_change'] = yearly_reg_vol.apply(lambda x: four_change(x.region)\
        if x.year == 2018 \
        else np.nan, axis=1)

# Changing all of the null values, added above, into integers in order to convert the entire column to int.
yearly_reg_vol['2015_to_2018_change'].fillna(0, inplace=True)
yearly_reg_vol['2015_to_2018_change'] = yearly_reg_vol['2015_to_2018_change'].apply(lambda x: int(x))
yearly_reg_vol.drop(yearly_reg_vol[(yearly_reg_vol['year'] == 2016) | (yearly_reg_vol['year'] == 2017)].index, inplace=True)
yearly_reg_vol = yearly_reg_vol.reset_index(drop=True)

# Saving to CSV
yearly_reg_vol.to_csv('avocados_data/yearly_regional_volume_change.csv')


# Getting the min/median/max of each year's Total Volume and saving to CSV
agg_vol_yearly = avocados.groupby('year')['Total Volume'].agg(['min', 'median', 'max'])
agg_vol_yearly.rename_axis('Total Volume min/median/max by Year', axis=1)
agg_vol_yearly.to_csv('avocados_data/agg_volume_yearly.csv')


# Median price of each region, then plotting as a lineplot
plt.close('all')
ax = plt.subplot()
median_price_region = avocados.rename(columns={'AveragePrice': 'Price'}).groupby('region')['Price'].median().reset_index()
region_list = avocados['region'].unique().tolist()
median_price_region.plot.line(ax=ax, marker='s', grid=True, figsize=(15,10))

# Labeling the X/Y axes, and creating a title 
plt.xlabel('regions')
plt.ylabel('average price in US dollars')
plt.title('Median price of Avocados for every Region')
ax.set_xticks(range(len(region_list)))
ax.set_xticklabels(region_list, rotation=90)

# Creating the values in the y-axis. Created a new list, populated the list, and preappended $ to each value 
y_interval = np.linspace(0.9, 1.9, num=21)
y_interval_list = y_interval.tolist()
new_y_axis = []

for x in y_interval_list:
    new_y_axis.append(str(x))

new_y_axis = ['$' + x for x in new_y_axis]

ax.set_yticks(y_interval)
ax.set_yticklabels(new_y_axis)
ax.legend()
plt.tight_layout()
plt.savefig('avocados_data/regional_median_price_line.png')

