import os
from tkinter import *

import numpy as np
from PIL import Image, ImageTk
import glob
import cv2
import os

path = glob.glob("drinks pics\\*.png")
list_files = os.listdir(r'drinks pics\\')
root = Tk()
root.geometry("800x600")
photos = []
root.title('BarMaster')

list_files_final = []
# Add image file
for x in list_files:
    if x.endswith(".png"):
        # Prints only text file present in My Folder
        list_files_final.append(x)


def displayImg(img):
    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)  # keep references!
    newPhoto_label = Label(image=photo)
    newPhoto_label.place(x=500, y=160)


list_files = os.listdir(r"drinks pics\\")
list_files_final = []
for x in list_files:
    if x.endswith(".png"):
        # Prints only text file present in My Folder
        list_files_final.append(x)


def Take_input():
    INPUT = input_user.get("1.0", "end-1c")

    alpha = str(INPUT).lower() + ".png"
    print(alpha)
    for file in list_files_final:
        if alpha == file:
            path = str("drinks pics\\") + alpha
            displayImg(path)


#
def show_images():

    img1 = cv2.imread('bloody mary.jpg')
    # Read Second Image
    img2 = cv2.imread('margarita.jpg')
    img3 = cv2.imread('tequila sunrise.jpg')

    # concatanate image Horizontally
    img_concate_Hori = np.concatenate((img1, img2,img3), axis=1)

    cv2.imshow('All_Drinks', img_concate_Hori)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


l = Label(root, text="Search a Drink :", bg='#325C7F', width=28)
input_user = Text(root, height=2, width=25)
l.place(x=80, y=300)
input_user.place(x=80, y=320)

# Add Image
# Create button and image
convert_btn = PhotoImage(file="search.png")
img = Button(root, image=convert_btn, command=lambda: Take_input(), borderwidth=0)
img.place(x=150, y=370)

img = Button(root, text="Show all Drinks", command=lambda: show_images())
img.place(x=300, y=380)

figure = PhotoImage(file="wine.png")
Label(
    root,
    image=figure
).place(x=80, y=40)
root.resizable(False, False)
root.geometry("800x550")

root.mainloop()
