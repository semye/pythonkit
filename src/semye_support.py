import os

__version__ = '1.0'


def getyxy():
    """
    一个函数
    """
    support_logs("打印yxy")


def helloworld():
    """
    一个函数 函数与函数之间空两行
    """
    print("helloworld!")


def add(a, b):
    """
    一个普通的函数 计算两个数的值
    :param a:
    :param b:
    :return:
    """
    return a + b


def support_logs(text):
    print("当前文件名是:" + os.path.basename(__file__) + ";Log:" + text)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    else:
        print("hello")


class Employee:
    """
    所有员工的基类
    """

    def __init__(self):
        print("FUCK!")

    @staticmethod
    def count(hello):
        print(hello)


# 定义人类
class Human:

    def eat(self, name):
        print(name + "吃饭")
        pass

    def sleep(self):
        print("睡觉")
        pass
