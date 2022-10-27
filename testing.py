import pandas
from scipy.io import arff

dataset = arff.loadarff('ames_housing.arff')
data = pandas.DataFrame(dataset[0])


#data.describe()
#data.head()

for i in data.loc[:, ~data.columns.isin(data._get_numeric_data())]:
    print()
    print(data[i].value_counts())

    fig, axs = plt.subplots()
    axs.plot(data[i], data['Sale_Price'], 'o', alpha=0.2)
    axs.set_xlabel(i)
    axs.set_ylabel('Sale_Price')