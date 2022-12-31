import random

import utime
from machine import Pin


class MotorController:
    def __init__(self):
        self.m1 = Pin(19, Pin.OUT)
        self.m2 = Pin(18, Pin.OUT)
        self.en1 = Pin(16, Pin.OUT)   

    def enable(self):
        self.en1(1)  

    def forward(self):
        self.m1(1)
        self.m2(0)
    
    def reverse(self):
        self.m1(0)
        self.m2(1)
    
    def stop(self):
        self.m1(0)
        self.m2(0)
        
def main():
    random_num = random.random()
    utime.sleep(1)
    if random_num < 0.1:
        motor_controller = MotorController()
        motor_controller.enable()
        motor_controller.forward()
        utime.sleep(1)
        motor_controller.stop()
        utime.sleep(2)
        motor_controller.reverse()
        utime.sleep(1)
        motor_controller.stop()
    else:
        print("Not triggered")
        
if __name__ == "__main__":
    while True:
        main()