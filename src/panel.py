import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('result/all_years_words_freq.csv',header=None,sep=' ',nrows=30)
    print(df.values.tolist())