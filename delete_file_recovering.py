import os
import shutil as s

#
file_name = "raf/google.py"

backup_file = "raf/dumy_new.py"

#
if os.path.exists(file_name):
    s.copy(file_name, backup_file)

    print(f"Copy File: {file_name}")

    # removing the dumy file

    os.remove(file_name)

    print(f"deleted file: {file_name}")

else:
    print("file is not found")

    # recover deleted file
if os.path.exists(backup_file):

    #  recover the actual file
    s.copy(backup_file,file_name)

    print(f"file copy: {backup_file}")

    # remove the backup file
    os.remove(backup_file)
else:
    print( FileNotFoundError)
