import time

## timer times initiation
seconds = 0
minutes = 0
hours = 0

while True:         # Stopwatch loop
    time.sleep(1)
    seconds += 1
    if seconds == 60:   #resets for each minute
        seconds = 0
        minutes += 1
    if minutes == 60:   #resets for each hour
        minutes = 0
        hours += 1


    allottedTime = f"H: {hours} M: {minutes} S:{seconds}"
    print(allottedTime)

    ## Below is outputting to a file for battery test, can remove or comment out post-test

    batteryTestOutputFile = open("batterytest.txt", "w")
    batteryTestOutputFile.write(allottedTime)


