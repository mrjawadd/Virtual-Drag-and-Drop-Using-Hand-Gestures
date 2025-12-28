# Virtual Drag and Drop Using Hand Gestures

A computer vision-based application that allows users to interact with virtual objects using hand gestures. This app leverages OpenCV and hand tracking techniques to detect pinch gestures in real-time, enabling you to drag and move objects on your screen without any physical input device. Ideal for gesture-based UI experiments, interactive demos, or just a fun tech project.

## Features

* **Real-time Hand Tracking:** Detects hand and finger positions using computer vision.
* **Pinch Gesture Detection:** Recognizes pinch gestures to grab and move virtual objects.
* **Drag and Drop Interaction:** Allows smooth dragging of objects across the screen using hand gestures.
* **Lightweight and Fast:** Works efficiently in real-time with standard webcams.

## How to Run

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Run the main program:

   ```bash
   python main.py
   ```
3. Use your hand to interact with the objects.
4. Press `Q` or `ESC` to exit the application.

## Requirements

* Python 3.x
* Webcam (built-in or external)
* Libraries: OpenCV, MediaPipe (for hand tracking), and other dependencies listed in `requirements.txt`.

## Usage Tips

* Ensure proper lighting for better hand detection.
* Keep your hand within the webcam frame for smooth interactions.
* Experiment with different gestures and object sizes to see how the detection performs.

## Future Improvements

* Add support for multi-hand interactions.
* Enable more complex gestures like zooming, rotating, or resizing objects.
* Integrate with AR/VR environments for immersive experiences.
