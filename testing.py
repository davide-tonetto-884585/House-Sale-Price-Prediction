import pandas
from scipy.io import arff
import matplotlib.pyplot as plt

dataset = arff.loadarff('ames_housing.arff')
data = pandas.DataFrame(dataset[0])
print(data.columns)

fig, axs = plt.subplots()
axs.plot(data['Street'], data['Sale_Price'], 'o', alpha=0.2)
axs.set_xlabel('Street')
axs.set_ylabel('Sale_Price')


#data.describe()
#data.head()

#for i in data.loc[:, ~data.columns.isin(data._get_numeric_data())]:
   # print()
   # print(data[i].value_counts())

   # fig, axs = plt.subplots()
 #   axs.plot(data[i], data['Sale_Price'], 'o', alpha=0.2)
  #  axs.set_xlabel(i)
    #axs.set_ylabel('Sale_Price')
#%%
