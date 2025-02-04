# Automatic-License-Plate-Recognition-ALPR-System-with-Access-Control

Project Description:
This project is an Automatic License Plate Recognition (ALPR) system integrated with access control using an Arduino-controlled servo mechanism. The system is designed to detect and recognize vehicle license plates in real-time using a camera, check the recognized plate number against a pre-defined list stored in an Excel file, and control access by activating a servo motor if the plate number is authorized.

Key Features:
License Plate Detection and Recognition:

Utilizes a YOLO-based deep learning model for detecting license plates in video frames.

Employs a mobile Vision Transformer (ViT) model for Optical Character Recognition (OCR) to extract the license plate number.

Excel-Based Authorization:

The system checks the recognized license plate number against a list of authorized plates stored in an Excel file (car_numbers.xlsx).

If the plate number is found in the Excel file, the system grants access by activating the servo motor.

Arduino-Controlled Servo Mechanism:

The system communicates with an Arduino via a serial connection to control a servo motor.

When an authorized plate is detected, the servo motor moves to a specific angle (e.g., 100 degrees) to simulate access control (e.g., opening a gate or barrier). After a delay, the servo returns to its original position.

Real-Time Video Processing:

The system captures live video from a camera and processes each frame to detect and recognize license plates.

Annotated frames with detected plates and OCR results are displayed in real-time for monitoring.

Multi-Threading for Smooth Operation:

The servo control is handled in a separate thread to ensure that the camera feed and plate recognition process are not interrupted.

User-Friendly Interface:

The system provides real-time feedback in the console and displays the processed video feed with annotations.

Users can exit the program by pressing the q key.

Applications:
Parking Management: Automate entry and exit for authorized vehicles in parking lots.

Security Checkpoints: Control access to restricted areas based on vehicle registration.

Toll Booths: Automate toll collection for registered vehicles.

Traffic Monitoring: Identify and log vehicles for traffic management purposes.

Technologies Used:
Python: The main programming language for the project.

OpenCV: For video capture, frame processing, and displaying results.

Fast ALPR: A library for license plate detection and OCR.

OpenPyXL: For reading and processing Excel files.

Arduino: For controlling the servo motor.

Threading: To handle servo control without interrupting the main video processing loop.

How It Works:
The system captures live video from a camera.

Each frame is processed to detect and recognize license plates using the ALPR model.

The recognized plate number is checked against the Excel file for authorization.

If the plate number is authorized, the system sends a command to the Arduino to activate the servo motor.

The servo motor moves to a specific angle to simulate access control and then returns to its original position after a delay.

The process continues in real-time until the user exits the program.

Future Enhancements:
Database Integration: Replace the Excel file with a database for scalability.

Cloud Connectivity: Store logs of recognized plates and access events in the cloud.

Advanced Security: Add features like facial recognition or RFID for multi-factor authentication.

Mobile App: Develop a mobile app for remote monitoring and control.

This project demonstrates the integration of computer vision, machine learning, and hardware control to create a practical and efficient access control system. It can be adapted for various real-world applications requiring automated vehicle identification and access management.

