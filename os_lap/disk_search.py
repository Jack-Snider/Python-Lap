import shutil

def hasDisk(disk):

    
    """
    Code for if the Disk  exists

    parameter 'disk' => This 'hasDisk' function returns bool type,
                                      if the parameter 'disk' exists, it returns True and if it's not, it returns False

    -example use-

    hasDisk('c')  
    hasDisk('d')
    ...

    """
    answer = False

    try:
        diskLabel = disk + ':\\'
        total, used, free = shutil.disk_usage(diskLabel)

        #print(total)
        #print(used)
        #print(free)

        answer = True
        
    except:

        answer = False

    return hasDisk



disks = ['c','i','d','e','f']

for disk in disks:
    print(f'{disk} : {hasDisk(disk)}')


"""
-result-

c : True
i : True
d : False
e : False
f : False

"""
