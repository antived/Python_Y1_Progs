# AdAstra 2022-23 problem-3
# program to correct 12hr clock w/ AM/PM into 24hr clock for NASA
# - vedant dutta

def TimeCorrect(ampmFmtTime):
    # Split the am-pm format time into substrings for hours,
    # minutes, seconds (but seconds part will still include
    # 'AM' or 'PM' substring, which will have to be split-out
    # further in subsquent step
    hhMmSsChunks = ampmFmtTime.split(':')   # split by ":"
    hrs = int(hhMmSsChunks[0])          # HH
    mins = int(hhMmSsChunks[1])         # MM
    secsAmPm = hhMmSsChunks[2].split()      # split by space
    secs = int(secsAmPm[0])             # SS
    amPm = secsAmPm[1]                  # AM / PM

    # Convert to 24-hour format
    if (amPm == "PM" or amPm == "pm") and hrs != 12:
        hrs += 12
    elif (amPm == "AM" or amPm == "am") and hrs == 12:
        hrs = 0

    # Re-assemble the time string in 24-hour format
    return "{:02d}:{:02d}:{:02d}".format(hrs, mins, secs)

# main()

# Sample usage of TimeCorrect() function defined above
print("09:55:35 AM is corrected as " + TimeCorrect("09:55:35 AM"))
print("12:00:00 PM is corrected as " + TimeCorrect("12:00:00 PM"))
print("11:59:59 PM is corrected as " + TimeCorrect("11:59:59 PM"))
print("12:00:00 AM is corrected as " + TimeCorrect("12:00:00 AM"))
