"""
Задача 4: LED-подсветка.
Робот мигает разными цветами: зелёный → красный → жёлтый → синий.
"""


def run_robot(bot):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    OFF = (0, 0, 0)

    colors = [GREEN, RED, YELLOW, BLUE]
    for color in colors:
        bot.leds.fill(color)
        bot.leds.write()
        yield bot.sleep(1.0)
        bot.leds.fill(OFF)
        bot.leds.write()
        yield bot.sleep(0.3)

    # Дальше едем по линии с подсветкой
    while True:
        sign = bot.camera.detect_sign()
        line_left = bot.line_left.read()
        line_right = bot.line_right.read()

        if sign == "STOP":
            bot.leds.fill(RED)
            bot.leds.write()
            bot.motors.stop()
            yield bot.sleep(2.0)
            continue
        elif sign == "GO":
            bot.leds.fill(GREEN)
            bot.leds.write()
        elif sign in ("LEFT", "RIGHT"):
            bot.leds.fill(YELLOW)
            bot.leds.write()
        else:
            bot.leds.fill(OFF)
            bot.leds.write()

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
