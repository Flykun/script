'''
显示文件的信息
适用于python3
仅仅适用于文件, 不能查找目录
可外接于json
'''

import os
import sys
import stat
import time

try_count = 16

while try_count:
    file_name = input("输入文件名: ")  # 选择文件
    f_hand = open(file_name)  # 打开文件
    count = 0
    for lines in f_hand:
        count = count + 1
    f_hand = open(file_name)
    inp = f_hand.read() # 读取文件
    t_char = len(inp) # 显示文件行数
    try_count >>= 1  # 移位运算
    try:
        file_stats = os.stat(file_name)  # 在给定的路径上执行一个系统 stat 的调用。
        print("系统调用", file_stats)
        break
    except OSError:
        print("\nNameError : [%s] 找不到文件!!!\n", file_name)

if try_count == 0:
    print("超过最高次数 \n退出系统")
    sys.exit()

# 文件信息
file_info = {
    'fname': file_name,
    'fsize': file_stats[stat.ST_SIZE],
    'f_lm': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_MTIME])),
    'f_la': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_ATIME])),
    'f_ct': time.strftime("%d/%m/%Y %I:%M:%S %p",
                          time.localtime(file_stats[stat.ST_CTIME])),
    'no_of_lines': count,
    't_char': t_char
}

print("\n文件名 =", file_info['fname'])
print("文件大小 =", file_info['fsize'], "bytes")
print("最后改动时间 =", file_info['f_lm'])
print("最后访问时间 =", file_info['f_la'])
print("创建时间 =", file_info['f_ct'])
print("总行数: ", file_info['no_of_lines'])
print("总字符数: ", file_info['t_char'])

