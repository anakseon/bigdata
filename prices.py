
from collections import Counter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
matplotlib


def new_func():
    inline


new_func()

airbnb = pd.read_csv("E:/Kaggle/AB_NYC_2019.csv")
airbnb. head()
# View the total number of data
len(airbnb)
# View the data type of each column
airbnb.dtypes
# View missing values
airbnb.isnull().sum()
# In the drop function, axis=1 represents the column, inplace=True Indicates that the original dataframe will also change after deletion
airbnb.drop(['id', 'host_name', 'last_review'], axis=1, inplace=True)
# Check if the deletion was successful
airbnb. head(3)
# fillna function, fill in missing values
airbnb.fillna({'reviews_per_month': 0}, inplace=True)
# Check for success
airbnb.reviews_per_month.isnull().sum()
# Find the unique value of neighborhood_group
airbnb.neighborhood_group.unique()
# View the unique value of room_type
airbnb. room_type. unique()

# Take out the id of the top ten landlords with the most listings
top_host = airbnb.host_id.value_counts().head(10)
top_host
# Verify that the data is correct
top_host_check = airbnb.calculated_host_listings_count.max()
top_host_check
top_host_df = pd.DataFrame(top_host)
top_host_df.reset_index(inplace=True)  # Create a new index
top_host_df.rename(columns={'index': 'Host_ID',
                   'host_id': 'P_Count'}, inplace=True)  # index rename
top_host_df
# Visualize the landlord id data of the top ten listings
viz_1 = sns.barplot(x="Host_ID", y='P_Count', data=top_host_df,
                    palette='Blues_d')  # The parameter palette is the palette
viz_1.set_title('Host with the most listings in NYC')
viz_1.set_ylabel('Count of listings')
viz_1.set_xlabel('Host IDs')
# Set the x-axis scale label, rotation is the slope of the label
viz_1.set_xticklabels(viz_1.get_xticklabels(), rotation=45)
# Then analyze the administrative area

# Brooklyn
sub_1 = airbnb.loc[airbnb['neighborhood_group'] == 'Brooklyn']
price_sub1 = sub_1[['price']]

# Manhattn
sub_2 = airbnb.loc[airbnb['neighborhood_group'] == 'Manhattan']
price_sub2 = sub_2[['price']]

# Queens
sub_3 = airbnb.loc[airbnb['neighborhood_group'] == 'Queens']
price_sub3 = sub_3[['price']]

# StatenIsland
sub_4 = airbnb.loc[airbnb['neighborhood_group'] == 'Staten Island']
price_sub4 = sub_4[['price']]

# Bronx
sub_5 = airbnb.loc[airbnb['neighborhood_group'] == 'Bronx']
price_sub5 = sub_5[['price']]

# Put the house prices of all administrative districts into a list to facilitate subsequent analysis
price_list_by_n = [price_sub1, price_sub2, price_sub3, price_sub4, price_sub5]
# Create a new list, which will add the price distribution of each administrative district later
p_l_b_n_2 = []

nei_list = ['Brooklyn', 'Manhattn', 'Queens', 'Staten Island', 'Bronx']
for x in price_list_by_n:
    # percentiles sets the percentile of the output
    i = x.describe(percentiles=[.25, .50, .75])
    i = i.iloc[3:]  # iloc slices according to the index
    i. reset_index(inplace=True)
    i.rename(columns={'index': 'Stats'}, inplace=True)
    p_l_b_n_2.append(i)

# Change the "price" of each district to the corresponding district name
p_l_b_n_2[0].rename(columns={'price': nei_list[0]}, inplace=True)
p_l_b_n_2[1].rename(columns={'price': nei_list[1]}, inplace=True)
p_l_b_n_2[2].rename(columns={'price': nei_list[2]}, inplace=True)
p_l_b_n_2[3].rename(columns={'price': nei_list[3]}, inplace=True)
p_l_b_n_2[4].rename(columns={'price': nei_list[4]}, inplace=True)

stat_df = p_l_b_n_2
stat_df = [df.set_index('Stats') for df in stat_df]
stat_df = stat_df[0].join(stat_df[1:])
stat_df
sub_6 = airbnb[airbnb.price < 500]
# Visualize with a violin plot
viz_2 = sns.violinplot(data=sub_6, x='neighborhood_group', y='price')
viz_2.set_title(
    'Density and distribution of prices for each neighborhood_group')
# View the top ten communities
airbnb.neighborhood.value_counts().head(10)
sub_7 = airbnb.loc[airbnb['neighbourhood'].isin(['Williamsburg', 'Bedford-Stuyvesant', 'Harlem', 'Bushwick',
                                                 'Upper West Side', 'Hell\'s Kitchen', 'East Village', 'Upper East Side', 'Crown Heights', 'Midtown'])]
viz_3 = sns.catplot(x='neighbourhood', hue='neighbourhood_group',
                    col='room_type', data=sub_7, kind='count')  # hue adds a new latitude
viz_3.set_xticklabels(rotation=90)
viz_4 = sub_6.plot(kind='scatter', x='longitude', y='latitude', label='availability_365',
                   c='price', cmap=plt.get_cmap('jet'), colorbar=True, alpha=0.4, figsize=(10, 8))
viz_4. legend()
names = [name for name in airbnb.name]


def split_name(name):
    spl = str(name). split()
    return spl


names_for_count = []
for x in names:
    for word in split_name(x):
        word = word. lower()
        names_for_count.append(word)
top_25_w = Counter(names_for_count).most_common()
top_25_w = top_25_w[:25]

sub_w = pd. DataFrame(top_25_w)
sub_w.rename(columns={0: 'Words', 1: 'Count'}, inplace=True)
viz_5 = sns.barplot(x='Words', y='Count', data=sub_w)
viz_5.set_title('Counts of the top 25 used words for listing names')
viz_5.set_ylabel('Count of words')
viz_5.set_xlabel('Words')
viz_5.set_xticklabels(viz_5.get_xticklabels(), rotation=80)

# Get the top ten data of comments
top_reviewed_listings = airbnb.nlargest(10, 'number_of_reviews')
top_reviewed_listings
rice_avrg = top_reviewed_listings.price.mean()
print('Average price per night: {}'. format(price_avrg))
