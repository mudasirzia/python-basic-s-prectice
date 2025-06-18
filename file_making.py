#                   < == ---: File making :--- === >


import os

#
import shutil as s

#
from itertools import count as c

os.makedirs("enter the directory", exist_ok=True)

if os.path.exists("enter the directory path"):
  
    with open(f"enter the file name with .py", "w") as file:
      
        pass

else:
  
    print("file not found")
