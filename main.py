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

import app

def main():
    app.App(window_title="Camera Classifier v0.1 Alpha")

if __name__ == "__main__":
    main()
