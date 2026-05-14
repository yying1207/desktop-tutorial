import os
import datetime

directory = '/Users/yingying/workspace/tmp_project/desktop-tutorial/Python'

# Rename
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        new_name = filename.replace('old_', 'new_')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

# Delete
threadhold_date = datetime.datetime(2023, 10,1)

for filename in os.listdir(directory):
    filePath = os.path.join(directory, filename)
    if os.path.isfile(filePath) and os.path.getmtime(filePath) < threadhold_date.timestamp():
        os.remove(filePath)