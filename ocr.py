# Hado l'Imports
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

import pytesseract
from gtts import gTTS
from playsound import playsound
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Hado diyal l'Video Reco
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

video = cv2.VideoCapture("download ip webcam in ur phone and put the ip")
video.set(3, 640)
video.set(4, 480)

# Hado diyal l'Images
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

img1 = cv2.imread("text.jpg")
img2 = cv2.imread("logos.jpg")
img3 = cv2.imread("signs.jpg")


h1Img, w1Img, _ = img1.shape
h2Img, w2Img, _ = img2.shape
h3Img, w3Img, _ = img3.shape

# Hado diyal l'Characters Reco
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

box1 = pytesseract.image_to_boxes(img1)
box2 = pytesseract.image_to_boxes(img2)
box3 = pytesseract.image_to_boxes(img3)

# Hado diyal l'Words Reco
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

data1 = pytesseract.image_to_data(img1)
data2 = pytesseract.image_to_data(img2)
data3 = pytesseract.image_to_data(img3)

# Hadi hiya Speech Recognition
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

# filewrite = open("string.txt", "w")
# for z, a in enumerate(data1.splitlines()):
#         if z != 0:
#             a = a.split()
#             if len(a) == 12:
#                 x, y = int(a[6]), int(a[7])
#                 w, h = int(a[8]), int(a[9])
#                 cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 1)
#                 cv2.putText(img1, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#                 filewrite.write(a[11] + " ")
# filewrite.close()
# fileread = open("string.txt", "r")
# lang = 'en'
# line = fileread.read()
# if line != ' ':
#     speech = gTTS(text=line, lang=lang, slow=False)
#     speech.save("test.mp3")
# cv2.imshow('gtts', img1)
# cv2.waitKey(0)
# playsound("test.mp3")


# Hadi hiya Video Recognition
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

# while True:
#     check, frame = video.read()
#     data4 = pytesseract.image_to_data(frame)
#     for z, a in enumerate(data4.splitlines()):
#         if z != 0:
#             a = a.split()
#             if len(a) == 12:
#                 x, y = int(a[6]), int(a[7])
#                 w, h = int(a[8]), int(a[9])
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
#                 cv2.putText(frame, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#     cv2.imshow('Video Capture', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         video.release()
#         cv2.destroyAllWindows()
#         break


# Hadi hiya Recognition Words
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

# for z, a in enumerate(data1.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 1)
#             cv2.putText(img1, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#
# for z, a in enumerate(data2.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 1)
#             cv2.putText(img2, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#
# for z, a in enumerate(data3.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 255, 0), 1)
#             cv2.putText(img3, a[11], (x, y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#
# cv2.imshow('Image 1', img1)
# cv2.imshow('Image 2', img2)
# cv2.imshow('Image 3', img3)
# cv2.waitKey(0)

# Hadi hiya Recognition Characters
# ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

# for a in box1.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img1, (x, h1Img - y), (w, h1Img - h), (0, 255, 0), 2)
#     cv2.putText(img1, a[0], (x, h1Img - y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#
# for a in box2.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img2, (x, h2Img - y), (w, h2Img - h), (0, 255, 0), 2)
#     cv2.putText(img2, a[0], (x, h2Img - y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#
# for a in box3.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img3, (x, h3Img - y), (w, h3Img - h), (0, 255, 0), 2)
#     cv2.putText(img3, a[0], (x, h3Img - y + 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
#
#
# cv2.imshow('image 1', img1)
# cv2.imshow('image 2', img2)
# cv2.imshow('image 3', img3)
#
# cv2.waitKey()

# BY WEEKENDOX ➜➜ ("https://github.com/Weekendox")