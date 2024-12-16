import cv2
import imageio

# Input video file and output GIF file
video_path = "1216.mp4"
gif_path = "hero-gif.gif"

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# Define the frame skipping factor (e.g., process every 2nd frame for 2x speed)
frame_skip = 2

# Frame list to store frames
frames = []
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:  # End of video
        break

    # Skip frames to speed up the video
    if frame_count % frame_skip == 0:
        # Convert the frame from BGR to RGB (imageio expects RGB format)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame_rgb)

    frame_count += 1

# Release the video capture object
cap.release()

# Save frames as GIF using a higher FPS for faster playback
# Adjust fps for the desired speed (e.g., 20 for faster playback)
output_fps = 20
imageio.mimsave(gif_path, frames, fps=output_fps)

print(f"GIF saved at {gif_path}")