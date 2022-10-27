import pyautogui
import time
import shutil
import os


st = time.time()
##############################################

def main():
    path =  str(input("Enter path: ").strip())
    newFile = str(input("Enter the name: ").strip())
    qty = int(input("Enter the number of copy: "))
    images, root = getFiles(path)
    rename_n_copyFile(newFile, qty, root, images)

def getFiles(path):
    img = []
    for root, dirs, files in os.walk(path):
        for name in files:
            img.append(name)
    return img, root
    
def rename_n_copyFile(newFile, qty, root, images):
    renamedImages = []
    if (len(images) >= 100 and qty >= 11) or qty >= 100 :
        print("Sorry buddy, you don't wanna crash your computer and torture harddrive.")
        return
    
    for i in range(0,len(images)):
        oldImage = root + "\\" + images[i]
        temp , ext = images[i].split(".")
        m = newFile + str(i) + "." + ext
        renamed = root + "\\" + m
        renamedImages.append(m)
        os.rename(oldImage, renamed)
 
    for img in renamedImages:
        oldName = root + "\\" + img
        for j in range(0,qty+1):
            n = img.replace(".", f'-{j}.')
            newName = root + "\\" + n
            shutil.copyfile(oldName, newName)


if __name__ == "__main__":
    main()

    

#############################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
