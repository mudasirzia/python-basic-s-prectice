#

# ---<<( Get IP by Hostname )>>---
import socket as s

import time as t

from tqdm import tqdm

#
get_hostname_from_user = input("Enter a Website URL (e.g., google.com):\t")
#
#
try:
    #
    # downloader baar
    for i in tqdm(range(5)):
        t.sleep(0.08)

    ip = s.gethostbyname(get_hostname_from_user)
    #
    #
    print(f"The ip address of {get_hostname_from_user} is: {ip}")

except s.gaierror:
    #
    #    t.sleep(0.5)
    print("Error!!!")
