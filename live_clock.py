#           < === ---: Live Clock :--- === > 
import time as t
# 
# 
import datetime as dt
# 
# 
from colorama import Fore,Style
# 
# 
# 
# 
while True:
    current_time = dt.datetime.now()

    exact_time = current_time.strftime(f"{Fore.CYAN}{"%I"}:{Fore.GREEN}{"%M"}:{Fore.MAGENTA}{"%S"} {Fore.YELLOW}{"%p"}{Style.RESET_ALL}")
    
    print(f"\r{Fore.BLACK}Current Time:{exact_time}", end="" , flush=True)

    t.sleep(1)
