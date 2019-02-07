# import the necessary packages
from threading import Thread
import cv2
 
class CamVideoStream:
    def __init__(self, src=0):
        # initialize the video camera stream and read the first frame
		# from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        # Initalize the timestamp variable
        self.ts = time.time()
 
		# initialize the variable used to indicate if the thread should
		# be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
            self.ts = time.time()

    def read(self):
        # return the frame most recently read
        return self.frame
        
    def open(self):
        # return if the the camera conexion is open
        return self.grabbed

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

    def timestamp(self):
        # return the timestamp related with the frame most recently read
        return self.ts