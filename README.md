
# Automatic License Plate Recognition (ALPR) System with Access Control

## Overview
This project is an **Automatic License Plate Recognition (ALPR) system** integrated with **access control** using an Arduino-controlled servo mechanism. The system detects and recognizes vehicle license plates in real-time using a camera, checks the recognized plate number against a pre-defined list stored in an Excel file, and controls access by activating a servo motor if the plate number is authorized.

---

## Features
1. **License Plate Detection and Recognition**:
   - Utilizes a **YOLO-based deep learning model** for detecting license plates in video frames.
   - Employs a **mobile Vision Transformer (ViT) model** for Optical Character Recognition (OCR) to extract the license plate number.

2. **Excel-Based Authorization**:
   - Checks the recognized license plate number against a list of authorized plates stored in an **Excel file** (`car_numbers.xlsx`).
   - Grants access by activating the servo motor if the plate number is found in the Excel file.

3. **Arduino-Controlled Servo Mechanism**:
   - Communicates with an **Arduino** via a serial connection to control a servo motor.
   - Moves the servo to a specific angle (e.g., 100 degrees) to simulate access control (e.g., opening a gate or barrier) and returns it to its original position after a delay.

4. **Real-Time Video Processing**:
   - Captures live video from a camera and processes each frame to detect and recognize license plates.
   - Displays annotated frames with detected plates and OCR results in real-time.

5. **Multi-Threading for Smooth Operation**:
   - Handles servo control in a separate thread to ensure uninterrupted camera feed and plate recognition.

6. **User-Friendly Interface**:
   - Provides real-time feedback in the console and displays the processed video feed with annotations.
   - Allows users to exit the program by pressing the `q` key.

---

## Applications
- **Parking Management**: Automate entry and exit for authorized vehicles in parking lots.
- **Security Checkpoints**: Control access to restricted areas based on vehicle registration.
- **Toll Booths**: Automate toll collection for registered vehicles.
- **Traffic Monitoring**: Identify and log vehicles for traffic management purposes.

---

## Technologies Used
- **Python**: The main programming language for the project.
- **OpenCV**: For video capture, frame processing, and displaying results.
- **Fast ALPR**: A library for license plate detection and OCR.
- **OpenPyXL**: For reading and processing Excel files.
- **Arduino**: For controlling the servo motor.
- **Threading**: To handle servo control without interrupting the main video processing loop.

---

## How It Works
1. The system captures live video from a camera.
2. Each frame is processed to detect and recognize license plates using the ALPR model.
3. The recognized plate number is checked against the Excel file for authorization.
4. If the plate number is authorized, the system sends a command to the Arduino to activate the servo motor.
5. The servo motor moves to a specific angle to simulate access control and then returns to its original position after a delay.
6. The process continues in real-time until the user exits the program.

---

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   pip install opencv-python serial openpyxl fast-alpr
   ```

2. **Prepare Excel File**:
   - Create an Excel file named `car_numbers.xlsx` with a list of authorized license plate numbers in the first column.

3. **Connect Arduino**:
   - Upload the servo control code to the Arduino.
   - Connect the Arduino to the computer and note the serial port (e.g., `COM6` or `/dev/ttyUSB0`).

4. **Run the Program**:
   ```bash
   python main.py
   ```

5. **Exit the Program**:
   - Press the `q` key to stop the program.

---

## Future Enhancements
- **Database Integration**: Replace the Excel file with a database for scalability.
- **Cloud Connectivity**: Store logs of recognized plates and access events in the cloud.
- **Advanced Security**: Add features like facial recognition or RFID for multi-factor authentication.
- **Mobile App**: Develop a mobile app for remote monitoring and control.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Thanks to the developers of **OpenCV**, **Fast ALPR**, and **OpenPyXL** for their amazing libraries.
- Special thanks to the Arduino community for providing robust hardware control solutions.

---

