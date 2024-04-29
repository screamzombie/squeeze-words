import pandas as pd
import pymysql
import os
from requests import head
from sqlalchemy import create_engine


class dataset:
    def __init__(self):
        self.db = pymysql.connect(
            host="127.0.0.1",
            database="squeeze",
            user="root",
            password="",
            port=3306,
            charset='utf8'
        )
        self.engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/squeeze")
        self.all_words_list = []

    def import_data(self, data_path="../data/tempData/all_years_words_freq.csv"):
        if os.path.exists(data_path):
            dataForm = pd.read_csv(data_path, header=None)
            self.all_words_list = dataForm.values.tolist()
        else:
            print("文件不存在")

    def storage_all_freq_sql(self):
        table_name = 'all_years_freq'
        df = pd.DataFrame(self.all_words_list)
        df.columns = ['word', 'freq']
        df.to_sql(table_name, self.engine, index=False, if_exists='replace')
        print('导入成功...')

    def establish_db(self):
        # for index in self.all_words_list:
        pass  
    
    def test(self):
        table_name = 'xmx'
        data_path = "../data/tempData/all_years_words_freq.csv"

        data = pd.read_csv(data_path, encoding='utf-8', header=None)
        data.columns = ['word', 'freq']
        print(data)
        engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/squeeze")
        data.to_sql(table_name, engine, index=False, if_exists='replace',)
        print('导入成功...')

    def test_dic(self):
        # print (dictionary.meaning("code"))
        pass


if __name__ == "__main__":
    a = dataset()
    a.import_data()
    # a.test()
    a.storage_all_freq_sql()
