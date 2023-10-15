import os
import shutil

source="/Users/mahendergadipally/Downloads/abc"
destination="/Users/mahendergadipally/Desktop"
list_of_files = os.listdir(source)
print(list_of_files)
for i in list_of_files:
    name,ext=os.path.splitext(i)
    if ext=="":
        continue
    if ext in ['.txt', '.doc', 'docx', '.pdf']:
        path1=source + "/" + i
        path2=destination + "/" + "document_files"
        path3=destination + "/" + "document_files" + "/" + i
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("creating and moving")
            shutil.move(path1,path3)