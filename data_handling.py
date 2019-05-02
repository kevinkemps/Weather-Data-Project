import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pandas import Series, DataFrame


def series_ex():
    series_obj = Series(np.arange(8), index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8'])
    print(series_obj[series_obj > 6])
    series_obj['row1', 'row5'] = 8
    print(series_obj)


def random():
    np.random.seed(25)
    DF_obj = DataFrame(np.random.rand(36).reshape((6, 6)), index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6'],\
                       columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6'])
    print(DF_obj.loc[['row1', 'row4'], ['c2', 'c3']])
    print(DF_obj['row2': 'row5'])
    print(DF_obj < .2)


def missing_val():
    missing = np.nan
    series_obj = Series(['row1', 'row2', missing, 'row4'])
    print(series_obj.isnull())
    np.random.seed(25)
    DF_rand = DataFrame(np.random.randn(36).reshape(6, 6))
    DF_rand.iloc[3: 6, 0] = missing
    DF_rand.iloc[1: 4, 5] = missing
    print(DF_rand.fillna(0))
    filled_DF = DF_rand.fillna({0: .1, 5: 1.25})
    ffill = DF_rand.fillna(method='ffill')
    print(DF_rand.isnull().sum())
    pass


def concat():
    DF_obj = DataFrame(np.arange(36).reshape(6, 6))
    DF_obj2 = DataFrame(np.arange(15).reshape(3, 5))
    #print(DF_obj, '\n', DF_obj2)
    print(pd.concat([DF_obj2, DF_obj]))
    seires_obj= Series(np.arange(6))
    seires_obj.name = "added"
    print(DF_obj.join(seires_obj).sort_values(by=[5], ascending=['False']))


def cars():
    address = r'C:\Users\KJones.pc\Documents\vscode\Data course\Ex_Files_Python_Data_Science_EssT\Ex_Files_' \
              r'Python_Data_Science_EssT\Exercise Files\Ch01\01_05\mtcars.csv'
    cars = pd.read_csv(address)
    #print(cars.head(5))
    cars_groups = cars.groupby(cars['cyl'])
    print(cars_groups.groups)
    print(cars_groups.get_group(8))
    print('mean:', cars_groups.mean())
    df = cars[['cyl', 'wt', 'mpg']]
    df.plot()
    df.plot(kind='bar')
    plt.show()


def line_chart():
    #%matplotlib inline
    rcParams['figure.figsize'] = 5, 4
    sb.set_style('whitegrid')
    x = range(1, 10)
    y = [1, 2, 3, 4, 5, 3, 2, 4, 8]
    plt.plot(x, y)
    plt.show()


def charts2():
    rcParams['figure.figsize'] = 5, 4
    x = range(1, 10)
    y = [1, 2, 3, 4, 5, 3, 2, 4, 8]

    fig = plt.figure()
    ax = fig.add_axes([.1, .1, .8, .9])
    ax.set_xlim([1, 9])
    ax.set_ylim([0, 5])
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_yticks([0, 1, 2, 3, 5])
    ax.plot(x, y)
    plt.show()


def sub_plt():
    rcParams['figure.figsize'] = 5, 4
    x = range(1, 10)
    y = [1, 2, 3, 4, 5, 3, 2, 4, 8]
    #fig = plt.figure()
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x)
    ax2.plot(x, y)
    plt.show()

def main():
    cars()

    pass


if __name__ == '__main__':
    main()

