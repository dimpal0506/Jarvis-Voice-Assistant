import cv2
import numpy as np
from PIL import Image  # pillow package
import os

# Get the absolute path of the directory where trainer.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths relative to BASE_DIR
samples_path = os.path.join(BASE_DIR, 'samples')
cascade_path = os.path.join(BASE_DIR, 'haarcascade_frontalface_default.xml')
trainer_path = os.path.join(BASE_DIR, 'trainer', 'trainer.yml')

# Create recognizer and detector
recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
detector = cv2.CascadeClassifier(cascade_path)  # Haar Cascade classifier


def Images_And_Labels(path):  # function to fetch the images and labels
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        # Convert image to grayscale
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img, 'uint8')

        # Extract numeric ID
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        # Detect faces in the image
        faces = detector.detectMultiScale(img_arr)

        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids


print("Training faces. It will take a few seconds. Wait...")

faces, ids = Images_And_Labels(samples_path)
recognizer.train(faces, np.array(ids))

# Make sure the trainer folder exists
trainer_folder = os.path.dirname(trainer_path)
os.makedirs(trainer_folder, exist_ok=True)

# Save the trained model
recognizer.write(trainer_path)

print("Model trained. Now we can recognize your face.")
