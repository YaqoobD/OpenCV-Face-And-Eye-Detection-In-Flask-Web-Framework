# OpenCV-Face-And-Eye-Detection-In-Flask-Web-Framework

Welcome to the OpenCV-Face-And-Eye-Detection-In-Flask-Web-Framework project!

This project showcases how to integrate face and eye detection using OpenCV into a Flask web application. OpenCV is a popular computer vision library that allows for various image and video processing tasks, including object detection. Flask, on the other hand, is a lightweight and flexible web framework for Python.

In this project, we have used the Haar Cascades classifier, which is a machine learning-based approach to object detection. The classifier is trained to detect specific objects, such as faces or eyes, based on a set of features. The features are determined by analyzing a large number of positive and negative images.

This project is intended for anyone interested in learning how to integrate OpenCV object detection into a Flask web application. The code is well-documented, and there are comments throughout the code to help you understand how everything works.

This code is a simple Flask web application that utilizes OpenCV to detect faces and eyes in real-time video streams from the user's webcam. Here's a brief overview of how it works:

* The code imports the Flask and OpenCV libraries.
* It creates a Flask application instance and sets up the user's webcam as the video source.
* The gen_frames function is defined, which captures each frame of the video stream and detects faces and eyes in the frame using the Haar cascades classifier. The detected objects are highlighted with bounding boxes.
* The index function is defined, which renders the index.html template. This template contains an HTML video element that displays the video stream from the webcam.
* The video_feed function is defined, which returns a Flask Response object that contains the gen_frames generator function as the source of the video stream.
* Finally, the Flask application is started with app.run(), and the video stream is displayed on the index.html template.

To use this code, you'll need to have Flask and OpenCV installed on your machine. Once you've installed these dependencies, you can run the application by executing the script and navigating to http://localhost:5000 in your web browser. The video stream should appear on the page, and faces and eyes should be detected in real-time as you move in front of the webcam.


## Acknowledgments

* Thanks to Krish Naik for the excellent tutorials on OpenCV and Flask that helped me develop this project.
* Special thanks to the OpenCV and Flask communities for providing the necessary tools and documentation to make this project possible.
