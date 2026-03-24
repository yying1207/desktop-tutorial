import os

directory = '/Users/yingying/workspace/tmp_project/desktop-tutorial/Python'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        new_name = filename.replace('old_', 'new_')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))