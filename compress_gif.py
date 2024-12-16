import cv2
import imageio
from PIL import Image

# Input and output paths
video_path = "1216.mp4"
temp_gif_path = "temp.gif"
final_gif_path = "output_compressed.gif"

# Open video file
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# Compression settings
frame_skip = 2               # Skip frames to reduce GIF size
resize_factor = 0.5          # Scale down frames
output_fps = 10              # Adjust playback speed (frames per second)
frames = []
frame_durations = []         # Frame durations in milliseconds
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_skip == 0:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = frame_rgb.shape
        # Resize frame
        frame_resized = cv2.resize(frame_rgb, (int(width * resize_factor), int(height * resize_factor)), interpolation=cv2.INTER_AREA)
        frames.append(frame_resized)
        # Add frame duration (based on fps)
        frame_durations.append(1000 // output_fps)

    frame_count += 1

cap.release()

# Save the GIF with frame durations using imageio
imageio.mimsave(temp_gif_path, frames, duration=[d / 1000.0 for d in frame_durations])

print(f"Compressed GIF saved and playable at {final_gif_path}")