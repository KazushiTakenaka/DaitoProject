import machine
import utime

class MelodyPlayer:
    def __init__(self, pin_num=15):
        self.buzzer_pin = machine.Pin(pin_num, machine.Pin.OUT)
        self.buzzer_pwm = machine.PWM(self.buzzer_pin, freq=50, duty_u16=8192)

    def tone(self, frequency):
        self.buzzer_pwm.freq(frequency)

    def play_melody(self, notes, rhythm):
        for note, duration in zip(notes, rhythm):
            self.tone(note)
            utime.sleep(duration)
        self.buzzer_pwm.duty_u16(0)
    
    def merry_chiristmas(self):
        player = MelodyPlayer()

        # メリークリスマスのメロディー
        notes = [262, 294, 330, 349, 392, 440, 494, 523]
        rhythm = [0.5, 0.5, 1, 0.5, 0.5, 1, 1, 1]
        player.play_melody(notes, rhythm)

# 使用例
"""
if __name__ == "__main__":
    player = MelodyPlayer()

    # メリークリスマスのメロディー
    notes = [262, 294, 330, 349, 392, 440, 494, 523]
    rhythm = [0.5, 0.5, 1, 0.5, 0.5, 1, 1, 1]
    player.play_melody(notes, rhythm)
"""