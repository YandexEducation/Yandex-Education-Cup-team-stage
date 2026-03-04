"""
Пример из справочника: моторы и yield.
Скачайте и загрузите в симулятор — робот поедет вперёд, повернёт влево и остановится.
"""


def run_robot(bot):
    bot.motors.move(50, 50)      # вперёд
    yield bot.sleep(1.0)         # обязательно yield!
    bot.motors.move(-30, 30)     # поворот влево
    yield bot.sleep(0.5)
    bot.motors.stop()
