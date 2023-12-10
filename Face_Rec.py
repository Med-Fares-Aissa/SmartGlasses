####################################FuRuS####################################
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
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

while(True):
#hethi l fnc principale
    def classify_face(im):


        ret, img = cap.read()
        #img = cv2.imread(im, 1)
        #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        #img = img[:,:,::-1]
     
        face_locations = face_recognition.face_locations(img)
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

        face_names = []
        for face_encoding in unknown_face_encodings:
            
            #lahne bch y9aren e tasawer eli encodinehom b taswira eli mel cam
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            #lahne 3ibara initialisineh l essem f unknown
            #yaani f kol mara ykamel executi l prg w bch yaawed yexcuti ysamih l aabed etheka unknown w ba3ed ythabet  
            name = "Unknown"

            # Lahne bch yhawel y9areb etaswira eli jayeto mel cam w taswira eli ecodineha a9reb distace keneet w yhawel yhot'hom fou9 baadh'hom w y9areen
            face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            #itha l9ahom kifkif lena yemchi yekteb f variable name lei samineh 9bila unknown essem e taswira eli heya essem l aabed 
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # lena ysawer rectangle
                cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

                # lena yekteb l essem f rectangle sghiir azra9 tahet e taswira
                cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)
                #BTW hethom e zouz ynajmo yetbadlo kima fazet fro (x, y , w , h ) mta3 9bal lei chofnehom


        # W lahne Bch yaffichi l video aadii 
        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names 
    print(classify_face("test.jpg"))


# w etheya kel3ada teb3a l cam
cap.release()
cv2.destroyAllWindows()

