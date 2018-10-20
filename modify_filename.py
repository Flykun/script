'''
批量修改文件名
仅适用于python3
'''
import os

dir = os.getcwd()  # 返回当前工作目录
subdir = os.listdir(dir)  # 返回指定路径下的文件和文件夹列表
for i in subdir:
    path = os.path.join(dir, i)  # 将目录和文件名合成一个路径
    if os.path.isdir(path):  # 判断是否是目录
        end_dir = os.listdir(path)
        for i in range(len(end_dir)):
            new_name = end_dir[i][0:50]
            os.rename(os.path.join(path, end_dir[i]),
                      os.path.join(path, new_name))  # 重命名
