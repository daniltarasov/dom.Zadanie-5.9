import time


class TimeThis:
    def __init__(self, num_runs):  # конструктору передаем число прогонов
        self.num_runs = num_runs

    def __call__(self, func):  # оборачиваемую функцию передаем методу __call__
        def wrapper(*args, **kwargs):  # а аргументы - внутренней функции
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)

        return wrapper


@TimeThis(10)
def f(iter):
    for j in range(iter):
        pass


f(1_000_000)
