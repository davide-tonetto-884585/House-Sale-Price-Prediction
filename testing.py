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

def refineData(df):
    replace_kitch = {"Kitchen_Qual":{b'Poor': 0, b'Fair': 1, b'Typical': 2, b'Good': 3, b'Excellent': 4}}
    replace_uti = {"Utilities":{b'AllPub': 1, b'NoSewr': 2, b'NoSeWa':3}}
#                    "Land_Slope":{b'Gtl': 0, b'Mod': 1, b'Sev': 2}}
    new_data = df.replace(replace_data)
    new_data = new_data.replace(replace_uti)
    return new_data

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
