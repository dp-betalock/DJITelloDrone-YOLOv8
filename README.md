# TelloCV
Combine YOLOv8 with a DJI Tello Drone! This project allows you to see the object detection results from your computer, control the drone with the Tello app, and save the results as a video export!

### Notes
- The TelloCV_GitHubScript.py script features comments/annotations to help understand what happens at each line of code.


# Usage
## Requirements
- [Tello App](https://www.dji.com/downloads/djiapp/tello)
- [Anaconda](https://www.anaconda.com/download)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- Visual Studio Build Tools (insert more info here)
- [CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
> CUDA is for NVIDIA GPUs; CUDA Toolkit 11.8 works with PyTorch 2.1.0)

## Cloning the Repository
1. In GitHub, under the green '<> Code' button, copy the HTTPS URL
2. Open Pycharm
3. Click 'Get from VCS'
4. Paste the URL to clone the repository
- Open 'Python Interpreter' dropdown tab
- Change environment name
- Select 'Conda'
- Set Python version to 3.9

oh wait hol up

## Make Script Adjustments
1. In the script, change the video path to where you want your exported video to be located (don't forget to use \\ and not \)
2. If needed, change the name of the YOLOv8 model file to the size you want to use (ex: yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.), as it is preset to use 'yolov8s.pt'

## Installing Requirements
1. Install the requirements.txt file using:
`


## NOTICE:
- Although the script will finish, the Tello drone will remain in flight when connected to multiple devices. This means that the drone will not land, even if it's told to do so in the script (based on my experience).
- To land when connected to the computer and Tello app, use the app to lower the altitude until the drone lands.

## Troubleshooting
- If you get an error related to needing Microsoft Visual C++, go here: (link)
note: based on my experience, I needed to install the updated version and change system paths.
- If you get an error related to having multiple copies of OpenMP, . . . 
