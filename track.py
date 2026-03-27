import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")  # auto-download

# Open video
cap = cv2.VideoCapture("input.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection + tracking
    frame = cv2.resize(frame, (640, 360))
    results = model.track(frame, persist=True)

    # Draw results
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Tracking", annotated_frame)

    # Exit key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()