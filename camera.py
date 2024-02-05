'''
This is a Camera Classifier Code.
We can use this for Image Classifier and almost the same code to identify celestial objects as well .We only need to update model.py:
By Adjusting preprocessing and feature extraction techniques.
By Training the classifier with appropriate model and dataset.
camera.py:
By Loading satellite images instead of camera frames.
app.py:
Update GUI elements for star identification context.
'''

import cv2 as cv

class Camera:

    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open camera!")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None
