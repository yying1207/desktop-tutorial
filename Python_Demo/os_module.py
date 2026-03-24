import os

"""
for dirname, dirpath, filenames in os.walk('/Users/yingying/workspace/tmp_project/desktop-tutorial'):
    print(f'Directory: {dirname}')
    print(f'Path: {dirpath}')
    print('Files:')
    for filename in filenames:
        print(f' - {filename}')
    print()
"""

print("test")
print(list(os.walk('/Users/yingying/workspace/tmp_project/desktop-tutorial')))
