import time

NUM_RUNS = 10  # число прогонов


class TimeThis:
    def __init__(self, num_runs):  # конструктору передаем число прогонов
        self.num_runs = num_runs
        self.avg_time = 0
        self.t0 = 0
        self.t1 = 0

    def __call__(self, func):  # оборачиваемую функцию передаем методу __call__
        def wrapper(*args, **kwargs):  # а аргументы - внутренней функции
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("[Декоратор] Выполнение заняло %.5f секунд" % avg_time)

        return wrapper

    def __enter__(self):
        """
        Реализация контекстного менеджера.
        на входе фиксируем время начала выполнения блока
        """
        self.t0 = time.time()


    def __exit__(self, exc_type, exc_value, traceback):
        """
        на выходе фиксируем время окончания выполнения блока и рассчитываем среднее значение
        """
        self.t1 = time.time()
        self.avg_time += (self.t1 - self.t0) / self.num_runs
        print("[Контекстный менеджер] Выполнение заняло %.5f секунд" % self.avg_time)


def foo(iter):
    for j in range(iter):
        pass

@TimeThis(NUM_RUNS)
def bar(iter):
    for j in range(iter):
        pass



def main():
    with TimeThis(NUM_RUNS):
        for _ in range(NUM_RUNS):
            foo(1000000)

    bar(1000000)



if __name__ == "__main__":
    main()