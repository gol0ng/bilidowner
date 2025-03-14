import glob
import os

# 指定要操作的目录路径
directory = "./"

# 使用glob模块匹配目录下所有的.mp4文件，并返回一个列表
mp4_files = glob.glob(os.path.join(directory, "*.mp4"))

# 遍历找到的所有.mp4文件，并使用os.remove()函数删除它们
for file in mp4_files:
    os.remove(file)
    print(f"Deleted: {file}")