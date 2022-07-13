"""
Code for if the Disk  exists

"""


import shutil



hasDisk = False

disk = input('DISK : ')

try:
    diskLabel = disk + ':\\'
    total, used, free = shutil.disk_usage(diskLabel)

    #print(total)
    #print(used)
    #print(free)

    hasDisk = True
    
except:

    hasDisk = False

print(hasDisk)