def path_format(fileName):
    
    
    fileName = list(fileName)        
    
    for index in range(len(fileName)):
        if fileName[index] == '\\':
            fileName[index] = '/'
    
    
    fileName = ''.join(fileName)
    
    return fileName

def encrypt(fileName,key):
    
    
    fileName = path_format(fileName)
    
    file = open(fileName, 'rb')
    data = file.read()
    file.close()

    data = bytearray(data)

    for index, value in enumerate(data):
        data[index] = value ^ key # XOR ecrypt

    file = open(fileName, 'wb')
    file.write(data)
    file.close()

    print('SUCCESSFULY ENCRYPTED')

key = int(input("ASK FOR A KEY BETWEEN 1 - 255 : "))
fileName = input("PLEASE ENTER FILE NAME : ") # Has to be absolute path
encrypt(fileName, key)

#s = path_format('C:\Program Files\Google\Chrome')
#print(s)


