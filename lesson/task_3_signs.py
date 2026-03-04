"""
Задача 3: Реакция на знаки.
Робот останавливается на STOP, поворачивает на LEFT/RIGHT, едет вперёд на GO.
"""


def run_robot(bot):
    while True:
        line_left = bot.line_left.read()
        line_center = bot.line_sensor.read()
        line_right = bot.line_right.read()
        sign = bot.camera.detect_sign()

        on_left = line_left < 3500
        on_right = line_right < 3500

        if sign == "STOP":
            bot.motors.stop()
            yield bot.sleep(2.0)
            continue
        elif sign == "GO":
            bot.motors.move(50, 50)
            yield bot.sleep(1.5)
            continue
        elif sign == "LEFT":
            bot.motors.move(40, -40)
            yield bot.sleep(0.5)
            continue
        elif sign == "RIGHT":
            bot.motors.move(-40, 40)
            yield bot.sleep(0.5)
            continue

        if on_left and on_right:
            bot.motors.stop()
            yield bot.sleep(0.3)
        elif on_left:
            bot.motors.move(-10, 10)
        elif on_right:
            bot.motors.move(10, -10)
        else:
            bot.motors.move(30, 30)

        yield bot.sleep(0.05)
