#  _____       _  _        ___ __   __
# |_   _| ___ | || | ___  / __|\ \ / /
#   | |  / -_)| || |/ _ \| (__  \   /
#   |_|  \___||_||_|\___/ \___|  \_/

# Import libraries
import cv2
from ultralytics import YOLO
from djitellopy import Tello


# Initializing the Tello drone
tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()


# State the path/location of where the video output file will be saved
# Insert your own path by copy and pasting the file path address from File Explorer
video_path = 'C:\\Users\\etc...\\video_name_here.mp4'   # add video name at the end!

# State what video codec to use (mp4, h.264, av1, etc.)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# video_out = (video_path, fourcc, FPS, (Frame Width, Frame Height), isColor = T/F)
video_out = cv2.VideoWriter(video_path, fourcc, 20, (960,720), isColor=True)

# Load the pretrained YOLOv8 model (yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.)
model = YOLO('yolov8s.pt', task='detect')

# Get the 'BackgroundFrameRead' object that HOLDS the latest captured frame from the Tello
frame_read = tello.get_frame_read(with_queue=False, max_queue_len=0)

while True:
    # Access the frame from the video using '.frame', so we can USE it and display it
    frame = frame_read.frame

    if frame is not None:   #in other words, if there IS a frame...
        # Run YOLOv8 Object Detection on the frame
        # 'results' saves information about the detected objects
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Convert the annotated frame colors from BGR to RGB
        annotated_frame = cv2.cvtColor(annotated_frame,cv2.COLOR_BGR2RGB)

        # Write the annotated frame to the video output
        video_out.write(annotated_frame)

        # Display the annotated frame in a window
        cv2.imshow("YOLOv8 Tello Drone Tracking", annotated_frame)

        # Break the loop if 'x' is pressed
        if cv2.waitKey(1) & 0xFF == ord("x"):
            break

    else:
        # Indicate no frame was received
        print("No frame received")

video_out.release()     # Closes the video output file
tello.end()             # Ends the tello object (lands tello, turns off stream, stops BackgroundFrameRead)
cv2.destroyAllWindows() # Destroys any open windows, such as the streaming window.

# NOTICE:
# Although the script will finish, the Tello drone will remain in flight when connected to multiple devices.
# This means that the drone will not land, even if it's told to do so in the script (based on my experience).
# To land when connected to the computer and Tello app, use the app to lower the altitude until the drone lands.

