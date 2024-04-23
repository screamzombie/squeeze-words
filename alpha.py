import re
import os
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
stopwords = ['a', 'b', 'c', 'd']


class controller:
    def __init__(self):  # * 初始化
        self.stop_words = []
        self.paper_list = []
        self.root_data_path = "./data"
        self.read_data()

    
    def return_paper_all_content(self, index):  # * 得到对应索引的内容
        if index <= len(self.paper_list):
            return self.paper_list[index].all_content
        else:
            print("index out of range")

    def show_all_years_freq(self): # * 获得所有年份的词汇频率ï
        total_content = ""
        for exam in self.paper_list:
            total_content += exam.all_content
        ans = self.word_frequency_analysis(total_content)
        for word, freq in ans:
            print(word, ":", freq)
        print(len(ans))

    def run(self):
        example = self.word_frequency_analysis(self.paper_list[0].all_content)
        for word, freq in example:
            print(word, ":", freq)

    def word_frequency_analysis(self, content):  # * 计算词频
        words = re.findall(r'\w+', content.lower())
        words_clean = []
        for word in words:
            if word not in stopwords and word.isdigit() == False and len(word) > 1:
                words_clean.append(word)

        word_freq = {}
        for word in words_clean:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        # 按词频降序排序
        sorted_freq = sorted(
            word_freq.items(), key=lambda x: x[1], reverse=False)
        return sorted_freq  # * 返回词频字典

    def read_data(self):
        files = os.listdir(self.root_data_path)  # * 得到文件夹下的所有文件名称
        files.sort()
        print(files)
        for i in files:
            alone_path = self.root_data_path + "/"+i
            sector_path = []
            for a in os.listdir(alone_path):
                sector_path.append(alone_path+"/"+a)
            sector_path.sort()
            print(sector_path)
            p = paper()
            p.year = i
            alone_path = "./data/"+i
            sector_path = []
            for a in os.listdir(alone_path):
                sector_path.append(alone_path+"/"+a)
            sector_path.sort()
            with open(sector_path[0], "r", encoding="utf-8") as f:
                p.read_content_a = f.read()
            with open(sector_path[1], "r", encoding="utf-8") as f:
                p.read_content_b = f.read()
            with open(sector_path[2], "r", encoding="utf-8") as f:
                p.read_content_c = f.read()
            with open(sector_path[3], "r", encoding="utf-8") as f:
                p.complete_content = f.read()
            with open(sector_path[4], "r", encoding="utf-8") as f:
                p.read_content_d = f.read()
            with open(sector_path[5], "r", encoding="utf-8") as f:
                p.translate_content = f.read()

            p.join_all_content()
            self.paper_list.append(p)


class paper:
    def __init__(self):
        self.year = None
        self.read_content_a = None  # * 阅读1
        self.read_content_b = None  # * 阅读2
        self.read_content_c = None  # * 阅读3
        self.read_content_d = None  # * 阅读4
        self.complete_content = None  # * 完形
        self.translate_content = None  # * 翻译
        self.all_content = ""  # * 整张试卷的所有内容
        self.dict_freq_all = {}  # * 所有内容的频率字典
        self.dict_freq_read = {}  # * 仅仅是阅读的频率

    def join_all_content(self):  # * 把所有内容合并到一起
        self.all_content = self.read_content_a + self.read_content_b + \
            self.read_content_c + self.read_content_d + \
            self.complete_content + self.translate_content
        # print(self.all_content)


if __name__ == "__main__":
    c = controller()
    # print(len(c.paper_list[0].all_content))
    # print(len(c.paper_list[2].all_content))
    c.show_all_years_freq()
