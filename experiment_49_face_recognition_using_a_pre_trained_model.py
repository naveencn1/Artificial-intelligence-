# CSA17 - Artificial Intelligence | Experiment 49 (Manual Ex. 5.9): Face Recognition using a Pre-trained Model
# Name            : V V Naveen Kumar
# Register Number : 192321018

import cv2
import face_recognition

known_img = face_recognition.load_image_file("known_person.jpg")
known_encoding = face_recognition.face_encodings(known_img)[0]
known_name = "Dr. Jai"

test_img = face_recognition.load_image_file("group_photo.jpg")
locations = face_recognition.face_locations(test_img)
encodings = face_recognition.face_encodings(test_img, locations)
print("Faces detected:", len(locations))

output = cv2.cvtColor(test_img, cv2.COLOR_RGB2BGR)
for (top, right, bottom, left), enc in zip(locations, encodings):
    distance = face_recognition.face_distance([known_encoding], enc)[0]
    match = face_recognition.compare_faces([known_encoding], enc, tolerance=0.6)[0]
    name = known_name if match else "Unknown"
    print("Face at (top=%d, left=%d): %s (distance %.2f)" % (top, left, name, distance))
    cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(output, name, (left, top - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imwrite("recognised.jpg", output)
print("Result saved as recognised.jpg")
