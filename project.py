#!/usr/bin/env python
# coding: utf-8

# # The Project #
# 1. This is a project with minimal scaffolding. Expect to use the the discussion forums to gain insights! It’s not cheating to ask others for opinions or perspectives!
# 2. Be inquisitive, try out new things.
# 3. Use the previous modules for insights into how to complete the functions! You'll have to combine Pillow, OpenCV, and Pytesseract
# 4. There are hints provided in Coursera, feel free to explore the hints if needed. Each hint provide progressively more details on how to solve the issue. This project is intended to be comprehensive and difficult if you do it without the hints.
# 
# ### The Assignment ###
# Take a [ZIP file](https://en.wikipedia.org/wiki/Zip_(file_format)) of images and process them, using a [library built into python](https://docs.python.org/3/library/zipfile.html) that you need to learn how to use. A ZIP file takes several different files and compresses them, thus saving space, into one single file. The files in the ZIP file we provide are newspaper images (like you saw in week 3). Your task is to write python code which allows one to search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza". This will test your ability to learn a new ([library](https://docs.python.org/3/library/zipfile.html)), your ability to use OpenCV to detect faces, your ability to use tesseract to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.
# 
# Each page of the newspapers is saved as a single PNG image in a file called [images.zip](./readonly/images.zip). These newspapers are in english, and contain a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB) and may take some time to work with, I would encourage you to use [small_img.zip](./readonly/small_img.zip) for testing.
# 
# Here's an example of the output expected. Using the [small_img.zip](./readonly/small_img.zip) file, if I search for the string "Christopher" I should see the following image:
# ![Christopher Search](./readonly/small_project.png)
# If I were to use the [images.zip](./readonly/images.zip) file and search for "Mark" I should see the following image (note that there are times when there are no faces on a page, but a word is found!):
# ![Mark Search](./readonly/large_project.png)
# 
# Note: That big file can take some time to process - for me it took nearly ten minutes! Use the small one for testing.

# In[8]:


import pytesseract
from PIL import Image
from zipfile import ZipFile 
import datetime 
import cv2 as cv
from PIL import ImageDraw, ImageFont
import numpy as np
import math

face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


# In[9]:


def get_faces(img):
    face_images = []
    cv_image = np.array(img) 
    cv_img = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(cv_img,1.3,5)
    for x,y,w,h in faces:
        cropped_face = img.crop((x,y,x+w,y+h))
        cropped_face.thumbnail((100,100))
        face_images.append(cropped_face)
    return face_images


# In[10]:


def make_sheet(cropped_faces):
    h = math.ceil(len(cropped_faces)/5)
    contact_sheet = Image.new('RGB',(500,h*100))
    x, y = 0,0
    for face in cropped_faces:
        contact_sheet.paste(face,(x,y))
        x, y = (0,y+100) if x == 400 else (x+100,y)
    return contact_sheet


# In[3]:


image_info = []
file_name = "readonly/images.zip"
with ZipFile(file_name, 'r') as zip: 
    zip.extractall()
    for info in zip.infolist():
        info_dict = {}
        filename = info.filename
        info_dict['name'] = filename
        img = Image.open(filename).convert('RGB')
        
        # store text
        info_dict['text'] = pytesseract.image_to_string(img)
        
        cropped_faces = get_faces(img)
        # store face_num
        info_dict['face_num'] = len(cropped_faces)
        
        # store contact_sheet
        if len(cropped_faces)>0:
            info_dict['contact_sheet'] = make_sheet(cropped_faces)
        else:
            info_dict['message'] = "But there were no faces in that file"
        image_info.append(info_dict)


# In[2]:


def Search(key_string):
    for info in image_info:
        if key_string in info['text']:
            print('Results found in file {}'.format(info['name']))
            if info['face_num']>0:
                display(info['contact_sheet'])
            else:
                print(info['message'])


# In[1]:


Search("Mark")


# In[14]:


Search("Christopher")


# In[ ]:




