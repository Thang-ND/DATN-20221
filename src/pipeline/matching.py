import pandas as pd
import os
import glob
import numpy as np
import strsimpy
print('setup done!')
import hashlib
from tqdm import tqdm


def load_data(path):
    #path = os.getcwd()
    path = os.path.join(path, '*.csv')
    print(path)
    csv_files = glob.glob(path)
    print(len(csv_files))
    df = pd.read_csv(csv_files[0])
    for i, file in enumerate(csv_files):
        if i == 0:
            continue
        tmp = pd.read_csv(file)
        df = pd.concat([df, tmp], axis=0)
    return df
if __name__ == "__main__":
    path = '../data/production'
    df = load_data(path)
    df = df.drop(['Unnamed: 0'], axis=1)
    print(df.columns)