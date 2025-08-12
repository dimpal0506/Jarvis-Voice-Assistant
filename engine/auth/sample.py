import cv2
import os

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_id = input("Enter a Numeric user ID here:  ")
print("Taking samples, look at camera ....... ")
count = 0

# ✅ Define correct absolute path to samples directory
samples_dir = os.path.join(os.path.dirname(__file__), 'samples')

# ✅ Create directory if not exists
os.makedirs(samples_dir, exist_ok=True)

while True:
    ret, img = cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

        # ✅ Save image to correct samples directory
        image_path = os.path.join(samples_dir, f"face.{face_id}.{count}.jpg")
        cv2.imwrite(image_path, converted_image[y:y+h, x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 100:
        break

print("Samples taken, now closing the program...")
cam.release()
cv2.destroyAllWindows()
