import os
import pandas as pd
import torch

def make_dir(path:str):
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    data_file = '../data/house_tiny.csv'
    make_dir('../data')
    with open(data_file, 'w') as f:
        f.write('NumRooms,Alley,Price\n')  # Column names
        f.write('1,Pave,127500\n')  # Each row represents a data point
        f.write('2,NA,106000\n')
        f.write('4,NA,178100\n')
        f.write('NA,NA,140000\n')

    data = pd.read_csv(data_file)
    print(data.isnull())
    print(data.isnull().sum(axis=0))
    print(data.dropna(thresh=2))
    print(len(data))
    max_null=max(data.isnull().sum(axis=0))
    data = data.dropna(axis=1,thresh=len(data)+1-max_null)
    print(data)

