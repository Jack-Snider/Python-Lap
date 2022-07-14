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

        #print(f'------------ {disk} -------------')
        #print(total)
        #print(used)
        #print(free)
        #print('--------------------------')

        answer = True
        
    except:

        answer = False

    return answer


# a ~ z
disks = [chr(w) for w in range(ord('a'),ord('z') + 1)]

existsDisk = []

for disk in disks:
    print(f"{disk} : {hasDisk(disk)}")
    if(hasDisk(disk)):
        existsDisk.append(disk)

print(existsDisk)


