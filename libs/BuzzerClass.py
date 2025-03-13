import machine
import utime

class MelodyPlayer:
    """メロディを再生するクラス。"""

    def __init__(self, pin_num: int = 1) -> None:
        """コンストラクタ。

        Args:
            pin_num: ブザーが接続されたピン番号。
        """
        self.buzzer_pin: machine.Pin = machine.Pin(pin_num, machine.Pin.OUT)
        self.buzzer_pwm: machine.PWM = machine.PWM(self.buzzer_pin, freq=50, duty_u16=8192)
        self.C3: int = 131
        self.D3: int = 147
        self.E3: int = 165
        self.F3: int = 175
        self.G3: int = 196
        self.C4: int = 262
        self.D4: int = 294
        self.E4: int = 330
        self.F4: int = 349
        self.G4: int = 392
        self.A4: int = 440
        self.B4: int = 494
        self.C5: int = 523

    def tone(self, frequency: int) -> None:
        """指定された周波数の音を再生する。

        Args:
            frequency: 再生する周波数。
        """
        self.buzzer_pwm.freq(frequency)

    def play_melody(self, notes: list[int], rhythm: list[float]) -> None:
        """指定された音階とリズムでメロディを再生する。

        Args:
            notes: 音階のリスト。
            rhythm: リズムのリスト。
        """
        for note, duration in zip(notes, rhythm):
            self.tone(note)
            utime.sleep(duration)
        self.buzzer_pwm.duty_u16(0)

    def happy(self) -> None:
        """うれしい感情のメロディを再生する。"""
        notes: list[int] = [self.C4, self.E4, self.G4, self.C5, self.C5, self.G4, self.E4, self.C4]
        rhythm: list[float] = [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.4]
        self.play_melody(notes, rhythm)

    def sad(self) -> None:
        """悲しい感情のメロディを再生する。"""
        notes: list[int] = [self.G4, self.E4, self.C4, self.D4, self.G3]
        rhythm: list[float] = [0.4, 0.4, 0.4, 0.8, 1.0]
        self.play_melody(notes, rhythm)

    def surprise(self) -> None:
        """驚きの感情のメロディを再生する。"""
        notes: list[int] = [self.C4, self.C5, self.C4, self.C5, self.C4, self.C5]
        rhythm: list[float] = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
        self.play_melody(notes, rhythm)

    def angry(self) -> None:
        """怒りの感情のメロディを再生する。"""
        notes: list[int] = [self.C3, self.C3, self.D3, self.E3, self.F3]
        rhythm: list[float] = [0.2, 0.2, 0.2, 0.2, 1]
        self.play_melody(notes, rhythm)

    def question(self) -> None:
        """疑問の感情のメロディを再生する。"""
        notes: list[int] = [self.G4, self.A4, self.G4, self.C5, self.B4, self.A4, self.G4]
        rhythm: list[float] = [0.2, 0.2, 0.2, 0.4, 0.2, 0.2, 0.4]
        self.play_melody(notes, rhythm)