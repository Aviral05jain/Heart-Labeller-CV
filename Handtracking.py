# import cv2
# import mediapipe as mp
# import pyttsx4
#
# speak_engine = pyttsx4.init();
#
# cap = cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils
#
# # Load the given image
# given_image = cv2.imread("heart-diagram.jpg")  # Provide the path to your image
# given_image = cv2.resize(given_image, (width, height))  # Resize the image to match the video stream size
#
# # Initialize pointer position variables
# pointer_position = None
# prev_pointer_position = None
#
# # Initialize given_image_copy
# given_image_copy = given_image.copy()
#
# while True:
#     success, img = cap.read()
#
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = hands.process(imgRGB)
#
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             for id, lm in enumerate(handLms.landmark):
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 if id == 8:  # Index finger tip
#                     px = width - cx
#                     pointer_position = (px, cy)
#                     cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
#
#
#
#     if pointer_position != prev_pointer_position:
#         # Clear previous pointer position
#         given_image_copy = given_image.copy()
#         prev_pointer_position = pointer_position
#
#     if pointer_position:
#         # Draw the pointer on the given image
#         cv2.circle(given_image_copy, pointer_position, 5, (255, 0, 255), cv2.FILLED)
#
#         if 220 <= pointer_position[0] <= 250 and 190 <= pointer_position[1] <= 270:
#             label_name = "Right Atrium"
#             cv2.putText(given_image_copy,label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 330 <= pointer_position[0] <= 415 and 235 <= pointer_position[1] <= 352:
#             label_name = "Left Ventricle"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 290 <= pointer_position[0] <= 300 and 185 <= pointer_position[1] <= 195:
#             label_name = "Pulmonary valve"
#             cv2.putText(given_image_copy,label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 335 <= pointer_position[0] <= 440 and 120 <= pointer_position[1] <= 155:
#             label_name = "Pulmonary Artery"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 405 <= pointer_position[0] <= 440 and 175 <= pointer_position[1] <= 210:
#             label_name = "Pulmonary Vein"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 310 <= pointer_position[0] <= 375 and 45 <= pointer_position[1] <= 110:
#             label_name = "Aorta"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 245 <= pointer_position[0] <= 290 and 350 <= pointer_position[1] <= 405:
#             label_name = "Inferior vena Cava"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 320 <= pointer_position[0] <= 400 and 160 <= pointer_position[1] <= 240:
#             label_name = "Left Atrium"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 245 <= pointer_position[0] <= 350 and 265 <= pointer_position[1] <= 370:
#             label_name = "Right Ventricle"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 345 <= pointer_position[0] <= 385 and 400 <= pointer_position[1] <= 440:
#             label_name = "Descending Aorta"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 310 <= pointer_position[0] <= 415 and 360 <= pointer_position[1] <= 395:
#             label_name = "Septum"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#         if 220 <= pointer_position[0] <= 300 and 60 <= pointer_position[1] <= 160:
#             label_name = "Vena Cava"
#             cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             speak_engine.say(label_name)
#             speak_engine.runAndWait()
#
#     cv2.imshow("Video Stream", img)
#     cv2.imshow("Given Image", given_image_copy)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import pyttsx4
import tkinter as tk
from PIL import Image, ImageTk

speak_engine = pyttsx4.init()

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Load the given image
given_image = cv2.imread("heart-diagram.jpg")  # Provide the path to your image
given_image = cv2.resize(given_image, (width, height))  # Resize the image to match the video stream size

# Initialize pointer position variables
pointer_position = None
prev_pointer_position = None

# Initialize given_image_copy
given_image_copy = given_image.copy()

# Create a tkinter window
root = tk.Tk()
root.title("Heart Diagram Labeling")

# Create a frame for the video streams
video_frame = tk.Frame(root)
video_frame.pack(side="left", padx=10, pady=10)

# Create a frame for the labeled image
image_frame = tk.Frame(root)
image_frame.pack(side="left", padx=10, pady=10)

# Create video stream label
video_label = tk.Label(video_frame)
video_label.pack()

# Create labeled image label
image_label = tk.Label(image_frame)
image_label.pack()


def update_gui():
    global pointer_position, prev_pointer_position, given_image_copy

    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for tkinter display
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:  # Index finger tip
                    px = width - cx
                    pointer_position = (px, cy)
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)


    if pointer_position != prev_pointer_position:
        # Clear previous pointer position
        given_image_copy = given_image.copy()
        prev_pointer_position = pointer_position

    if pointer_position:
        # Draw the pointer on the given image
        cv2.circle(given_image_copy, pointer_position, 5, (255, 0, 255), cv2.FILLED)
        if 220 <= pointer_position[0] <= 250 and 190 <= pointer_position[1] <= 270:
            label_name = "Right Atrium"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 330 <= pointer_position[0] <= 415 and 235 <= pointer_position[1] <= 352:
            label_name = "Left Ventricle"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 290 <= pointer_position[0] <= 300 and 185 <= pointer_position[1] <= 195:
            label_name = "Pulmonary valve"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 335 <= pointer_position[0] <= 440 and 120 <= pointer_position[1] <= 155:
            label_name = "Pulmonary Artery"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 405 <= pointer_position[0] <= 440 and 175 <= pointer_position[1] <= 210:
            label_name = "Pulmonary Vein"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 310 <= pointer_position[0] <= 375 and 45 <= pointer_position[1] <= 110:
            label_name = "Aorta"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 245 <= pointer_position[0] <= 290 and 350 <= pointer_position[1] <= 405:
            label_name = "Inferior vena Cava"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 320 <= pointer_position[0] <= 400 and 160 <= pointer_position[1] <= 240:
            label_name = "Left Atrium"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 245 <= pointer_position[0] <= 350 and 265 <= pointer_position[1] <= 370:
            label_name = "Right Ventricle"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 345 <= pointer_position[0] <= 385 and 400 <= pointer_position[1] <= 440:
            label_name = "Descending Aorta"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 310 <= pointer_position[0] <= 415 and 360 <= pointer_position[1] <= 395:
            label_name = "Septum"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

        if 220 <= pointer_position[0] <= 300 and 60 <= pointer_position[1] <= 160:
            label_name = "Vena Cava"
            cv2.putText(given_image_copy, label_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            speak_engine.say(label_name)
            speak_engine.runAndWait()

    # Convert the images to Tkinter format
    video_img = ImageTk.PhotoImage(image=Image.fromarray(frame))
    image_img = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(given_image_copy, cv2.COLOR_BGR2RGB)))

    # Update the labels
    video_label.config(image=video_img)
    video_label.image = video_img
    image_label.config(image=image_img)
    image_label.image = image_img

    root.after(10, update_gui)


update_gui()

root.mainloop()
cap.release()
cv2.destroyAllWindows()
