import os

file_path = "C:\\Users\\Administrator\\Downloads\\costume1.gif"

if os.path.exists(file_path):
    print("File exists:", file_path)
else:
    print("File does not exist:", file_path)
