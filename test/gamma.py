import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("../data/userData/dictionary.csv", header=None)
    print(df.head())
