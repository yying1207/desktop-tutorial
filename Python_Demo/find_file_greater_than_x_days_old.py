import os
import datetime
current_time = datetime.datetime.now()
print(f"Current time: {current_time}")

# Search for files that created more than x days ago
x = 10
for dirpath, dirname, filename in os.walk("/etc"):
    for file in filename:
        comp_path = os.path.join(dirpath, file)
        file_stat = os.stat(comp_path)
        """ Example output of os.stat("/etc/hosts"):
        >>> os.stat("/etc/hosts")
        os.stat_result(st_mode=33188, st_ino=424482, st_dev=16777232, st_nlink=1, st_uid=0, st_gid=0, st_size=213, st_atime=1698965096, st_mtime=1698965096, st_ctime=1699791204)
        """
        file_ctime = file_stat.st_ctime
        file_creation_date = datetime.datetime.fromtimestamp(file_ctime)

        diff_in_days = (current_time - file_creation_date).days
        if diff_in_days > x:
            print(comp_path, diff_in_days)
            os.remove(comp_path) # add file operations here, such as os.remove() to delete the file, or os.rename() to rename the file, etc.