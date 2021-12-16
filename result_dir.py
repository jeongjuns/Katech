import shutil
import os
from tqdm import tqdm
from pathlib import Path

path = 'outputs/'
dst = './result/'

file_list = os.listdir(path)

for f in file_list:
    full_name = f
    img_name = f.split('_')
    idx = img_name[-1]#[:-4]
    folder_name = img_name[1] + '_' + img_name[2]
    sub_name = img_name[0]
    result_name = img_name[0] + '_result'
    
    if not os.path.exists(dst + folder_name + '/' + sub_name):
        os.makedirs(dst + folder_name + '/' + sub_name)
        
    if not os.path.exists(dst + folder_name):
        os.makedirs(dst + folder_name)
    result_path = dst + folder_name + '/' + result_name

    if not os.path.exists(result_path):
        os.makedirs(result_path)
    
    shutil.copyfile(os.path.join(path, full_name), os.path.join(dst, folder_name, result_name, full_name))


print(full_name)    #2_20200615_140701_004740_v001_1.xml
print(idx)   #1.xml
print(folder_name)  #20200615_140701
print(sub_name) #2_result
  
