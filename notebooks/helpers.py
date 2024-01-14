import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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