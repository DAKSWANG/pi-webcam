# -*- coding:utf-8 -*-
#讓紅色LED燈分成0-100等級亮度
# 豬頭胖胖
import RPi.GPIO as GPIO
led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

while True:
   duty_s = raw_input("請輸入亮度值(0~100):")
   duty = int(duty_s)
   pwm_led.ChangeDutyCycle(duty)