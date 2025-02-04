#include <Servo.h>

Servo myServo; // إنشاء كائن لمحرك السيرفو
int angle = 0; // زاوية المحرك

void setup() {
    Serial.begin(9600); // بدء الاتصال التسلسلي
    myServo.attach(4);  // توصيل المحرك على المنفذ 9
    myServo.write(angle); // ضبط الزاوية الافتراضية
}

void loop() {
    if (Serial.available() > 0) {
        int newAngle = Serial.parseInt(); // قراءة الرقم القادم من بايثون
        if (newAngle == 100) {  // إذا كان الأمر 100، افتح الباب وانتظر 6 ثوانٍ
            myServo.write(100);
            Serial.println("Servo opened to 100 degrees.");
            delay(6000);  // انتظر 6 ثوانٍ
            myServo.write(0);  // أعد الباب إلى 0 درجة
            Serial.println("Servo closed to 0 degrees.");
        }
    }
}
