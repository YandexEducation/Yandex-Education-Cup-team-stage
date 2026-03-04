"""
Задача 1: Запуск симулятора.
Скачайте и загрузите в симулятор — робот поедет вперёд 2 секунды и остановится.
"""


def run_robot(bot):
    bot.motors.move(50, 50)
    yield bot.sleep(2.0)
    bot.motors.stop()
