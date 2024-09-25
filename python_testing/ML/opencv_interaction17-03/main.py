import cv2
import mediapipe as mp
import csv

# Create a window with the camera input
cap = cv2.VideoCapture(0)

# Mediapipe Hand Module
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

def get_pressed_key():
    return cv2.waitKey(1) & 0xff

def write_to_csv(csv_writer, points, pressed_key):
    # Write the pressed key as the first column in the CSV file
    csv_writer.writerow([pressed_key] + [point for point in points])

while True:
    # Read the frames from the camera
    ret, frame = cap.read()
    
    # Convert the frame from BGR to RGB (Mediapipe requires RGB frames)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Make predictions on the frame
    results = hands.process(rgb_frame)
    
    # Draw the hand contours and landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if mode == 'input':
                # Save the current position of the finger landmarks into the CSV
                points = [[landmark.x, landmark.y, landmark.z] for landmark in hand_landmarks.landmark]
                write_to_csv(csv_writer, points, get_pressed_key())
                
            else:
                mpDraw.draw_landmarks(
                    frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
    
    # Display the resulting frame
    cv2.imshow('Hand Detection', frame)
    
    # Change the mode based on the key pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        mode = 'input' if mode == 'normal' else 'normal'
    
    # Exit the camera with 'q' key
    if key == ord('q'):
        break

# When everything done, release the capture and close the CSV file
cap.release()
csv_file.close()
cv2.destroyAllWindows()