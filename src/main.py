# from panel import *
from calculate import *
from operater import *

if __name__ == '__main__':
    c = controller()
    c.default_run()
    s = slave()
    s.default_loading()
    select = "start"
    print("输入q退出")
    while True:
        # select = input()
        if select != "q":
            word = s.return_words_random()
            print(word[0], "   ", "1 熟识 2 不认识 3查看释义 4 下一个")
            select = input()
            if select == "1":
                s.append_grasp(word[0])
            elif select == "3":
                print(word)
        elif select == "q":
            break
