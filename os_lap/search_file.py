import os

def getFiles(disk, extension):
    
    """
    
    parameter 'disk' => Disk for where you would like to search (entire branches)
    parameter 'extension' => file extension which you would like to search (ex : .txt , .jpg, .png ...)

    so the example parameters you can insert would be like

    -example use-
    
    getFiles('c:\\', ['.txt'])
    getFiles('d:\\', ['.txt','.png'])
    getFiles('i:\\', ['.txt','.png','.jpg'])
    
    
    """

    # Sageguard password
    safeguard = input('PLEASE ENTER THE SAFEGUARD PASSWORD : ')
    if safeguard != 'start':
        quit()

    # Get file extension to search

    # Grab all files from the machine
    file_paths = []
    for root, dirs, files in os.walk(disk):
        for file in files:
            file_path, file_ext = os.path.splitext(root + '\\' + file)
            if file_ext in extension:
                file_paths.append(root + '\\' + file)
    
    for f in file_paths:
        print(f)   
    
    return file_paths
    
   
print('This is search file')
    

    
"""
os.walk()를 이용한 방법
위와 유사한 구현 내용을 os.walk()로 처리할 수 있다.

os.walk()는 하위의 폴더들을 for문으로 탐색할 수 있게 해줍니다. 인자로 전달된 path에 대해서 다음 3개의 값이 있는 tuple을 넘겨준다.

root : dir과 files가 있는 path
dirs : root 아래에 있는 폴더들
files : root 아래에 있는 파일들

"""    

files = getFiles('c:\\', ['.txt','.png'])
print(files)    
    