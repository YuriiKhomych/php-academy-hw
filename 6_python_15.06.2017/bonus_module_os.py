import os

abs_path_to_file = os.path.abspath(__file__)
list_dir = os.listdir()

print('All files in :', os.getcwd())
for file in list_dir:
    if os.path.isfile(file):
        print(file)

print('All folders in :', os.getcwd())
for folder in list_dir:
    if os.path.isdir(folder):
        print(folder)

# print(os.listdir(os.path.dirname(abs_path_to_file)))
