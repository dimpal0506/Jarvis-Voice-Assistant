import time
import cv2
import pyautogui as p


def AuthenticateFace():

    flag = 0
    # Local Binary Patterns Histograms
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('engine\\auth\\trainer\\trainer.yml')  # load trained model
    cascadePath = "engine\\auth\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    # ID mapping must match the IDs used during dataset creation/training
    # Example: if dataset filenames were like user1.xx.jpg -> ID=1, user2.xx.jpg -> ID=2
    names = ['', 'User1', 'Dimpal']   # index 1 → User1, index 2 → Dimpal

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    success_count = 0  # count consecutive successful matches

    while True:
        ret, img = cam.read()
        if not ret:
            break

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id_pred, confidence = recognizer.predict(converted_image[y:y + h, x:x + w])

            # Stricter threshold (lower = better match)
            if confidence < 70:  # tune this between 60–80 if needed
                id = names[id_pred] if id_pred < len(names) else "unknown"
                success_count += 1
                if success_count >= 3:  # require 3 matches in a row
                    flag = 1
                    break
            else:
                id = "unknown"
                success_count = 0  # reset if any fail

            # Display results
            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, f"Conf: {round(confidence, 2)}", (x + 5, y + h - 5),
                        font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27 or flag == 1:
            break

    cam.release()
    cv2.destroyAllWindows()
    return flag
