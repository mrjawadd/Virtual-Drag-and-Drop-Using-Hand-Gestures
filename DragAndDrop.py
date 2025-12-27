import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)


class DragRect:
    def __init__(self, posCenter, size=[150, 150]):
        self.posCenter = posCenter
        self.size = size
        self.color = (255, 0, 255)
        self.isHeld = False

    def update(self, cursor, grabbed):
        cx, cy = self.posCenter
        w, h = self.size

        # Check if cursor is inside rect
        if cx - w//2 < cursor[0] < cx + w//2 and cy - h//2 < cursor[1] < cy + h//2:
            self.isHeld = grabbed
            if grabbed:
                self.posCenter = cursor
        else:
            self.isHeld = False


# Create rectangles
rectList = [DragRect([x * 250 + 150, 200]) for x in range(5)]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    grabbed = False
    cursor = (0, 0)

    if hands:
        lmList = hands[0]['lmList']
        x1, y1, _ = lmList[8]
        x2, y2, _ = lmList[12]
        length, _, _ = detector.findDistance((x1, y1), (x2, y2), img)

        if length < 50:  # fingers pinched
            cursor = (x1, y1)
            grabbed = True

    # Transparent overlay
    overlay = img.copy()
    for rect in rectList:
        rect.update(cursor, grabbed)
        cx, cy = rect.posCenter
        w, h = rect.size

        color = (0, 255, 0) if rect.isHeld else rect.color

        # Draw with transparency
        alpha = 0.4 if rect.isHeld else 0.25
        cv2.rectangle(overlay, (cx - w//2, cy - h//2),
                      (cx + w//2, cy + h//2), color, cv2.FILLED)

        # Add border + label
        cv2.rectangle(overlay, (cx - w//2, cy - h//2),
                      (cx + w//2, cy + h//2), (255, 255, 255), 2)
        cv2.putText(overlay, "Drag Me", (cx - 45, cy + 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Blend overlay for transparency
    img = cv2.addWeighted(overlay, 0.7, img, 0.3, 0)

    cv2.imshow("Virtual Drag & Drop - Enhanced", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
while True:
    success, img = cap.read()
    if not success:
        break
    
    # your processing and display code here
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:  # press ESC to close safely
        break

cap.release()
cv2.destroyAllWindows()
print("Camera released and windows closed successfully")

cap.release()
cv2.destroyAllWindows()
import sys
sys.exit()
