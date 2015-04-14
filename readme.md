log-killer
a program that deletes the oldest log file
until enough disk space is full.

requirements:
python 2.7
psutil (pip install psutil)

the script takes 3 mandatory arguments:

log-killer.py [directory] [spacelimit] [ext]

directory:  the directory to look at for log files.  non-recursive.
spacelimit:  the space threshold for the disk, in a percentage.  whole numbers only.
ext:  the file extension to look at.  files that don't match this extension are ignored.

examples:

windows:
`python log-killer.py c:\logs 90 txt`
delete the oldest txt file stored in c:\logs until the disk is at or under 80% capacity.

linux:
`python log-killer.py /var/log 60 log`
delete the oldest log file stored in /var/log until the disk is at or under 60% capacity.