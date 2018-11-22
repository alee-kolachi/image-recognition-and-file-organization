import face_recognition
import sys
import os
import os, fnmatch
import shutil
from pathlib import Path
from os import path    

def method(imagePath,folderPath,folderName):
    imagePath = face_recognition.load_image_file(''+imagePath)
    imagePath_encoding = face_recognition.face_encodings(imagePath)[0]
    listOfFiles = os.listdir(folderPath)  
    pattern = "*.jpg"
    for i in listOfFiles:
        if fnmatch.fnmatch(i, pattern):
            anyImage = face_recognition.load_image_file(''+folderPath + "\\" + i)
            unknown_face_encoding = face_recognition.face_encodings(anyImage)
            results = face_recognition.compare_faces(imagePath_encoding, unknown_face_encoding)
            newpath = folderPath + "/" + folderName
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            if True in results:
                src = folderPath + "/" + i
                shutil.copy(src,newpath)
    list = os.listdir(newpath) # dir is your directory path
    number_files = len(list)
    if number_files == 0:
        f= open(newpath + "/" + "Ooops.txt","w+")
        f.write("There were no images that matched the image you provided!!!")

    