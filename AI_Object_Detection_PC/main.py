import cv2
import os
from detector import detect
from alert import play_alarm, log_detection
from config import SAVE_IMAGES, PLAY_SOUND, ALARM_SOUND_PATH

os.makedirs("captures", exist_ok=True)

cap = cv2.VideoCapture(0)

print("System Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect(frame)

    for label, conf, x1, y1, x2, y2 in detections:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        log_detection(label)

        if SAVE_IMAGES:
            filename = f"captures/{label}.jpg"
            cv2.imwrite(filename, frame)

        if PLAY_SOUND:
            play_alarm(ALARM_SOUND_PATH)

    cv2.imshow("AI Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
