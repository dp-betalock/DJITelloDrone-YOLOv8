# TelloCV
Combine YOLOv8 with a DJI Tello Drone! This project allows you to see the object detection results from your computer, control the drone with the Tello app, and save the results as a video export!

### Notes
- There is a good amount of stuff to install; not recommended to start this project on low storage (unless you already fulfilled most of the requirements, of course)
- The TelloCV_GitHubScript.py script features comments/annotations to help understand what happens at each line of code.


# Usage/Instructions
### Requirements
- Windows 10/11
- [Tello App](https://www.dji.com/downloads/djiapp/tello)
- [Anaconda Package Manager](https://www.anaconda.com/download)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- Visual Studio Build Tools (insert more info here)
- [CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
> CUDA is for NVIDIA GPUs; CUDA Toolkit 11.8 works with PyTorch 2.1.0)
- Download your desired YOLOv8 model size under 'Performance Metrics' and 'Detection (COCO)' at [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/models/yolov8/#performance-metrics) to acquire a yolov8(n/s/m/l/x).pt file that will be used later

### Cloning the Repository
1. In GitHub, under the green '<> Code' button, copy the HTTPS URL
2. Open Pycharm
3. Click 'Get from VCS' from the PyCharm welcome screen
4. Paste the URL and click 'Clone'
5. After the project is created, you may see a popup that says: "**File environment.yml contains project dependencies. Would you like to create a conda environment using it?**" Click 'OK' as this will install the required packages and libraries required for this project and create a new Conda Environment named 'TelloCV_GitHubEnv'.
7. In PyCharm, look at the bottom right corner and click on 'No interpreter'. To create a new interpreter, click on 'Add New Interpreter' and then 'Add Local Interpreter'. Then, click on "Conda Environment" on the left column and make sure 'Use existing environment' is selected. Find '**TelloCV_GitHubEnv**' in the dropdown menu. Finally, click 'OK'. Python 3.9 should automatically be used.

### Make Script Configurations
1. In the script, change the video path to where you want your exported video to be located (don't forget to use \\ and not \)
2. If needed, change the name of the YOLOv8 model file to the size you want to use (ex: yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.), as it is preset to use 'yolov8s.pt'.
3. Drag and drop that yolov8(n/s/m/l/x).pt file into your project.
>Look around line 21 for the video export path, and around line 30 for the yolo model file...


### Using the Tello Drone with the script
1. Make sure the battery is fully charged.
2. Turn on the Tello Drone until the LED flashes yellow.
3. On your computer AND your phone/tablet, connect to your Tello WiFi. (If you see what the drone sees on the Tello App, it's definitely connected)
4. On PyCharm, click 'Run' at the top right.
5. After a few seconds, you should see a window appear that displays the drones video stream and anything it detects. This will also make the stream on the Tello App freeze or go black, which is normal.
6. You are in control of when the drone starts takeoff and when it lands with Tello App. You can grab the drone and test the video feed performance from the streaming window before taking off using the Tello App.
7. Use the streaming window to fly the drone and see the YOLOv8 object detection results on screen!
8. Once you are finished flying the drone, click the 'x' key on the keyboard to stop the stream.
9. Land the Tello Drone with the Tello App by dragging the altitude joystick really far down. If the drone is near the floor and not landing, try dragging the joystick down farther.

### Viewing the Video Results
1. The video that is exported starts recording as soon as the streaming window appears, and ends when you close the streaming window with the 'x' key on the keyboard.
2. To view that video, go to the file path you set the video export to be located in.
>Note: If you want multiple videos, make sure you change the video name each time. If the name remains unchanged, it will overwrite that video with that name every time.


## Troubleshooting
### GPU Check
Using GPU instead of CPU on this project is important for real-time video speed. To check if CUDA is available and that the GPU is being used, run this code:
```
import torch
# Check if CUDA is available
if torch.cuda.is_available():
    # Create a tensor on the GPU
    device = torch.device("cuda")
    x = torch.rand(5, 5).to(device)
    print("Tensor on GPU:", x)
else:
    print("CUDA is not available.")

#Making sure that GPU is used and not CPU.
import ultralytics
ultralytics.checks()
```
### Packages/Libraries/Modules not installed
Use pip or conda to install packages:
```
pip install package_name
conda install package_name
```
Or for a specific version of a package:
```
pip install package_name==version_number
conda install package_name=version_number
```

### Multiple Copies of OpenMP error
1. In PyCharm go to Run > Edit Configurations... and click on the python script. Find 'Environment Variables:' and paste the following there:
PYTHONUNBUFFERED=1;KMP_DUPLICATE_LIB_OK=TRUE;OMP_NUM_THREADS=4
>This is what worked for me at least...

### Requiring Microsoft Visual C++ Build Tools
Download the installer from [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Make sure to select the "Desktop development with C++" workload during installation.

After that, 

## Important Sources
