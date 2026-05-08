import cv2
import os

# Video Path
video_path = "../data/videos/video.mp4"

# Directory for the frames
output_dir = "../data/frames"
os.makedirs(output_dir, exist_ok=True)

# Open the video
cap = cv2.VideoCapture(video_path)

# Get the FPS
fps = cap.get(cv2.CAP_PROP_FPS)

# Counter
frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Give an image each second
    if frame_count % int(fps) == 0:
        filename = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()