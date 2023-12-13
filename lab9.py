import random
import datetime

# Функция для логирования
def log(message):
    # Получаем текущую дату и время
    now = datetime.datetime.now()

    # Преобразуем время в строку
    timeString = now.strftime("[%Y-%m-%d %H:%M:%S]")

    # Выводим дату и время, а затем сообщение
    print(timeString, message)

def main():
    # Вводим количество бочек N
    N = int(input("Введите количество бочек N: "))
    log("Ввод N: " + str(N))

    # Создаем список для хранения бочек
    meshok = list(range(1, N+1))

    log("Вытаскиваем бочонки:")

    while len(meshok) > 0:
        randomIndex = random.randint(0, len(meshok) - 1)

        # Выводим номер вытянутого бочонка
        log("Вытянутый бочонок: " + str(meshok[randomIndex]))
        
        del meshok[randomIndex]

    log("Все бочонки вытянуты!")

if __name__ == "__main__":
    main()