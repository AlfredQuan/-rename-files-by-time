#! python3
import os
#import exifread
#from datetime import datetime
from operator import itemgetter
from time import time

#def get_folders_and_files(target_folder):
#    for folder_name, subfolders, filenames in os.walk(target_folder):
#        return (subfolders, filenames)

def sort_by_day(folder, files):
    sort_dict = []
    for filename in files:
        if os.path.splitext(filename)[1] != '.py':
            try:
                #tags = exifread.process_file(picture)
                #time = tags['EXIF DateTimeOriginal']
                #date_time = datetime.strptime(str(time), '%Y:%m:%d %H:%M:%S')
                file = os.path.join(folder, filename)
                date_time = os.path.getmtime(file)
                list = [file, date_time]
                sort_dict.append(list)
            except:
                print('无法读取' + filename + '的时间')
    #print(sort_dict)
    sorted_files = []
    #assert()
    #print(sorted(sort_dict, key=itemgetter(1)))
    for i in sorted(sort_dict, key=itemgetter(1)):
        #print(i)
        sorted_files.append(i[0])
    #print(sorted_files)
    return sorted_files


def rename_files(folder, files):
    count = 0
    for file in files:
        new_name = os.path.join(folder, str(count) + os.path.splitext(file)[1])
        os.rename(file, new_name)
        print("正在重命名文件" + str(file))
        count += 1

def rename_folders(root, folders):
    count = 0
    for folder in folders:
        new_name = os.path.join(root, str(count))
        os.rename(folder, new_name)
        print("正在重命名文件夹" + str(folder))
        count += 1


for folder_name, subfolders, filenames in os.walk('.'):
    if len(subfolders) > 0:
        rename_folders(folder_name, subfolders)
    #print(folder_name)
    if len(filenames) > 0:
        sorted_pics = sort_by_day(folder_name, filenames)
        rename_files(folder_name, sorted_pics)
print("完成")





