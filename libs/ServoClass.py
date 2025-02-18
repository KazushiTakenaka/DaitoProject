import machine
import utime

class Servo:
    def __init__(self, pin, freq=50, min_duty=500, max_duty=2500):
        """
        サーボモーターの初期化

        Args:
            pin: サーボモーターの接続ピン
            freq: PWM周波数 (デフォルト: 50Hz)
            min_duty: 最小デューティ比 (デフォルト: 500)
            max_duty: 最大デューティ比 (デフォルト: 2500)
        """
        self.pin = machine.Pin(pin, machine.Pin.OUT)  # ピンを出力に設定
        self.pwm = machine.PWM(self.pin)  # PWM制御オブジェクトを生成
        self.freq = freq  # 周波数を設定
        self.min_duty = min_duty  # 最小デューティ比
        self.max_duty = max_duty  # 最大デューティ比
        self.pwm.freq(self.freq)  # PWM周波数を設定
        self.angle_val: int = 90  # 現在の角度を初期値90度で設定

    def set_angle(self, angle: int, wait=0.0) -> None:
        """
        サーボモーターの角度を設定

        Args:
            angle: 設定する角度 (0-180度)
            wait: 待機時間 (秒)
        """
        # 角度をデューティ比に変換
        duty = int((angle / 180) * (self.max_duty - self.min_duty) + self.min_duty) * 65535 // 20000
        self.pwm.duty_u16(duty)  # デューティ比を設定
        if wait > 0:
            utime.sleep(wait)  # 待機
