import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from gtts import gTTS 
from time import sleep

cap = cv2.VideoCapture(0)
#fonction bch tencodilek les photos eli mawjoud f dossier essmo faces
def get_encoded_faces():

    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
                print("get_encoded_faces");

    return encoded

# hethom les variables eli msajlin mel fonction eli fetet
#mahtoutin l bara mel whie true khater ken ndakhouhom fel loop bch yeklo barchaaa mememoire
#w bch ywali kol mara yaawed yencodi fe les images w heya testha9 tsir mara baraka awel ma t'hel l programme
faces = get_encoded_faces()
faces_encoded = list(faces.values())
known_face_names = list(faces.keys())
text_ekher='dae'
while(True):


    ret, img = cap.read()
 
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


            texts= known_face_names[best_match_index]
                
            if text_ekher != texts :
                if texts == "Fares" :
                    os.system(" menyar.mp3")
                if texts == "amal" :
                    os.system("start amal.mp3")
                if texts == "wided" :
                    os.system("start wided.mp3")
            text_ekher = texts
                

        # W lahne Bch yaffichi l video aadii 
    cv2.imshow('Video', img)
    k= cv2.waitKey(20) & 0xFF 
    if k== 27:
        break


# w etheya kel3ada teb3a l cam
cap.release()
cv2.destroyAllWindows()


