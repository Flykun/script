'''
查找目录, 如果目录不存在就创建目录
适用于python3
'''
from __future__ import print_function
import os


def main():
    CheckDir = input("请输入要查找的目录名: ")
    print()

    if os.path.exists(CheckDir):  # 检查文件是否存在
        print("目录存在")
    else:
        print("找不到" + CheckDir)
        print()
        os.makedirs(CheckDir)  # 创建新目录
        print("创建 " + CheckDir)
        print('创建成功')


if __name__ == '__main__':
    main()
