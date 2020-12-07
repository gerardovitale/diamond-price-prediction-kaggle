import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
plt.style.use('seaborn')

def open_csv(file_name_csv):
    path = f'../diamonds-datamad1020/{file_name_csv}'
    return pd.read_csv(path, index_col=[0])

def plotting_pair(df, file_name, hue=None, hue_order=None, palette='colorblind', markers=None):
    '''
    Create and save an image with a seaborn pairplot, giving a DataFrame and a file name.
    '''
    sns.pairplot(df, hue=hue, hue_order=hue_order, palette=palette, markers=markers)
    save_path = f'../images/{file_name}.png'
    plt.savefig(save_path)
    