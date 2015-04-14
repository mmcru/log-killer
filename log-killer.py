__author__ = 'crupi'

import psutil
import os
from sys import argv

#directory to look at
directory = str(argv[1])
#percentage to stop at
spacelimit = int(argv[2])
#log file extension
ext = str(argv[3])

print """
log killer engaged with the following settings:
directory: %s
hdd threshold (percentage): %s
log file extension: %s
""" % (directory, spacelimit, ext)

#initial count for number of deleted files
count = 0

#basic disk info to console
print "directory information for: %s" % directory
print "total size: %s bytes" % psutil.disk_usage(directory).total
print "used: %s bytes" % psutil.disk_usage(directory).used
print "free: %s bytes" % psutil.disk_usage(directory).free
print "percent total disk used: %s " % psutil.disk_usage(directory).percent
print ""

#find oldest file in directory
def oldest_file_in_tree(rootfolder, extension=".iso"):
    try:
        return min(
            (os.path.join(dirname, filename)
            for dirname, dirnames, filenames in os.walk(rootfolder)
            for filename in filenames
            if filename.endswith(extension)),
            key=lambda fn: os.stat(fn).st_mtime)
    except ValueError:
        print "directory has no files with extension %s" % extension

#loop until disk is under spacelimit
while psutil.disk_usage(directory).percent > spacelimit:
    oldest = oldest_file_in_tree(directory, ext)
    print "removing %s" % oldest
    os.remove(oldest)
    print "disk is now %s percent full" % psutil.disk_usage(directory).percent
    count += 1

if count > 0:
    print "finished!  deleted %s files under %s" % (count, directory)
else:
    print "finished... couldn't find any files that met the criteria, or the disk is already using less space than the specified threshold.  see readme.md for help."

print "disk is now %s percent full" % psutil.disk_usage(directory).percent