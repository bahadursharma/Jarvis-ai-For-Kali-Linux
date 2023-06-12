import cv2
import face_recognition
import playsound
import traceback

# Load your image (the one to compare faces with)
known_image = face_recognition.load_image_file("/home/zenox/Jarvis/imageData/2023-05-21-175856.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the frame to RGB color
        rgb_frame = frame[:, :, ::-1]

        # Find all faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        if len(face_encodings) > 0:
            # Check if the faces match yours
            matches = face_recognition.compare_faces([known_encoding], face_encodings[0])

            if matches[0]:
                # Play the sound if it's a match
                playsound.playsound("/home/zenox/Jarvis/mp3(data)/Jarvis face ID.mp3")

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        traceback.print_exc()
        break

# Release the video capture
video_capture.release()
cv2.destroyAllWindows()
