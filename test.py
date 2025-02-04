import serial
import time

# تحديد منفذ الـ Arduino (استبدله بالمنفذ الصحيح مثل COM3 أو /dev/ttyUSB0)
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)  # الانتظار حتى يتم تجهيز الاتصال

def move_servo(angle):
    if 0 <= angle <= 180:
        arduino.write(f"{angle}\n".encode())  # إرسال الزاوية إلى Arduino
        time.sleep(0.5)  # انتظار استجابة المحرك
        response = arduino.readline().decode().strip()  # قراءة الاستجابة
        print(response)  # طباعة التأكيد من Arduino
    else:
        print("الزاوية يجب أن تكون بين 0 و 180 درجة.")

# تجربة تحريك المحرك إلى زوايا مختلفة
move_servo(0)
time.sleep(1)
move_servo(90)
time.sleep(1)
move_servo(180)
