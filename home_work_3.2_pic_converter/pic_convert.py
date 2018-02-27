
import glob
import os.path
import subprocess


# Пример использования для нашей задачи:
# sips --resampleWidth 200 myphoto.jpg


fullpath = os.path.abspath(os.path.dirname(__file__))
files = glob.glob(os.path.join(fullpath, 'Source', "*.jpg"))
subprocess.Popen(['mkdir', 'res'])

for file in files:
    print(file)
    subprocess.Popen(['sips', '--resampleWidth', '200', file, '--out', 'res/'])
