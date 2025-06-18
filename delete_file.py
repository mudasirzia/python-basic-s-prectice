#               < === --- : Deleting file script --- === >

import os
# 
# 
file_name = "scripts/camera_access.py"  # must give compelete location
# 
# 
if os.path.exists(file_name):
# 
    os.remove(file_name)
# 
    print(f"File {file_name} has been removes sucessfully!!!")
    
else:
    
    print(f"file {file_name} is not exists")


