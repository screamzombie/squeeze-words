import requests
from bs4 import BeautifulSoup
import re


def read_lst():
    """读取wordlist.txt中的单词"""
    lst = []
    with open('wordlist.txt', encoding='utf-8') as f:
        lines = f.readlines()
        lst = [i.strip() for i in lines]
    return lst


def look_up(lst):
    """进行单词查询"""
    n = 1
    try:
        for i in lst:
            url = r"http://dict.cn/"+i
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
            with open("Wordmeaning.txt", "a+", encoding="utf-8") as f:
                f.write(f"{n}. "+i+phonetic+meaning+"\n")
                # f.write(s+"\n") #写入例句
            n += 1
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    uls = read_lst()
    look_up(uls)
