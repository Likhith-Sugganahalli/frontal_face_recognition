#this is a python script to take video feed from a webcam and detect faces(frontal)
#in the live feed and save the faces as crop(num).jpg
#the crop feature works best for images, in a video feed,
#multiple instances of the same face are saved
#and over time this accumalates :(


# import required libraries
import cv2
import numpy as np
cnt=0# counter, inorder to print multiple faces
# there are multiple haars cascade files you can try, their paths are to be initialised below
alt_tree=r"C:\Users\likhi\Documents\python_tut\face_detection\haarcascade_frontalface_alt_tree.xml"
default_file=r"C:\Users\likhi\Documents\python_tut\face_detection\haarcascade_frontalface_default.xml"
alt_standard=r"C:\Users\likhi\Documents\python_tut\face_detection\haarcascade_frontalface_alt.xml"
alt_2=r"C:\Users\likhi\Documents\python_tut\face_detection\haarcascade_frontalface_alt2.xml"
try:
	face_cascade  = cv2.CascadeClassifier(default_file)
	eye_cascade = cv2.CascadeClassifier(r'C:\Users\likhi\Documents\python tut\face recognistion\haarcascade_eye.xml')
	cap = cv2.VideoCapture(0)#video feed begins
except:
	print("error loading cascades")

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)# values 1.3 and 5 can be tweaked if curious, the cascade file is loaded
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0) , 2)# a rectangle is formed surrounding the 'face'
		roi_gray = gray[y:y+h, x:x+w]# this is the region of interest in grayscale i.e hopefully the face
		roi_color = img[y:y+h, x:x+w]# this is the same
		cnt+=1
		img_item = "crop{}.jpg".format(cnt)
		cv2.imwrite(img_item, roi_color)
	cv2.imshow('img',img)
	k=cv2.waitKey(30) & 0xff# stops the feed on esc button press
	if k == 27:
		break

	
cap.release()# ending all processes
cv2.destroyAllWindows()