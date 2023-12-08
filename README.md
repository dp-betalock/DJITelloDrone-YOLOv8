# TelloCV
"This project allows you to use YOLOv8 with a DJI Tello Drone for real-time object detection streaming on your computer! You can control the drone with the Tello app and also save the detection results as a video."

### Notes
- The TelloCV_GitHubScript.py script features comments/annotations to help in understanding what happens at each line of code.


# Usage/Instructions
### Requirements
>[!IMPORTANT]
>Not recommended to start this project on low storage (unless you already fulfilled most of the requirements, of course)
- Windows 10/11
- [Tello App](https://www.dji.com/downloads/djiapp/tello)
- [DJI Tello Drone](https://store.dji.com/product/tello?vid=38421)
- [Anaconda Package Manager](https://www.anaconda.com/download)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- [CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
> CUDA is for NVIDIA GPUs; CUDA Toolkit 11.8 works with PyTorch 2.1.0)
- Download your desired YOLOv8 model size under 'Performance Metrics' and 'Detection (COCO)' at [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/models/yolov8/#performance-metrics) to acquire a yolov8(n/s/m/l/x).pt file that will be used later

### Cloning the Repository
1. In GitHub, under the green '**<> Code**' button, copy the HTTPS URL
2. Open Pycharm
3. Click '**Get from VCS**' from the PyCharm welcome screen
4. Paste the URL and click 'Clone'
5. After the project is created, you may see a popup that says:
"**File environment.yml contains project dependencies. Would you like to create a conda environment using it?**" Click '**OK**' as this will install the required packages and libraries required for this project and create a new Conda Environment named '**TelloCV_GitHubEnv**'. Wait until the processes are complete before moving on.
6. In PyCharm, look at the bottom right corner and click on '**No interpreter**'. To create a new interpreter, click on '**Add New Interpreter**' and then '**Add Local Interpreter**'. Then, click on "**Conda Environment**" on the left column and make sure '**Use existing environment**' is selected. Find '**TelloCV_GitHubEnv**' in the dropdown menu. Finally, click '**OK**'.
7. Although Python 3.9 should automatically be selected, you can verify this by clicking on the interpreter in the bottom right corner, clicking '**Interpreter Settings...'**, and scrolling down until you find the '**python**' package with its version number next to it.

### Make Script Configurations
>[!TIP]
>Look around line 21 for the video export path and line 30 for the YOLO model file.
1. In the script, change the video path to where you want your exported video to be located (don't forget to use double backslashes).
2. If needed, change the name of the YOLOv8 model file to the size you want to use in the script (ex: 'yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', etc.), as it is preset to use 'yolov8s.pt'.
3. Drag and drop that yolov8(n/s/m/l/x).pt file from Ultralytics into your PyCharm project.
4. Type ```pip install opencv-python ultralytics djitellopy``` in the PyCharm terminal. These are the last few pip packages that need to be installed.

### Using the Tello Drone with the script
1. Make sure the battery is fully charged.
2. Turn on the Tello Drone until the LED flashes yellow.
3. On your computer **AND** your phone/tablet, connect to your Tello WiFi network (if you see what the drone sees on the Tello App, it's definitely connected)
4. On PyCharm, click 'Run' at the top right.
5. After a couple of seconds, a connection with the drone will be initialized and you should see a streaming window appear that displays the drone's video stream and anything it detects. This will also make the stream on the Tello App freeze or go black, which is normal.
6. You are in control of when the drone starts takeoff and when it lands using the **Tello App**. You can grab the drone and test the video feed performance from the streaming window before taking off using the Tello App.
7. Use the streaming window to fly the drone and see the YOLOv8 object detection results on screen!
9. Once you are finished flying the drone, land with the Tello App by dragging the altitude joystick really far down and **holding** it there. If the drone is near the floor and not landing, try dragging the joystick down farther.
10. Click the '**x**' key on the keyboard to stop the stream and the script.
>[!NOTE]
>If for any reason you are unable to land the drone, _carefully_ grab the underside of the drone and flip it upside down. This will stop the motors as a safety feature.

### Viewing the Video Results
1. The video that is exported starts recording as soon as the streaming window appears, and ends when you close the streaming window with the 'x' key on the keyboard.
2. To view that video, go to the file path you set the video export to be located in.
>[!NOTE]
>If you want multiple videos, make sure you change the video name each time. If the name remains unchanged, it will overwrite the video with that name every time.


## Troubleshooting
### GPU Check / Slow video feed problems
Using GPU instead of CPU on this project is important for real-time video speed. Setting your GPU to performance mode also helps. To check if CUDA is available and that the GPU is being used, run this code:
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

# Check the version of CUDA
cuda_version = torch.version.cuda
print(f"CUDA Version: {cuda_version}")

# Making sure that GPU is used and not CPU.
import ultralytics
ultralytics.checks()
```
If CUDA was detected as not available, or 'CUDA Version: None', run the following code in the PyCharm terminal and it should do the trick:

```conda install pytorch torchvision torchaudio -c pytorch```

### Packages/Libraries/Modules not installed/found
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
Example:
```
ModuleNotFoundError: No module named 'ultralytics'
```
Type ```pip install ultralytics``` in the PyCharm terminal.

### Multiple Copies of OpenMP error
1. In PyCharm go to Run > Edit Configurations... and click on the python script. Find 'Environment Variables:' and paste the following there:

PYTHONUNBUFFERED=1;KMP_DUPLICATE_LIB_OK=TRUE;OMP_NUM_THREADS=4
>This is what worked for me...

### Requiring Microsoft Visual C++ Build Tools
Download the installer from [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Make sure to select the "Desktop development with C++" workload during installation.

To verify that the Microsoft Visual C++ Build Tools are successfully installed and available in your command prompt or terminal:
1. Open the command prompt on your computer
2. Type ```cl.exe```
If the command was recognized and Microsoft Visual C++ Build Tools are correctly installed, you should see information about the compiler, including its version.

If the compiler is NOT recognized or an error message is displayed, it may indicate an issue with the installation or the PATH configuration. Do the following carefully:
1. Find the path by locating the Visual Studio Build Tool installation directory. The address will be in the same format but might have a different year or version number. That being said, in File Explorer, you may be able to follow a directory that might look something like this:
```C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64```
3. Copy the entire address.
4. Open the Windows Start Menu.
5. Search for "Environment Variables" and click "Edit the system environment variables."
6. After the System Properties window opens, click the "Environment Variables..." button.
7. Under the "System Variables" section, select the 'Path' variable and click the "Edit..." button.
8. After the Edit Environment Variable window opens, click the "New" button and paste the path.
9. Click 'OK'
10. Restart your computer and repeat the two steps for verifying the installation of the Build Tools (open cmd, type cl.exe...).

### Tello Drone Not Connecting // Auto Landing // Drifting
From my experience, when I connect the drone through its WiFi network, the Tello App doesn't always register the connection. The app can be a bit intermittent sometimes and work one day, and not work another day. Try the following:
- Hold down the power button on the drone for a few seconds until the LED turns off. Wait a few seconds until pressing and holding the power button once again to turn it back on.
- Close out the Tello App completely. Then, go to the Settings app and find the Tello WiFi. Click the 'i' icon and click 'Forget This Network'. Unfortunately, I do not know about the process for forgetting/removing a WiFi network connection on other devices besides Apple devices. After that, reconnect the Tello.
- Check for Tello App updates.

Auto landing:
- The Tello drone has a safety feature that auto-lands the drone after 15 or so seconds of no received input. Using the Tello App seems to prevent this problem, but it is good to know.

Drifting:
- Fly the drone in a very well-lit environment! It helps keep the drone still.
- Make sure the blades are not bent.
- Wind will blow the drone away.

## Important & helpful sources I used for this project!
- [YOLOv8 Model on GitHub](https://github.com/ultralytics/ultralytics )
- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
- [DJITelloPy API Reference](https://djitellopy.readthedocs.io/en/latest/tello/ )
