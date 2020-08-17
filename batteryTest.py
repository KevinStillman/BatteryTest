import time
import datetime
import os

SAVETOFILE = True

## timer times initiation
start = int(time.time())

while True:             # Stopwatch loop, Note: One full loop takes slightly longer than a second
    time.sleep(15)      # The output time will be updated every 15 seconds (Less CPU and disk usage)
    now = int(time.time())
    timePassed = str(datetime.timedelta(seconds=now-start))
    
    os.system('cls')    #Change this to 'clear' if on Linux, Disable this if being run in the Shell
    print(timePassed)

    ## Output to file

    if SAVETOFILE:
        with open("Time Before Shutdown.txt", "w") as file:
            file.write(timePassed)
