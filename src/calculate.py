from tools import *
import re
import os
import pandas as pd


class section:  # ! 章节
    def __init__(self):
        self.section_name = None
        self.section_content = None
        self.section_freq_dict = {}

    def set_this_freq_dict(self):
        self.section_freq_dict = get_freq_dict_by_content(
            self.section_content)

    def return_this_freq_dict(self):
        return self.section_freq_dict

    def set_this_section_content(self, content_path):
        with open(content_path, "r", encoding="utf-8") as f:
            self.section_content = f.read()

    def return_this_section_content(self):
        return self.section_content


class paper:  # ! 试卷
    def __init__(self):
        self.year = None
        self.section_list = []  # * 章节列表
        self.all_content = None  # * 所有内容
        self.all_freq_dict = {}  # * 本试卷全部的单词频率

    def set_all_freq_dict(self):
        self.all_freq_dict = get_freq_dict_by_content(self.all_content)

    def return_all_freq_dict(self):
        return self.all_freq_dict


class controller:
    def __init__(self):
        self.paper_list = []
        self.all_paper_content = ""
        self.all_paper_content_words_freq = {}

    def load_paper(self):
        paper_dir = os.listdir("../data/rawData")
        paper_dir.sort()
        for direct in paper_dir:
            p = paper()
            p.year = direct  # ? 设置试卷年份
            paper_path = "../data/rawData/"+direct
            section_dir = os.listdir(paper_path)
            section_dir.sort()
            paper_all_content = ""
            for section_index in section_dir:
                total_path = paper_path+"/"+section_index
                s = section()
                s.section_name = section_index
                s.set_this_section_content(total_path)
                s.set_this_freq_dict()
                paper_all_content += s.return_this_section_content()
                p.section_list.append(s)
            p.all_content = paper_all_content
            p.set_all_freq_dict()
            self.paper_list.append(p)
            self.all_paper_content += paper_all_content

    def calculate_freq_dict(self):
        self.all_paper_content_words_freq = get_freq_dict_by_content(
            self.all_paper_content)

    def storage_all_content_words_freq(self):
        df = pd.DataFrame(self.all_paper_content_words_freq)
        df.to_csv('../data/tempData/all_years_words_freq.csv',
                  index=False, header=None)

    def storage_words_freq_by_paper(self):
        for paper in self.paper_list:
            df = pd.DataFrame(paper.all_freq_dict)
            df.to_csv('../data/tempData/'+paper.year+'_words_freq.csv',
                      index=False, header=None)

    def create_paper_directory(self):
        for paper in self.paper_list:
            if not os.path.exists("../data/tempData/"+paper.year):
                os.mkdir("../data/tempData/"+paper.year)

    def storage_sections_words_freq(self):
        self.create_paper_directory()
        for paper in self.paper_list:
            for section in paper.section_list:
                df = pd.DataFrame(section.section_freq_dict)
                df.to_csv('../data/tempData/'+paper.year+'/'+section.section_name+'_words_freq.csv',
                          index=False, header=None)


if __name__ == '__main__':
    c = controller()
    c.load_paper()
    c.calculate_freq_dict()
    c.storage_all_content_words_freq()
    c.storage_words_freq_by_paper()
    c.create_paper_directory()
    c.storage_sections_words_freq()
