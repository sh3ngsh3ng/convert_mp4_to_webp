import cv2
import imageio
 
video_path = "sample-hero.mp4"
gif_path = "hero-gif.gif"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot find video file")
    exit()


frames = []


while True:
    ret, frame = cap.read()
    if not ret:
        # end of video
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frames.append(frame_rgb)

# release the video capture object
cap.release()

# Save the frames as a gif using imageio
# Adjust 'fps' as needed for playback speed
imageio.mimsave(gif_path, frames, fps=10)

print("gif Saved")
