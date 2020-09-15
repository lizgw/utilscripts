#!/bin/bash
#   Filename:       pangpui_fix.sh
#   Author:         Liz Wigglesworth
#   GitHub:         https://github.com/lizgw/utilscripts
#   Date:           1st September 2020
#   Version:        1.0
#   
#   Description:
#       Finds duplicate PanGPUI processes and kills the extra ones
#       so only one is left running. A quick alternative to messing
#       around in the task manager GUI.
#
#       This exists because either the PanGPUI Linux client sucks
#       and likes to start itself multiple times when I turn on
#       my computer or something about my computer is making it
#       act strangely. (It's probably both.)

echo "Counting PanGPUI processes..."
# get the pangpui processes running
# we get rid of the last line because that's our grep command process
ps -ax | grep PanGPUI | head -n -1 > /tmp/pangpui_ps.txt

# check how many lines we have - that's how many PanGPUI processes we have
num_ps=`cat /tmp/pangpui_ps.txt | wc -l`
if [ $num_ps -lt 2 ]
    then
        echo "There aren't multiple instances of PanGPUI running, no need to do anything."
        # cleanup
        rm /tmp/pangpui_ps.txt
        exit
fi

# there are at least 2 processes running, so we need to kill all but the first one
echo "Multiple ($num_ps) PanGPUI processes found, eliminating the duplicates..."

# trim whitespace & get the process ids from the file we saved
pids=`cat /tmp/pangpui_ps.txt | sed -e 's/^[ \t]*//' | cut --fields 1 --delimiter=' ' --output-delimiter=$'\t'`
# keep the first process running - remove it from our list of things to kill
pids=`echo $pids | cut -f 2- --delimiter=' '`
# kill the remaining ones
for id in $pids
do
    echo "Killing process $id..."
    kill -9 $id
done
# cleanup
rm /tmp/pangpui_ps.txt
echo "Done!"
