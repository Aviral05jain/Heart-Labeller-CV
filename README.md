# Heart-Labeller-CV
This is a computer Vision assigment project given by dVerse labs to label all the sections of the Heart with a synthesized voice using Computer Vision and Object detection

for this project I had 5 goals to complete
1. the pointer for the screen
2. My Videocam and the image screen scaling for the efficient interaction
3. find out the coordinates of the regions of the heart and give the label output with respect to that
4. Use the synthsized engine for voice of the labels
5. Mkae a suitable GUI to integrate both the videos
[heart-diagram](https://github.com/Aviral05jain/Heart-Labeller-CV/assets/110279490/25a218c7-e4da-4794-9d45-400610924431)

# Goal 1
For the first goal I used OpenCV and Mediapipe for the landmarks detection to make the pointer and adjusted the code to get the landmark for index finger only since it was only going to be used

# Goal 2
I used opencv for videostream generation for both the heart image and the videocam

# Goal 3
Now this was quite the tedious part of the project. My first focus was to find the black dots and just make a small border around them and then just use the pointer to track the black dots but I need a model like YOLOv3 to work for the labeling but it was not a heart specimen or X ray and was just a simple diagram so I just figured all the coordinates of the regions of the heart. Thanks to the pointer which i made in the first goal I able to track the coordinates and work on giving the outputs based on which coordinate the pointer lied. It was now just a condition of comparisions

# Goal 4
Now with my label analysis logic was complete it was time to finally give the voice over to the labelled values. For the voice over I used pyttsx4 a text to speech NLP python package tool. Initialized the engine and when there was a label value the engine was intructed to say and then run.

# Goal 5
Now with my prototype complete it was time to integrate both  the videostream and the image into one screen. I used Tkinter got GUI creation and Pillow for image scaling and configuration

# The bugs which I found:
In the code there was line number 196 which was px = width - cx where px is the x-coordinate of the pointer in heart image,cx was the x pointer of videostream , width was the width of the videocam
In the prototype ( the code with commments) it was working fine my pointer was having synchroized alighnment (finger moving right image pointer moving right) but when i did the interface the opposite happened.
This I was not able to figure out but I could have figured out easily if there was more time

Other was the waiting of the engine of the speaker. It was a bit problematic beacuse the pointer and videostreaming was stopping beacuse that

In the end I have made a project with the tangible output. But surely I will work on the optimization and performance increment

![Screenshot 2024-03-01 235637](https://github.com/Aviral05jain/Heart-Labeller-CV/assets/110279490/d1eeac79-57a8-45cc-b90c-327cf41988e0)

Thank you Krishna Sir for giving me this opportunity to hone myself in my field of Interest i.e AI and Machine Learning with special regard in Computer Vision!


