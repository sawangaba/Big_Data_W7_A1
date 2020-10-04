
#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Top Items sold")
plt.ylabel("Sales in 2016")
data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv") 

data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
data['year'] = data['Date'].dt.year

# # changing index to sort the date easily into new dataset.
# datee = data.set_index(['Date'])
# sixteen=datee.loc['30-10-2016':'31-12-2016']


# #below is the code for printing the values with NONE items.
# # popular=sixteen['Item'].value_counts()
# # popular.head(5)

# #Now we will first reset the index without droping any column and then change index to item to sort items into new datasets without NONE type of Items.
# sixteen.reset_index(inplace = True)
# items = sixteen.set_index(['Item'])
# NewItems= items.drop(['NONE'])
# NewItems.reset_index(inplace = True)

# #after reseting the index, we will count the items and print the top 5 items occuring.
# popular=NewItems['Item'].value_counts()


items = data.set_index(['Item'])
NewItems= items.drop(['NONE'])
NewItems.reset_index(inplace = True)

lol= NewItems.loc[NewItems['year'] == 2016]


#after reseting the index, we will count the items and print the top 5 items occuring.
popular=lol['Item'].value_counts()
print("Top 5 Items sold in 2016: \n")
print(popular.head())

popular.head().plot(kind='bar', color='red')

plt.show()

# %%
