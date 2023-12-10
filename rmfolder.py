import os
import re
import shutil

# 获取当前目录下所有文件夹
folder_list = [folder for folder in os.listdir() if os.path.isdir(folder)]

# 定义匹配的正则表达式
pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

# 删除匹配的文件夹
for folder in folder_list:
    if re.match(pattern, folder):
        folder_path = os.path.join(os.getcwd(), folder)
        try:
            shutil.rmtree(folder_path)
        except OSError as e:
            print(f"Error: {folder_path} : {e.strerror}")
