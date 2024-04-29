import requests
from bs4 import BeautifulSoup


class vocabulary:
    def __init__(self):
        self.english_value = None  # 英文
        self.chinese_values = []  # 中文释义
        self.freq_number = None  # 出现频率
        self.example_list = []  # 例句
        self.tags = []  # 标签

    def check_flag_in_tags(self, tag):  # 判断标签在不在这个标签表中
        if tag in self.tags:
            return True
        else:
            return False

    def look_up_by_youdao(self):
        try:
            self.chinese_values = []
            url = r"http://dict.cn/"+self.english_value
            r = requests.get(url, timeout=30).text
            recode = r.encode('utf-8')
            soup = BeautifulSoup(recode, "html.parser")
            # 爬取单词发音
            html = soup.find('bdo', lang="EN-US")
            if html is not None:
                phonetic = html.string
            # 爬取汉语语义
            html2 = soup.find("ul", class_="dict-basic-ul")
            if html2 is not None:
                meaning = html2.text.replace("\n", "")
                self.chinese_values.append(meaning)
        except Exception as exc:
            print(exc)


class dictSystem:
    def __init__(self):
        self.database = []  # 利用有道的接口建立本地数据库
        self.word_list = []  # * 准备查的单词列表
        self.open_word_csv = ""

    def reset_open_word_csv(self, new_open_path=None):
        if new_open_path != None:
            self.open_word_csv = new_open_path
        else:
            print("没有选择打开文件")

    def my_init(self):
        pass

    def make_database(self):
        pass
