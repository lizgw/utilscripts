# deversionify.py
# a script that removes all the annoying windows backup
# timestamps like this: (2018_03_24 02_25_02 UTC)
# from filenames so things stop breaking.
# run it in the directory you want to fix!!
# v1.0 - 05/21/19

import os
timestamp_start = " (2"
timestamp_end = "UTC)"

for root, dirs, files in os.walk("."):
    print("** SCANNING " + root)
    # print(files)
    for item in files:
            print("checking " + item + "...")
            old_name = item
            # find the part that's the timestamp (2018-01-blah blah blah...)
            date_start = old_name.find(timestamp_start)
            date_end = old_name.find(timestamp_end)
            # TODO eventually: add some more checks to this to ensure it's actually a windows backup timestamp
            if date_start != -1 and date_end != -1:
                # rename the file & cut out the timestamp
                new_name = old_name[:date_start] + old_name[date_end + len(timestamp_end):]
                os.rename(os.path.join(root, old_name), os.path.join(root, new_name))
                print("** RENAMED " + old_name + " to " + new_name)