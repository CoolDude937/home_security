from flask import Flask, render_template, Response
import cv2
import face_recognition
import numpy as np
app=Flask(__name__)
video_capture = cv2.VideoCapture(0)
# andy's family faces
andy_image = face_recognition.load_image_file("andy_neutral_small.jpg")
andy_face_encoding = face_recognition.face_encodings(andy_image)[0]

joseph_image = face_recognition.load_image_file("joseph_neutral_small.jpg")
joseph_face_encoding = face_recognition.face_encodings(joseph_image)[0]

liudan_image = face_recognition.load_image_file("liudan_neutral_small.jpg")
liudan_face_encoding = face_recognition.face_encodings(liudan_image)[0]

chuan_image = face_recognition.load_image_file("chuan_neutral_small.jpg")
chuan_face_encoding = face_recognition.face_encodings(chuan_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    andy_face_encoding,
    joseph_face_encoding,
    chuan_face_encoding,
    liudan_face_encoding
]
known_face_names = [
    "Andy Ma",
    "Joseph Ma",
    "Chuan Ma",
    "Liu Dan"
]
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def gen_frames():  
    while True:
        ret, frame = video_capture.read()  # read the camera frame
        if not ret:
            break
        else:
            # flip frame horizontally
            frame = cv2.flip(frame, 1)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            # rgb_frame = frame[:, :, ::-1]
            rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            # Find all the faces and face enqcodings in the frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


            # Loop through each face in this frame of video
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.5)

                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('home_security_index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug=True)