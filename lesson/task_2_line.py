"""
Задача 2: Следование по линии.
Робот едет по чёрной линии, поворачивая при отклонении.
"""


def run_robot(bot):
    while True:
        line_left = bot.line_left.read()
        line_center = bot.line_sensor.read()
        line_right = bot.line_right.read()

        on_left = line_left < 3500
        on_right = line_right < 3500

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
