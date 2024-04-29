import os
import pandas as pd
import random


class dictionary:
    def __init__(self):
        self.dict_list = []
        self.diction_path = "../data/userData/dictionary.csv"
        self.import_dict()

    def import_dict(self):
        temp = pd.read_csv(self.diction_path, header=None)
        self.dict_list = temp.values.tolist()

    def return_word_value(self, literal):
        for word in self.dict_list:
            if word[0] == literal:
                return word[1]
        return None


class slave:
    def __init__(self):
        self.dict = dictionary()
        self.stopwords = []
        self.target_learn_list = []
        self.target_learn_path = "../data/tempData/all_years_words_freq.csv"
        self.not_in_dict_list = []
        self.ready_to_learn_list = []

    def load_stopwords(self):
        with open("../data/userData/grasp.txt", "r", encoding="utf-8") as f:
            self.stopwords = f.read().split("\n")

    def load_target_learn_list(self):
        if self.target_learn_path != None:
            df = pd.read_csv(self.target_learn_path, header=None)
            self.target_learn_list = df.values.tolist()
        else:
            print("文件不存在")

    def select_learn_target(self):
        ls = os.listdir("../data/tempData")
        clear_ls = []
        for i in ls:
            if i.endswith(".csv"):
                clear_ls.append(i)
        clear_ls.sort()
        cnt = 0
        for i in clear_ls:
            print(cnt, " ", i)
            cnt += 1
        select = int(input())
        self.target_learn_path = "../data/tempData/" + clear_ls[select]

    def make_learn_list(self):
        self.ready_to_learn_list.clear()
        for word in self.target_learn_list:
            if word[0] in self.stopwords or word[0] in self.not_in_dict_list:
                continue
            else:
                combination = []
                combination.append(word[0])
                combination.append(self.dict.return_word_value(word[0]))
                combination.append(word[1])
                self.ready_to_learn_list.append(combination)

    def detection(self):
        cnt = 0
        for word in self.target_learn_list:
            if word[0] in self.stopwords:
                continue
            if self.dict.return_word_value(word[0]) == None:
                self.not_in_dict_list.append(word[0])
                cnt += 1
        print("共有", cnt, "个单词搜索不到")

    def append_grasp(self, literal):
        if literal not in self.stopwords:
            with open("../data/userData/grasp.txt", "a") as f:
                f.write(literal+"\n")

    def return_words_random(self):
        index = random.randint(0, len(self.ready_to_learn_list)-1)
        return self.ready_to_learn_list[index]

    def return_learn_list(self):
        return self.ready_to_learn_list

    def default_loading(self):
        self.load_stopwords()
        self.load_target_learn_list()
        self.detection()
        self.make_learn_list()


if __name__ == "__main__":
    s = slave()
    s.load_stopwords()
    s.load_target_learn_list()
    s.detection()
    s.make_learn_list()
    print(s.ready_to_learn_list[21])
    s.append_grasp("hello")
    print(s.stopwords)
