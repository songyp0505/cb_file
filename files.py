import os
import shutil

# 获取该目录下的所有文件
currentPath = os.getcwd()
files = os.listdir(currentPath)

# 遍历每个文件
for file_name in files:
    # 检查文件名是否符合年月日的格式
    if file_name.endswith('.pdf') and len(file_name) >= 10:
        year = file_name[:4]
        month = file_name[5:7]
        
        # 创建目标目录（如果不存在的话）
        target_directory = os.path.join(source_directory, year, month)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        
        # 文件的原始路径
        source_file_path = os.path.join(source_directory, file_name)
        
        # 文件的目标路径
        target_file_path = os.path.join(target_directory, file_name)
        
        # 移动文件
        shutil.move(source_file_path, target_file_path)

# 完成分类
print("Files have been sorted.")
