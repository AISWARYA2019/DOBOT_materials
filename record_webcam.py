import cv2
import sounddevice as sd
from scipy.io.wavfile import write
import os
from pydub import AudioSegment

def camera():
    
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    
    cap = cv2.VideoCapture(1)
    ###############PLEASE RENAME "trial_no_()" BEFORE RUNNING
    filename = 'D:\IISc RIL internship\video trials\trial_no_1.avi'
    codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
    framerate = 30
    resolution = (640, 480)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
               
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    
    VideoFileOutput.release()
    cap.release()

def mic():
    fs = 44100  # this is the frequency sampling; also: 4999, 64000
    seconds = 5  # Duration of recording
 
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("Starting: Speak now!")
    sd.wait()  # Wait until recording is finished
    print("finished")
    write('output.wav', fs, myrecording)  # Save as WAV file
    os.startfile("output.wav")

thr = threading.Thread(target = mic, name='thread2, args = ()')
thr.start()
camera()
