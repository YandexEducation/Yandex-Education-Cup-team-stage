"""
Готовый скрипт для урока «Симулятор и сенсоры робота».
Скачайте этот файл и загрузите в симулятор для выполнения практических заданий.

Использование: откройте симулятор, загрузите этот скрипт, выберите карту и нажмите «Старт».
"""


def run_robot(bot):
    """Минимальный скрипт следования по линии с реакцией на знаки."""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    OFF = (0, 0, 0)

    # Стартовый сигнал — мигание зелёным
    bot.leds.fill(GREEN)
    bot.leds.write()
    yield bot.sleep(0.5)
    bot.leds.fill(OFF)
    bot.leds.write()
    yield bot.sleep(0.5)

    while True:
        # Читаем датчики линии
        line_left = bot.line_left.read()
        line_center = bot.line_sensor.read()
        line_right = bot.line_right.read()

        # Знак от камеры
        sign = bot.camera.detect_sign()

        on_left = line_left < 3500
        on_center = line_center < 3500
        on_right = line_right < 3500

        # Реакция на знаки
        if sign == "STOP":
            bot.leds.fill(RED)
            bot.leds.write()
            bot.motors.stop()
            yield bot.sleep(2.0)
            bot.leds.fill(OFF)
            bot.leds.write()
            continue

        elif sign == "GO":
            bot.leds.fill(GREEN)
            bot.leds.write()
            bot.motors.move(50, 50)
            yield bot.sleep(1.5)
            bot.leds.fill(OFF)
            bot.leds.write()
            continue

        elif sign == "LEFT":
            bot.leds.fill(YELLOW)
            bot.leds.write()
            bot.motors.move(40, -40)
            yield bot.sleep(0.5)
            bot.leds.fill(OFF)
            bot.leds.write()
            continue

        elif sign == "RIGHT":
            bot.leds.fill(YELLOW)
            bot.leds.write()
            bot.motors.move(-40, 40)
            yield bot.sleep(0.5)
            bot.leds.fill(OFF)
            bot.leds.write()
            continue

        # Логика следования по линии
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
