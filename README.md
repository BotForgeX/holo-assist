## Holo-Assist
Holo-Assist is a projector-based interactive system that uses a camera to detect hand movements for interacting with various applications. The system includes:
1. Measuring App
2. Brick Game
3. Calculator

## Installation
Before running the project, install the required dependencies:

``pip install -r requirements.txt``

## Setup and Calibration
1. Calibrate Hand Tracking
Run the following command to calibrate hand tracking and get screen coordinates:
``python hand_calibration.py``
2. Follow the on-screen instructions to complete the calibration process.
3. Start the Home Screen
4. Once calibration is complete, launch the home screen:
``python home_screen.py``

This will provide access to the available applications.

## Controls and Gestures
1. Hover: Move the index finger over a button to highlight it.
2. Pinch Gesture: Pinch the thumb and index finger together to click/select.
3. Release Gesture: Release fingers to complete an action.

## Notes
1. Ensure that the camera is properly positioned for accurate hand tracking.
2. If calibration is unsuccessful, rerun ``hand_calibration.py``.
3. Adjust the .env file settings if needed.

## Project Modifications
This project is based on an original implementation by Concept-Bytes. The original project included AI, Spotify, and voice assistance integration. However, our team focused on refining and extending only the fully functional applications.

## Changes and Enhancements:
1. Increased accuracy of the Measuring App
2. Developed a new Calculator App with gesture-based interaction
3. Enhanced the Brick Game and added a Home Button for better navigation

## Credits  
Original Project by [Concept-Bytes](https://github.com/Concept-Bytes)

Modified and extended by [Prithivkanth](https://github.com/prithivkanth) and [Bojith_Akash](https://github.com/BOJITH14072005) 
