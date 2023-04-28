# import necessary libraries
from flask import Flask,render_template,Response
import cv2

# create a Flask app instance
app=Flask(__name__)

# set up the camera as the video source
camera=cv2.VideoCapture(0)

# define a function to generate video frames
def gen_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        
        else:
            detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade =cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
            # Draw The rectangle arounf the each face
            
            for (x,y, w, h ) in faces:
                cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2) 
                
            # convert the frame to a JPEG image and yield it to the browser
                roi_gray = gray [y:y+h, x:x+w]
                roi_color = frame [y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray,1.1,7)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey),(ex+ew, ey+eh),(0,255,0),2)
                    
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            
# define the root URL endpoint
@app.route('/')
def index():
    
    # render the index.html template
    return render_template('index.html')

# define a video feed URL endpoint
@app.route('/video_feed')
def video_feed():
    
    # return the video stream as a Flask response
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
 
# Start the Flask app with debugging enabled    
if __name__=='__main__':
    app.run(debug=True)        
                    
                    
            
            