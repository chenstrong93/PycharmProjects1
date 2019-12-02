import pandas as pd
from scipy.interpolate import lagrange
from sklearn.model_selection import train_test_split

inputfile = 'E:/PycharmProjects/6-1/missing_data.xls'
outputfile = 'E:/PycharmProjects/6-1/missing_data_processed.xlsx'

data = pd.read_excel(inputfile, header=None)


def ployinterp_columns(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


for i in data.columns:
    for j in range(len(data)):
        if data[i].isnull()[j]:
            data[i][j] = ployinterp_columns(data[i], j)

data.to_excel(outputfile, header=None, index=False)
