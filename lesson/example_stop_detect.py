"""
Пример из справочника: детекция STOP.
Робот едет вперёд, при виде знака STOP — останавливается на 2 секунды.
"""


def run_robot(bot):
    while True:
        sign = bot.camera.detect_sign()
        if sign == "STOP":
            bot.motors.stop()
            yield bot.sleep(2.0)
        else:
            bot.motors.move(40, 40)
        yield bot.sleep(0.05)
