import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


def get_splits(tree_clf):
    splits = np.array(tree_clf.tree_.threshold)

    splits = splits[splits != -2]
    splits = splits.tolist()
    splits.append(np.Inf)
    splits.append(-np.inf)
    splits.sort()

    return splits

def create_cut_and_dummies(dataset, col, splits):
    col_cat = f'{col}_cat'

    dataset[col_cat] = pd.cut(dataset[col], splits)
    return pd.get_dummies(dataset, columns=[col_cat], prefix=[col_cat])

def hist_plot(dataset, f_size=(10, 5)):
    plt.figure(figsize=f_size)
    sns.histplot(data=dataset, kde=False, bins=50)
    plt.plot()

def scatter_plot(x, y, f_size=(5, 3)):
    plt.figure(figsize=f_size)
    sns.scatterplot(x=x, y=y)
    plt.plot()

def hist_plot_compare(x1, x2, x1_title, x2_title):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 45), layout='constrained')

    sns.histplot(x1, ax=axes[0], bins=50).set(title=x1_title, xlabel="")
    sns.histplot(x2, ax=axes[1], bins=50).set(title=x2_title, xlabel="")

    plt.show()

def rename_cols_for_lgbm(dataset):
    return dataset.rename(columns = lambda x: re.sub('[^A-Za-z0-9_]+', 'X', x))

def get_calcofi_original_cols():
    return sorted(calcofi_original_cols)

def get_lots_of_nan_cols():
    return sorted(lots_of_nan_cols)

def get_without_nan_cols(columns):
    without_nan_cols = list(set(columns) - set(get_lots_of_nan_cols()))
    return sorted(without_nan_cols)

# 'without' NaN, strictly speaking, as we're leaving here the columns with ~20% missing values
def get_originals_without_nan_cols():
    return sorted(list(set(get_calcofi_original_cols()) - set(get_lots_of_nan_cols())))

calcofi_original_cols = [
        'R_SVA',
        'R_SALINITY',
        'R_PHAEO',
        'R_PRES',
        'R_NO3',
        'R_NO2',
        'Lat_Dec',
        'R_Depth',
        'R_CHLA',
        'R_DYNHT',
        'Lon_Dec',
        'R_O2',
        'R_NH4',
        'R_SIGMA',
        'R_PO4',
        'R_O2Sat',
        'R_SIO3'
    ]

lots_of_nan_cols = [
    'R_NH4',
    'R_PHAEO',
    'R_CHLA',
    'R_NO2',
    'R_NO3',
    'R_SIO3',
    'R_PO4',
]

random_seed = 2024

target_feature = 'R_TEMP'