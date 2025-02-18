import machine
import utime
from libs.ServoClass import Servo

class Daiton:
    def __init__(self, right_leg_pin = 2, left_leg_pin = 3, right_foot_pin = 4, left_foot_pin = 5, freq=50, min_duty=500, max_duty=2500):
        self.left_leg: Servo = Servo(left_leg_pin)
        self.right_leg: Servo = Servo(right_leg_pin)
        self.left_foot: Servo = Servo(left_foot_pin)
        self.right_foot: Servo = Servo(right_foot_pin)

    def move(self, direction = "forward", speed = "nomal") -> None:
        """
        Args:
            direction: 進行方向 forward or backward or turn_left or turn_right
            speed: スピード slow or mormal or fast
        """
        self.left_leg.set_angle(45, 0.0)
        self.right_leg.set_angle(45,0.5)
        self.left_leg.set_angle(90, 0.0)
        self.right_leg.set_angle(90,0.5)
        self.left_leg.set_angle(135, 0.0)
        self.right_leg.set_angle(135,0.5)
        self.left_leg.set_angle(90, 0.0)
        self.right_leg.set_angle(90,0.5)

    def dance(self, type = "moonwalk_left", speed = "noamal") -> None:
        """
        Args:
            type: ダンスの種類 moonwalk_right
            speed: スピード slow or mormal or fast
        """
        pass