import re
import os
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
stopwords = ['a', 'b', 'c', 'd']


class controller:
    def __init__(self):
        self.stop_words = []
        self.paper_list = []
        self.root_data_path = "./data"
        self.read_data()

    def storage_words_freq_by_year(self, year):
        for paper in self.paper_list:
            if paper.year == str(year):
                pass

    def return_paper_all_content(self, index):  # * get total content by index
        if index <= len(self.paper_list):
            return self.paper_list[index].all_content
        else:
            print("index out of range")

    def show_all_years_freq(self):  # * display all previous years words freq
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

    def word_frequency_analysis(self, content):  # * calculate freq
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

        # sort by frequency down
        sorted_freq = sorted(
            word_freq.items(), key=lambda x: x[1], reverse=False)
        return sorted_freq

    def read_data(self):
        files = os.listdir(self.root_data_path)
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
        self.read_content_a = None  # * read 1
        self.read_content_b = None  # * read 2
        self.read_content_c = None  # * read 3
        self.read_content_d = None  # * read 4
        self.complete_content = None  # * complate
        self.translate_content = None  # * translate
        self.all_content = ""  # * all content of this paper
        self.dict_freq_all = {}  # * a dict of all words freq
        self.dict_freq_read = {}  # * only read texts

    def join_all_content(self):  # * join all content
        self.all_content = self.read_content_a + self.read_content_b + \
            self.read_content_c + self.read_content_d + \
            self.complete_content + self.translate_content

    # * return this paper's all words freq
    def return_this_paper_all_words_freq(self):
        pass


if __name__ == "__main__":
    c = controller()
    c.show_all_years_freq()
