# Smart Glasses for Blind People - Project README

## Overview
This project aims to develop smart glasses specifically designed to assist blind individuals in recognizing persons, distances, and objects. The software component is developed using Python, while the hardware is implemented using Raspberry Pi.

## Features
1. **Person Recognition:** The smart glasses utilize facial recognition technology to identify individuals. A pre-saved photo in the "face" folder is compared with the live video feed from the Raspberry Pi camera.

2. **Distance Estimation:** The system incorporates distance measurement capabilities to provide information about the proximity of objects or persons. This is crucial for helping the user navigate their surroundings safely.

3. **Object Recognition:** The smart glasses can identify and provide information about various objects in the user's environment, enhancing their awareness.

## Hardware Requirements
- **Raspberry Pi:** The core hardware for running the smart glasses system.
- **Camera Module:** Raspberry Pi-compatible camera for capturing live video feed.

## Software Development
- **Programming Language:** Python is used for the software development of the smart glasses.
- **Facial Recognition:** The system employs facial recognition algorithms to compare a live video feed with a pre-saved photo to identify individuals.

## System Operation
The basic functionality involves comparing a pre-saved photo (stored in the "face" folder) with the live video feed from the Raspberry Pi camera. If a match is found, the system will pronounce the name associated with the recognized face.

## Getting Started
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Med-Fares-Aissa/SmartGlasses
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Setup Hardware:

Connect the Raspberry Pi and camera module.
Ensure the camera is properly configured.
Run the System:

bash
Copy code
python main.py
Contributing
Contributions to the project are welcome. If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to contributors who have helped make this project possible.

For more information or inquiries, please contact [med.fares.aissa@email.com].
