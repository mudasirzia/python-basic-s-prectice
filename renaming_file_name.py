#               < === --- : Renaming file script --- === >

import os

#
#
from colorama import Fore, Style

try:
    old_name = "enter the actual name of file/.py"  # give complete location to exact changing in it
    #
    new_name = "enter the new name you want of file /.py"
    #

    os.rename(old_name, new_name)

    #
    #
    print(
        f"old file name:{Fore.YELLOW}{old_name}{Style.RESET_ALL}\nnew file:{Fore.GREEN}{new_name}{Style.RESET_ALL}"
    )

except FileNotFoundError:

    print(f"file name {old_name} is not found!!!")

except Exception as e:

    print(f"Some error occcured: {e}")
