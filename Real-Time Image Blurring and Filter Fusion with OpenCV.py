import cv2 
import numpy as np 

# creating a filter to apply over our image
filter1 = np.ones((3, 3), np.float)/(9.0) 
filter2 = np.ones((5, 5), np.float)/(25.0) 
filter3 = np.ones((7, 7), np.float)/(49.0) 

# initialize video capture or read image file
input_type = input("Enter 'camera' to capture from webcam or 'image' to use an image file: ")
if input_type == 'camera':
    cap = cv2.VideoCapture(0)
elif input_type == 'image':
    file_path = input("Enter the path of the image file: ")
    frame = cv2.imread(file_path)
    frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))
else:
    print("Invalid input. Exiting program.")
    exit()

while True:
    if input_type == 'camera':
        # read frame from video capture
        ret, frame = cap.read()
        # resizing frame for our needs
        frame = cv2.resize(frame, (500, 500), fx = 0.1, fy = 0.1)
    
    # apply filters to frame
    blur1 = cv2.filter2D(frame, -1, filter1) 
    blur2 = cv2.filter2D(frame, -1, filter2) 
    blur3 = cv2.filter2D(frame, -1, filter3) 
    
    # create an image which is the overlap of all other filters
    blur_blast = cv2.filter2D(blur1, -1, filter2)
    blur_blast = cv2.filter2D(blur_blast, -1, filter3)
    
    # display original and filtered frames
    cv2.imshow('ORIGINAL', frame) 
    cv2.imshow('BLUR1', blur1) 
    cv2.imshow('BLUR2', blur2) 
    cv2.imshow('BLUR3', blur3) 
    cv2.imshow('BLUR_BLAST', blur_blast)
    
    # check for key press
    if cv2.waitKey(1) == ord('q'):
        break

# release video capture and destroy all windows
if input_type == 'camera':
    cap.release()
cv2.destroyAllWindows()
