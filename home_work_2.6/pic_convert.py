
import glob
import os.path
import subprocess
import sys

# Пример использования для нашей задачи:
# sips --resampleWidth 200 myphoto.jpg

def create_file_list():  # return [list] with file names
    fullpath = os.path.abspath(os.path.dirname(__file__))
    # print(fullpath)
    files = glob.glob(os.path.join(fullpath, 'Source', "*.jpg"))
    # print(files)
    return files


for file in create_file_list():
    subprocess.popen('sips --resampleWidth 200 ' + file)
    # rs.args += ['--resampleWidth', 200, file]




# subprocess.run('ping yandex.ru')