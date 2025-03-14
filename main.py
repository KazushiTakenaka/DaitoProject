from utime import sleep
# 独自のライブラリをインポート (Servo)
from libs.ServoClass import Servo
from libs.BuzzerClass import MelodyPlayer
# test commit
def main():
    """
    メイン処理。

    サーボモーターを制御して歩行動作を行い、開始時にメロディを再生する。
    """

    """
    セットアップ
    """
    left_leg: Servo = Servo(16)  # 左足サーボモーターオブジェクトを生成
    right_leg: Servo = Servo(17)  # 右足サーボモーターオブジェクトを生成
    left_foot: Servo = Servo(18)  # 左足首サーボモーターオブジェクトを生成
    right_foot: Servo = Servo(19)  # 右足首サーボモーターオブジェクトを生成
    home(left_leg, right_leg, left_foot, right_foot, first_flag=1)  # 初期位置
    first_time:int = 0

    """
    メイン処理
    """
    while True:
        if first_time == 0:
            player: MelodyPlayer = MelodyPlayer(20)
            player.happy()
            first_time = 1

        """
        前進動作
        """
        move(left_foot, right_foot, left_leg, right_leg, 1, 0.01)
        # for _ in range(5):
        #     move(left_foot, right_foot, left_leg, right_leg, 1, 0.01)
        # home(left_leg, right_leg, left_foot, right_foot)

        """
        後進動作
        """
        # move(left_foot, right_foot, left_leg, right_leg, -1, 0.01)
        # for _ in range(5):
        #     move(left_foot, right_foot, left_leg, right_leg, -1, 0.01)
        # home(left_leg, right_leg, left_foot, right_foot)

        """
        かに歩き動作
        """
        # for _ in range(5):
        #     side_step(left_foot, right_foot, left_leg, right_leg, 1, 0.2)  # 右方向への横歩き (1: 右, -1: 左)
        # home(left_leg, right_leg, left_foot, right_foot)
        # for _ in range(5):
        #     side_step(left_foot, right_foot, left_leg, right_leg, -1, 0.2) # 左方向への横歩き
        # home(left_leg, right_leg, left_foot, right_foot)

def home(left_leg: Servo, right_leg: Servo, left_foot: Servo, right_foot: Servo, speed = 0.01, first_flag = 0):
    """
    サーボモーターを初期位置(90°)に戻す。

    Args:
        left_leg: 左足サーボモーターオブジェクト
        right_leg: 右足サーボモーターオブジェクト
        left_foot: 左足首サーボモーターオブジェクト
        right_foot: 右足首サーボモーターオブジェクト
        speed: サーボモーターの動作速度 (秒)
        first_flag: 初回実行フラグ (1: 初回, 0: 通常)
    """
    # 起動時の初期位置動作
    if first_flag == 1:
        left_foot.set_angle(90, 0.0)  # 左足首を90度に設定
        right_foot.set_angle(90, 0.0)  # 右足首を90度に設定
        left_leg.set_angle(90, 0.0)  # 左足を90度に設定
        right_leg.set_angle(90, 0.5)  # 右足を90度に設定 (0.5秒待機)
        left_foot.angle_val = 90  # 現在の角度を更新
        right_foot.angle_val = 90  # 現在の角度を更新
        left_leg.angle_val = 90  # 現在の角度を更新
        right_leg.angle_val = 90  # 現在の角度を更新
        
    # 途中に初期位置に戻す動作
    elif first_flag == 0:
        # モーターも動かす方向を制御
        if left_leg.angle_val <= 90:
            cal_val = 1
        elif left_leg.angle_val >= 90:
            cal_val = -1

        i = 0
        start_angle = left_leg.angle_val
        for i in range(start_angle, 90 + cal_val, cal_val): # 角度を順番に変化させる
            left_foot.set_angle(i)# 1つ目のサーボモーターの角度を設定
            right_foot.set_angle(i)# 2つ目のサーボモーターの角度を設定
            left_leg.set_angle(i)  # 3つ目のサーボモーターの角度を設定
            right_leg.set_angle(i, speed)  # 4つ目のサーボモーターの角度を設定 (speed秒待機)
            left_foot.angle_val = i  # 現在の角度を更新
            right_foot.angle_val = i  # 現在の角度を更新
            left_leg.angle_val = i  # 現在の角度を更新
            right_leg.angle_val = i  # 現在の角度を更新

def twin_servo_angle(servo_1: Servo , servo_2: Servo, end_angle: int, speed = 0.01) -> None:
    """
    2つのサーボモーターを同じ角度で動かす

    Args:
        servo_1: 1つ目のサーボモーターオブジェクト
        servo_2: 2つ目のサーボモーターオブジェクト
        end_angle: 終了角度
        speed: 速度 (秒)
    """
    # モーターも動かす方向を制御
    if servo_1.angle_val <= end_angle:
        cal_val = 1
    elif servo_1.angle_val >= end_angle:
        cal_val = -1

    j = 0
    start_angle = servo_1.angle_val
    for j in range(start_angle, end_angle + cal_val, cal_val): # 角度を順番に変化させる
        servo_1.set_angle(j)  # 1つ目のサーボモーターの角度を設定
        servo_2.set_angle(j, speed)  # 2つ目のサーボモーターの角度を設定 (speed秒待機)
        servo_1.angle_val = j  # 現在の角度を更新
        servo_2.angle_val = j  # 現在の角度を更新

def move(left_foot: Servo, right_foot: Servo, left_leg: Servo, right_leg: Servo,  direction = 1, speed = 0.01) -> None:
    """
    歩行動作

    Args:
        left_foot: 左足首サーボモーター
        right_foot: 右足首サーボモーター
        left_leg: 左足サーボモーター
        right_leg: 右足サーボモーター
        direction: 前進、後進切替(1=前進 -1=後進)
        speed: 速度 (秒)
    """
    angle1: int = 30  # 足の角度変化量
    angle2: int = 0
    angle3: int = 40
    angle4: int = 0
    # 変更角度を整数に調整
    if not angle1 % 2:
        angle2 = round(angle1 / 2)  # 足首の角度変化量
        angle4 = round(angle3 / 2)  # 足首の角度変化量
    elif angle1 % 2:
        angle1 = angle1 + 1
        angle3 = angle3 + 1  
        angle2 = round(angle1 / 2)  # 足首の角度変化量
        angle4 = round(angle3 / 2)  # 足首の角度変化量

    # 前進動作
    if direction == 1:
        if left_foot.angle_val == 90 and right_foot.angle_val == 90 and left_leg.angle_val == 90 and right_leg.angle_val ==90:  # 初期動作
            twin_servo_angle(left_foot, right_foot, left_foot.angle_val + angle2, speed) # 足首を少し上げる
            twin_servo_angle(left_leg, right_leg, right_leg.angle_val - angle4, speed) # 足を少し下げる

        # 歩行動作の繰り返し
        twin_servo_angle(left_foot, right_foot , left_foot.angle_val - angle1, speed) # 足首を下げる
        twin_servo_angle(left_leg, right_leg , right_leg.angle_val + angle3, speed) # 足を上げる
        twin_servo_angle(left_foot, right_foot , left_foot.angle_val + angle1, speed) # 足首を上げる
        twin_servo_angle(left_leg, right_leg , right_leg.angle_val - angle3, speed) # 足を下げる
    # 後進動作
    elif direction == -1:
        if left_foot.angle_val == 90 and right_foot.angle_val == 90 and left_leg.angle_val == 90 and right_leg.angle_val ==90:  # 最初の動作
            twin_servo_angle(left_foot, right_foot , left_foot.angle_val + angle2, speed) # 足首を少し上げる
            twin_servo_angle(left_leg, right_leg , right_leg.angle_val + angle4, speed) # 足を少し下げる

        # 歩行動作の繰り返し
        twin_servo_angle(left_foot, right_foot , left_foot.angle_val - angle1, speed) # 足首を下げる
        twin_servo_angle(left_leg, right_leg , right_leg.angle_val - angle3, speed) # 足を上げる
        twin_servo_angle(left_foot, right_foot , left_foot.angle_val + angle1, speed) # 足首を上げる
        twin_servo_angle(left_leg, right_leg ,right_leg.angle_val + angle3, speed) # 足を下げる

def side_step(left_foot: Servo, right_foot: Servo, left_leg: Servo, right_leg: Servo, direction = 1, speed = 0.01):
    """
    横歩き動作

    Args:
        left_foot: 左足首サーボ
        right_foot: 右足首サーボ
        left_leg: 左足サーボ
        right_leg: 右足サーボ
        direction: 横歩きの方向 (1: 右, -1: 左)
        speed: 速度
    """
    angle1: int = 10 # 足の角度変化量
    angle2: int = 0
    # 変更角度数値を整数に調整
    if not angle1 % 2:
        angle2 = round(angle1 / 2)  # 足首の角度変化量
    elif angle1 % 2:
        angle1 = angle1 +1
        angle2 = round(angle1 / 2)  # 足首の角度変化量


    if direction == 1:  # 右方向
        if left_foot.angle_val == 90 and right_foot.angle_val == 90 and left_leg.angle_val == 90 and right_leg.angle_val ==90:  # 初期動作
            left_foot.set_angle(left_foot.angle_val + angle2, speed)
            right_foot.set_angle(right_foot.angle_val + angle2, speed)

        # 横歩き動作の繰り返し
        left_foot.set_angle(left_foot.angle_val - angle1, speed)
        right_foot.set_angle(right_foot.angle_val - angle1, speed)
        left_foot.set_angle(left_foot.angle_val + angle1, speed)
        right_foot.set_angle(right_foot.angle_val + angle1, speed)

    elif direction == -1:  # 左方向
        if left_foot.angle_val == 90 and right_foot.angle_val == 90 and left_leg.angle_val == 90 and right_leg.angle_val ==90:  # 初期動作
            left_foot.set_angle(left_foot.angle_val - angle2, speed)
            right_foot.set_angle(right_foot.angle_val - angle2, speed)

        # 横歩き動作の繰り返し
        left_foot.set_angle(left_foot.angle_val + angle1, speed)
        right_foot.set_angle(right_foot.angle_val + angle1, speed)
        left_foot.set_angle(left_foot.angle_val - angle1, speed)
        right_foot.set_angle(right_foot.angle_val - angle1, speed)

main()  # メイン関数を実行