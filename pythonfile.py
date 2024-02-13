import pandas as pd 

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

dr = pd.read_csv('NAZARI_NIYAZ_python_assignment2_orig.csv')

# dr.dtypes
# dr.head(3)
# dr.info()
# dr.isna().sum()
# dr.shape
# dr.describe()
# dr = dr.rename(columns={'YEAR REGISTERED': 'REGISTEREDYEAR'})       #rename a column
# dr.info()
# dr['PROPERTY TYPE'].unique()            #unique values of a column
# dr['PROPERTY TYPE'].value_counts() 
# dr['WARDNAME'].value_counts()
# dr['WARDNAME'].unique()
# type(dr['RSN'][0])                      # RSN column type is int64
# dr['RSN'] = dr['RSN'].astype(str)       # change the RNS column data type from int64 to str
# type(dr['RSN'][0])
# dr['RSN'] = dr['RSN'].astype('Int64')   # change the RNS column back to int64 
# type(dr['RSN'][0])
# # Save the Data frame in an Excel file
# dr.to_excel('NAZARI_NIYAZ_python_assignment2_proc.xlsx' , index=False)
# # Add a new column named LOCATION. Fill the data with concatenation of lat and long columns
# dr['LOCATION'] = '(' + round(dr['LATITUDE'] , 2).astype(str) + ',' + round(dr['LONGITUDE'] , 2).astype(str) + ')'
# # Add a new column name DIRECTION and fill the data with expansion of geographic directions
# dr['DIRECTION'] = dr['GRID'].str[0]
# dr['DIRECTION'] = dr['DIRECTION'].str.replace('N' , 'NORTH')
# dr['DIRECTION'] = dr['DIRECTION'].str.replace('S' , 'SOUTH')
# dr['DIRECTION'] = dr['DIRECTION'].str.replace('E' , 'EAST')
# dr['DIRECTION'] = dr['DIRECTION'].str.replace('W' , 'WEST')
# # Drop newly added column LOCATION
# dr.drop(columns='LOCATION' , inplace=True)
# filter_list =['PRIVATE' , 'SOCIAL HOUSING' ]
# dr = dr.loc[dr['PROPERTY TYPE'].isin(filter_list)]
# dr.head(3)
# dr = dr.rename(columns={'PARKING AREAS': 'PARKING'}) 
# dr.query('PARKING > 1').head(10)     # This will list the apartments which has more than one parking place
# df_with_nan = dr[dr.isna().any(axis=1)]         # Returns all the rows which has NaN value in any of the columns
# df_with_nan.head(3)
# dr[(dr['REGISTEREDYEAR'].isna()) & (dr['FENCING'].isna())].head(10)     # Select the rows with two column NaN
# dr.dropna(subset=['REGISTEREDYEAR'], inplace=True)              # Drop those apartment which their Registration date is null
# # # Grouping and aggregating
# dr_grouped = dr.groupby('WARDNAME')
# dr_grouped.size()
# dr_summary = dr.groupby('PROPERTY TYPE').agg(storeys_count=('CONFIRMED STOREYS' , 'count') , mean_units = ('CONFIRMED UNITS' , 'mean'))
# #dr_summary

# # Plot
import matplotlib.pyplot as plt 
fig , ax = plt.subplots()

ax.set_title('Building Score Depend On Building Year')
ax.set_xlabel('Building Year')
ax.set_ylabel('Score')
ax.set_axisbelow(True)          # The line will be below dots
ax.grid(alpha = 0.7 )
plt.scatter(dr['YEAR BUILT'] , dr['CURRENT BUILDING EVAL SCORE'])
plt.savefig('buildingscore.png')

# building = ax.scatter(dr['YEAR BUILT'] , dr['CURRENT BUILDING EVAL SCORE'])
# ax.legend([building ] , ['Building'] ,
#           bbox_to_anchor = (1,1) ,
#           loc = 'upper left'
#           ) 
# fig , ax = plt.subplots()
# ax.set_title('Building Score and Unit Number For Building Year')
# ax.set_xlabel('Building Year')
# ax.set_ylabel('Score')
# ax.set_axisbelow(True)          # The line will be below dots
# ax.grid(alpha = 0.7 )
# score = ax.scatter(dr['YEAR BUILT'] , dr['CURRENT BUILDING EVAL SCORE'])
# units = ax.scatter(dr['YEAR BUILT'] , dr['CONFIRMED UNITS'])
# ax.legend([score , units] , ['Building Score' , 'Building Units'] ,
#           bbox_to_anchor = (1,1) ,
#           loc = 'upper left'
#           ) 


# # Note: seaborn and plotly didn't teach in the class. I read the documentation myself.
# import seaborn as sns
# sns.scatterplot(x=dr['YEAR BUILT'], y=dr['CONFIRMED UNITS'] )
# plt.grid(True)
# plt.show()


# import plotly.express as px
# fig = px.scatter(x=dr['YEAR BUILT'], y=dr['CONFIRMED UNITS'] , labels={'x': 'Building Year', 'y': 'Number of Units'}, title='Number of Apartment Units During the Years')
# fig.show()


