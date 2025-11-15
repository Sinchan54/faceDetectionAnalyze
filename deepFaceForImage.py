from deepface import DeepFace
import cv2


cv_img = cv2.imread("DSC02418.jpg") #Enter location of the input image
detected_faces = DeepFace.extract_faces(img_path=cv_img)
boxThresholdSize = 300000 # Set filter on what size of face allowed for detection
conf = 0.9 # Set confidence threshold for filtering

for face_info in detected_faces:
    x = face_info['facial_area']['x']
    y = face_info['facial_area']['y']
    w = face_info['facial_area']['w']
    h = face_info['facial_area']['h']

    print('Area of face box', int(w*h)) # to display size of boxes for setting threshold
    # Draw the bounding box on the image
    if(face_info['confidence'] > conf and int(w*h)>boxThresholdSize):
          cv2.rectangle(cv_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
          startY = y
          endY = y+h
          startX = x
          endX = x+w
          cropped_image = cv_img[startY:endY, startX:endX]
          cv2.imwrite('cropped_image.jpg', cropped_image)
          cv2.imshow("Faces Detected", cv_img)
          cv2.waitKey(0)
          cv2.destroyAllWindows()
          cv2.imwrite("output.jpg", cv_img)




