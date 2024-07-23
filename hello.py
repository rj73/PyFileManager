import os
import shutil


audio=[".mp3", ".wma", ".aac"]
video=[".mp4"]
document=[".docx", ".pdf"]
software=[".exe",".apk"]
images=[".jpg", ".png"]

path="C:\\Users\\Rajesh Lap\\Desktop\\testing"

files=os.listdir(path)


# //make new folder or make directory ....once it created and you try to run again
# // you will get error cause it doesnt recreate
os.mkdir(path+"\\"+"audio")
os.mkdir(path+"\\"+"video")
os.mkdir(path+"\\"+"document")
os.mkdir(path+"\\"+"software")
os.mkdir(path+"\\"+"images")
os.mkdir(path+"\\"+"unkwon")


for file in files:
    extension= os.path.splitext(file)[1]
    print(extension)
    if extension=="":
        files1= os.listdir(path+"\\"+file)
        for file1 in files1:
            ext= os.path.splitext(file)[1]
            newpath=path+"\\"+file+"\\"
            if ext in audio:
                shutil.move(newpath +file1, path+"\\"+"audio")
            elif ext in video:
                shutil.move(newpath +file1, path+"\\"+"video")
            elif ext in document:
                shutil.move(newpath +file1, path+"\\"+"document")
            elif ext in software:
                shutil.move(newpath +file1, path+"\\"+"software")
            elif ext in images:
                shutil.move(newpath +file1, path+"\\"+"images")
            else:
                shutil.move(newpath +file1, path+"\\"+"unknown")

    elif extension in audio:
        shutil.move(path + "\\" +file, path+"\\"+"audio")
    elif extension in video:
        shutil.move(path + "\\" +file, path+"\\"+"video")
    elif extension in document:
        shutil.move(path + "\\" +file, path+"\\"+"document")
    elif extension in software:
        shutil.move(path + "\\" +file, path+"\\"+"software")
    elif extension in images:
        shutil.move(path + "\\" +file, path+"\\"+"images")
    else:
        shutil.move(path + "\\" +file, path+"\\"+"unknown")
        

print(files)